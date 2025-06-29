# ✉️ Enhanced Email Generator (Powered by Groq LLaMA3)

This is a simple yet powerful Streamlit web app that generates professional, formal, or casual email responses using the [Groq API](https://groq.com/) and LLaMA3 model. It allows users to input sender and recipient details, define a writing style, and generate AI-crafted email responses in seconds.

## 🚀 Features

- Input sender and recipient email/name
- Choose writing style (Formal, Casual, Professional, Friendly, Polite)
- Define subject line and email prompt
- Personalize greeting with recipient name
- Adjustable max token limit
- View, copy, and download generated email content

## 📦 Prerequisites

Before running the app, ensure the following:

- Python 3.7+
- Groq API Key (sign up at [Groq](https://console.groq.com/) to get one)

## 🛠 Installation

1. Clone the repository:
 ```bash
   git clone https://github.com/your-username/enhanced-email-generator.git
   cd enhanced-email-generator

```  
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your Groq API key inside the script or use environment variables for production safety.
 ```bash
streamlit run app.py
```

## 📄 File Structure
bash
Copy
Edit
enhanced-email-generator/
│
├── app.py              # Main Streamlit application
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies


## 🧠 Sample Input & Output
Input:
Sender: john.doe@example.com
Recipient: jane.smith@example.com
Style: Professional
Prompt: "Generate a follow-up email after a meeting to discuss next steps."
Subject: "Next Steps from Our Meeting"

Output:
A personalized, structured email with greeting, body, and closing, which can be copied or downloaded.

## 📌 Notes
The model used is llama3-8b-8192 from Groq.

Default temperature is set to 0.7 for balanced creativity and coherence.

Max tokens slider allows control over response length (50–500 tokens).
