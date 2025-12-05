Aspect-Based Sentiment Analyser

A full-stack machine learning application that goes beyond simple positive/negative classification. This tool analyzes customer reviews to identify specific aspects (like "camera", "battery", "screen") and determines the sentiment for each one independently.

📌 About the Project

Traditional sentiment analysis often fails with mixed reviews (e.g., "The camera is amazing, but the battery life is terrible"). Most systems would classify this as "Neutral."

This project solves that problem.

It uses Natural Language Processing (NLP) to grammatically link adjectives to nouns, allowing it to understand that the user is Positive about the Camera but Negative about the Battery.

Key Features

Granular Analysis: Extracts specific features from the text.

NLP Pipeline: Uses spaCy for dependency parsing and Part-of-Speech tagging.

Sentiment Scoring: Uses TextBlob to calculate polarity scores.

Visual Dashboard: Real-time bar chart visualization using Chart.js.

📂 Project Structure

This repository contains the source code for the application. Note: Heavy libraries (like venv or node_modules) are excluded to keep the repository clean. You will need to install the dependencies listed below.

app.py: The Flask backend server and NLP logic.

templates/sentiment_dashboard.html: The frontend user interface.

requirements.txt: List of Python libraries required.

⚙️ Setup & Installation

Follow these steps to get the project running on your local machine.



2. Install Dependencies

Since the library files are not included in the repo, you need to install them using pip:

pip install flask flask-cors spacy textblob


Alternatively, if a requirements.txt file is present:

pip install -r requirements.txt


3. Download the Language Model

This project uses the English core web model from spaCy. You must download it separately:

python -m spacy download en_core_web_sm


4. Run the Application

Start the Flask server:

python app.py


You should see output indicating the server is running (usually on http://127.0.0.1:5000).

5. Open the Dashboard

Open your web browser and navigate to the sentiment_dashboard.html file, or simply drag that file into your browser window.

🛠️ Technologies Used

Python 3.x

Flask (Web Framework)

spaCy (NLP & Dependency Parsing)

TextBlob (Sentiment Polarity)

JavaScript / Chart.js (Visualization)

Tailwind CSS (Styling)

📧 Contact

Developed by Amit Nautiyal 
Graphic Era Hill University
MCA 2024-26
