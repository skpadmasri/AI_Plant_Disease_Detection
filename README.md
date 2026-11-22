# 🌿 AI-Powered Plant Disease Detection & Diagnosis System

An end-to-end Deep Learning and Generative AI web application built with **Python, Django, TensorFlow/Keras (MobileNet), and Google Gemini API**. It detects plant leaf diseases from uploaded images and provides an interactive AI Plant Pathology Chatbot for treatment, symptoms, and prevention guidance.

## 🚀 Key Features
- **Automated Disease Classification:** Uses a trained MobileNet Convolutional Neural Network (`mudra_mobilenet_model.h5`) to identify plant leaf diseases with confidence scores.
- **AI Plant Pathology Assistant:** Integrated **Google Gemini API** chatbot (`Users/views.py`) that answers follow-up questions about the detected disease, fungicides, organic remedies, and prevention.
- **Role-Based Access Control:** Separate dashboards for **Users** (registration, login, image prediction, training metrics view, AI chatbot) and **Admins** (user approval management, model evaluation).
- **Training Metrics Visualization:** Displays epoch-wise training and validation accuracy/loss metrics (`training_metrics.csv`).

## 🛠️ Tech Stack
- **Backend:** Python, Django
- **Deep Learning & Data Science:** TensorFlow, Keras (MobileNet), NumPy, Pandas, Scikit-learn
- **Generative AI:** Google GenAI SDK (`gemini-2.5-flash` / `gemini-flash-latest`)
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
- **Database:** SQLite3

## ⚙️ Local Setup Instructions
1. Clone the repository:
   git clone https://github.com/skpadmasri/AI_Plant_Disease_Detection.git
   cd AI_Plant_Disease_Detection

2. Install dependencies:
   pip install django tensorflow numpy pandas scikit-learn google-genai pillow

3. Configure your Gemini API Key in AI_Powered_Plant_Disease_Detection/settings.py:
   GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

4. Run database migrations and start the server:
   python manage.py migrate
   python manage.py runserver

Open http://127.0.0.1:8000/ in your browser.
             

   
