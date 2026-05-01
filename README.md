# ai-voice-ivr
# 🎧 AI Voice IVR System

A complete AI-powered Interactive Voice Response (IVR) system built using **Twilio, Dialogflow, Flask, and Ngrok**.

This system allows users to **call a phone number and interact using voice**, where AI understands user intent and responds dynamically.

---

## 🚀 Features

* 📞 Real-time phone call handling using Twilio
* 🗣️ Voice-based interaction (Speech Recognition)
* 🤖 AI intent detection using Dialogflow
* 🔁 Continuous conversation flow (no button pressing required)
* ⚡ Fast backend using Flask
* 🌐 Public access using Ngrok

---

## 🧠 How It Works

```plaintext
User Call → Twilio → Flask Server → Dialogflow (AI)
                                ↓
                        AI Response → Twilio Voice Reply
```

---

## 🛠️ Tech Stack

* Python (Flask)
* Twilio Voice API
* Dialogflow (Google Cloud)
* Ngrok (for tunneling)
* Git & GitHub

---

## 📦 Project Structure

```plaintext
dialogflow-webhook/
│
├── app.py          # Main Flask backend
├── README.md       # Project documentation
├── .gitignore      # Ignore sensitive files
└── venv/           # Virtual environment (not uploaded)
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/arshikhan229/ai-voice-ivr.git
cd ai-voice-ivr
```

---

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install flask
```

---

### 4. Run the server

```bash
python app.py
```

---

### 5. Start ngrok

```bash
ngrok http 5000
```

---

### 6. Configure Twilio

Set webhook URL:

```plaintext
https://your-ngrok-url/menu
```

---

## 📞 Example Usage

1. Call the Twilio number

2. Speak naturally:

   * "I need support"
   * "billing issue"
   * "sales"

3. AI will understand and respond accordingly

---

## 🔐 Security Note

* Do NOT upload:

  * `key.json`
  * `.env`
  * `venv/`

---

## 🌟 Future Improvements

* Live agent transfer
* CRM / ERPNext integration
* Database for order tracking
* GPT-based conversational AI
* Deployment on cloud (Render / Railway)

---

## 👩‍💻 Author

**Arshi Khan**
AI Engineer | Voice AI Developer

---

## 💬 License

This project is open-source and available for learning and development purposes.
