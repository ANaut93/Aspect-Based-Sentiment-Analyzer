


from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy
from textblob import TextBlob

app = Flask(__name__)
CORS(app)

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Spacy model 'en_core_web_sm' not found.")
    print("Please run this command in your terminal: python -m spacy download en_core_web_sm")
    exit()



@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    if not request.json or 'review_text' not in request.json:
        return jsonify({'error': 'Invalid request.'}), 400

    text = request.json['review_text']

   
    doc = nlp(text)
    aspects = []
    sentiment_scores = []

    for token in doc:
        if token.pos_ == 'ADJ':
            opinion_word = token.text

        
            subject_noun = None
            for ancestor in token.ancestors:
                if ancestor.pos_ == 'NOUN':
                    subject_noun = ancestor.text
                    break 

            if subject_noun:
                polarity = TextBlob(opinion_word).sentiment.polarity

                if polarity > 0.1:
                    sentiment_label = 'Positive'
                elif polarity < -0.1:
                    sentiment_label = 'Negative'
                else:
                    sentiment_label = 'Neutral'
                
                aspects.append({'term': subject_noun, 'sentiment': sentiment_label})
                sentiment_scores.append(polarity)

    unique_aspects = {}
    for aspect in aspects:
        if aspect['term'] not in unique_aspects:
            unique_aspects[aspect['term']] = aspect['sentiment']
    

    if not sentiment_scores:
        overall_sentiment_label = 'Neutral'
    else:
        average_polarity = sum(sentiment_scores) / len(sentiment_scores)
        if average_polarity > 0.2: 
            overall_sentiment_label = 'Positive'
        elif average_polarity < -0.2: 
            overall_sentiment_label = 'Negative'
        else:
            overall_sentiment_label = 'Mixed'

    
    response_data = {
        "overallSentiment": overall_sentiment_label,
        "aspects": unique_aspects
    }

    return jsonify(response_data)


if __name__ == '__main__':
    print("Starting Flask server with upgraded logic...")
    app.run(debug=True, port=5000)

