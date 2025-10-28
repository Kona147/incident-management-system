#🧭 Open-Source Incident Management System
🎯 Objective

A lightweight web-based Incident Management System that allows users to log, track, assign, and resolve infrastructure or application issues. The system includes role-based access (User/Admin) and Docker containerization for deployment.

🛠️ Tech Stack

Backend: Python (Flask)

Database: SQLite

Frontend: HTML, Bootstrap, Jinja2 Templates

Containerization: Docker

Version Control: Git / GitHub

⚙️ Features

✅ Log new incidents with details (title, description, priority, status)
✅ View all open and resolved incidents
✅ Update, assign, and close incidents
✅ SQLite for simple, file-based storage
✅ REST APIs for CRUD operations
✅ Fully containerized with Docker

🧩 Project Structure
incident-management-system/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_incident.html
│   ├── update_incident.html
│
├── static/
│   └── style.css
│
└── incident.db

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/incident-management-system.git
cd incident-management-system

2️⃣ Create and Activate Virtual Environment
python3 -m venv .venv
source .venv/bin/activate    # (Linux/macOS)
# OR
.venv\Scripts\activate       # (Windows)

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py


Visit http://127.0.0.1:5000

🐳 Run with Docker
Build Docker Image
docker build -t incident-system .

Run Container
docker run -d -p 5000:5000 incident-system


Open your browser at:
👉 http://localhost:5000

💾 Sample Data

Example of test incidents:

ID	Title	Priority	Status	Assigned To
1	API not responding	High	Open	Admin
2	Database connection issue	Medium	Resolved	Karthik
🚧 Future Enhancements

Add email notifications for assignment and resolution using Gmail SMTP

Include user authentication (login/signup)

Add role-based dashboards (Admin/User)

Deploy using GitHub Actions and Docker Hub

🤝 Contributing

Contributions are welcome!

Fork the repo

Create a new branch (feature/your-feature)

Commit and push changes

Open a Pull Request


## 📜 License

This project is licensed under the **MIT License** — feel free to use and modify.

**Kona Sai Karthik**
💼 GitHub: [@Kona147](https://github.com/Kona147)
