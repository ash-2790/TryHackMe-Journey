🚀 TryHackMe GitHub Automation (Python)

Automate tracking of TryHackMe room completions and keep your GitHub profile updated automatically using Python.

This project helps cybersecurity learners maintain a public, verifiable learning log without violating TryHackMe’s terms of service.

📌 Problem Statement

Cybersecurity learners often complete labs on platforms like TryHackMe, but:

Progress is scattered

GitHub profiles look inactive

No structured record of learning exists

Recruiters prefer visible, consistent, hands-on work.

✅ Solution

This project:

Tracks completed TryHackMe rooms locally

Automatically updates a GitHub README

Maintains structured progress data

Creates meaningful GitHub activity

All done ethically without scraping or using private APIs.

🛠️ Tech Stack

Python 3

Git & GitHub

JSON (data storage)

Markdown (README generation)

📂 Project Structure
tryhackme-github-automation/
│
├── data/
│   └── completed_rooms.json
│
├── scripts/
│   ├── add_room.py
│   └── update_readme.py
│
├── README.md
├── requirements.txt
└── .gitignore

⚙️ How It Works
You complete a TryHackMe room
        ↓
Run Python script
        ↓
Room added to JSON
        ↓
README.md updated
        ↓
GitHub commit & push

🧪 Usage Guide
1️⃣ Clone the Repository
git clone https://github.com/ash-2790/tryhackme-github-automation.git
cd tryhackme-github-automation

2️⃣ Add a Completed Room
python scripts/add_room.py


You will be prompted for:

Room name

Difficulty level

3️⃣ Update README Automatically
python scripts/update_readme.py

4️⃣ Push Changes to GitHub
git add .
git commit -m "Updated TryHackMe progress"
git push


Your GitHub now reflects your learning progress 📈

📊 Sample Output (README Section)
## Completed Rooms
- Intro to Networking (Easy) – 2026-01-18
- Linux Fundamentals (Easy) – 2026-01-20

🔐 Ethics & Compliance

❌ No scraping

❌ No unauthorized API usage

❌ No automation of TryHackMe actions

✅ Manual confirmation only

✅ Fully compliant with TryHackMe ToS

🎯 Use Cases

Cybersecurity internship applications

SOC analyst portfolio

GitHub profile enhancement

Learning accountability

🌱 Future Enhancements

GitHub Actions automation

CSV export of progress

Difficulty-wise analytics

Integration with Hack The Box

CLI-based dashboard

👤 Author

Ashish Kumar
B.Tech CSE | Cybersecurity & Network Security
GitHub: https://github.com/ash-2790

⭐ Final Note

“Consistency matters more than certificates.”

If you find this project useful, consider giving it a ⭐ and building upon it.
