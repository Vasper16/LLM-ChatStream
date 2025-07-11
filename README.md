# 🤖 LLM ChatStream

LLM ChatStream is an advanced AI chatbot powered by **Gemini 1.5 Flash** from Google Generative AI. Built with Streamlit, it provides a clean, responsive UI with theme switching, chat history, quick prompts, and PDF export — all designed for productivity, education, and real-world LLM applications.

---

## 📌 Table of Contents

- [✨ Features](#-features)
- [🚧 Upcoming Features](#-upcoming-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📦 Installation](#-installation)
- [📁 Project Structure](#-project-structure)
- [🖼️ Screenshots](#-screenshots)
- [🙌 Acknowledgements](#-acknowledgements)
- [📝 License](#-license)

---

## ✨ Features

- ✅ **Google Gemini 1.5 Flash** Integration (Generative AI API)
- ✅ **Modern Chat UI** with Streamlit
- ✅ **Theme Toggle**: Light and Dark mode
- ✅ **Chat Memory**: Retains context within session
- ✅ **Quick Prompt Buttons** for FAQs or testing
- ✅ **PDF Export** of entire chat history
- ✅ **Reset Chat Button** for clean start
- ✅ **Timestamps** displayed with each message

---

## 🚧 Upcoming Features

- 🎙️ **Voice Input (Web Speech API)**
- 💾 **Persistent Chat History (Session Save/Load)**
- 🎨 **Custom Theme Builder (More than 2 color modes)**
- 📊 **Chat Analytics Dashboard**
- 🧠 **Prompt Presets (Templates for LLM usage)**

---

## 🛠️ Tech Stack

| Layer     | Tools Used                        |
|-----------|-----------------------------------|
| Frontend  | Streamlit                         |
| Backend   | Google Generative AI (Gemini 1.5) |
| Styling   | Custom CSS                        |
| PDF Export| FPDF (Python)                     |
| Config    | python-dotenv                     |

---

## 📦 Installation

> ⚠️ Requires **Python 3.8+**

### 1. Clone the Repository

```bash
git clone https://github.com/Vasper16/LLM-ChatStream.git
cd LLM-ChatStream

2. Install Dependencies
pip install -r requirements.txt

3. Setup API Key
Create a .env file in the root directory and add your Gemini API key:
GOOGLE_API_KEY=your_google_api_key_here

4. Run the Application
streamlit run main.py

📁 Project Structure
LLM-ChatStream/
├── main.py              # Main application logic
├── utils.py             # PDF export utility
├── style.css            # UI styling
├── theme.css (optional) # Legacy theme logic (currently unused)
├── requirements.txt     # Python dependencies
├── .env                 # API key (not committed)
└── README.md            # Project documentation

🙌 Acknowledgements

Google Generative AI
Streamlit
FPDF Library
OpenAI & community designs for layout inspiration

📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

💡 Maintained by @Vasper16. Feel free to star ⭐ the repo if you found this useful!

---

Let me know if you’d like:

- A markdown file export (`README.md`)
- Help generating screenshots or GIF previews
- Contributor/credits section
- Deployment instructions (e.g., Streamlit Cloud, Heroku)

Would you like me to help push this to your GitHub repo now?
