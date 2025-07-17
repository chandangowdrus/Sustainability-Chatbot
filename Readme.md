Here’s a complete `README.md` file tailored to your **Sustainability Chatbot** project that uses the **Gemini API**, allows users to ask sustainability-related questions, and extracts context from a Sustainability Report PDF:

---

````markdown
# 🌱 Sustainability Chatbot

A simple AI-powered chatbot that answers questions related to sustainability based on the contents of a provided Sustainability Report (PDF). Powered by **Google Gemini Pro API**.

---

## 📌 Features

- 📄 Extracts text from uploaded Sustainability Report (PDF)
- 🤖 Uses Gemini Pro to generate intelligent responses
- 💬 Chat interface built with Flask
- 🧠 Remembers and uses context for better answers
- 🔐 Keeps your API key secure using `.env` file

---

## 🧰 Tech Stack

- Python 3.8+
- Flask
- Google Gemini API (Generative Language API)
- PyMuPDF (`fitz`) for PDF text extraction
- `python-dotenv` for loading secrets
- `requests` for API communication

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/chandangowdrus/Sustainability-Chatbot.git
cd Sustainability-Chatbot
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your Gemini API Key

Create a `.env` file in the root of the project:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

> ⚠️ **Do not share or push your `.env` file.** It contains your secret API key.

### 4. Run the app

```bash
python app.py
```

Then visit:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🖼️ Screenshot

> Chatbot UI with PDF upload and question input (Optional: Insert an image here)

---

## 📝 Usage

1. Upload any **Sustainability Report PDF** (like Infosys, TCS, etc.)
2. Type your question like:

   * *"What are the carbon reduction goals?"*
   * *"How does the company handle water conservation?"*
3. Receive accurate, context-aware answers from the AI.

---

## 📁 Project Structure

```
Sustainability-Chatbot/
│
├── templates/
│   └── index.html         # Chatbot front-end
├── static/
│   └── style.css          # Optional: Styling
├── app.py                 # Main Flask backend
├── .env                   # API key (not pushed)
├── requirements.txt       # Python dependencies
└── README.md              # You're here!
```

---

## 🔒 Security

* Keep `.env` file private.
* Never hardcode or share API keys publicly.
* Use GitHub secret scanning protection.

---

## 💡 Example Sustainability Reports

You can use publicly available reports like:

* [Infosys Sustainability Report](https://www.infosys.com/sustainability/resource-center/Documents/infosys-esg-report-2022-23.pdf)
* [Microsoft Sustainability Report](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RW10fDI)

---

## 📬 Contact

If you have questions or suggestions, feel free to connect:

* 🔗 GitHub: [@chandangowdrus](https://github.com/chandangowdrus)

---

## ✅ To Do

* [ ] Add chatbot memory for follow-up questions
* [ ] Support multiple document uploads
* [ ] Deploy on Render/Heroku

---

## 🧠 License

MIT License © 2025 Chandan S.

```

---

Would you like this `README.md` file added to your project folder automatically, or should I help you include a screenshot preview or deployment instructions (like on Render)?
```
