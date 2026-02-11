AI-real-fake-news-detector/
│
├── app.py
├── requirements.txt
├── .env
└── README.md
⚙️ Installation Steps
1️⃣ Clone the Repository
git clone https://github.com/vaishnavidisale/Ai-real-fake-news-detector.git
cd Ai-real-fake-news-detector
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Add Your Groq API Key
Create a .env file:
GROQ_API_KEY=your_api_key_here
Get API Key from:
https://console.groq.com
4️⃣ Run the Application
streamlit run app.py

🧠 How It Works

User enters news text.
AI model analyzes the text.
Returns:
Verdict (REAL or FAKE)
Confidence Score

Explanation
Extracts keywords.
Fetches related live news articles.
Displays clickable article links.

📊 Example Output
VERDICT: REAL
CONFIDENCE: 82%
EXPLANATION:
The news content matches verified reports from trusted sources...

🔐 Important Note
Do NOT upload .env file to GitHub.
Add his in .gitignore:
.env

🎯 Project Type
Generative AI Project
NLP Project
Final Year Engineering Project
Resume Ready Project

👨‍💻 Author
Vishu
Engineering Student | AI Enthusiast 🚀

