# 🧭 Open-Source Incident Management System

## 🎯 Objective

A lightweight web-based **Incident Management System** that allows users to log, track, assign, and resolve infrastructure or application issues. The system includes role-based access (User/Admin), email notifications, and Docker containerization for deployment.

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Database:** SQLite
* **Frontend:** HTML, Bootstrap, Jinja2 Templates
* **Containerization:** Docker
* **Version Control:** Git / GitHub
* **Email Notifications:** SMTP

---

## ⚙️ Features

✅ Log new incidents with details (title, description, priority, status)
✅ View all open and resolved incidents
✅ Update, assign, and close incidents
✅ SQLite for simple, file-based storage
✅ REST APIs for CRUD operations
✅ Email alerts for assignment & resolution
✅ Fully containerized with Docker

---

## 🧩 Project Structure

```
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
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/incident-management-system.git
cd incident-management-system
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate    # (Linux/macOS)
# OR
.venv\Scripts\activate       # (Windows)
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🐳 Run with Docker

### Build Docker Image

```bash
docker build -t incident-system .
```

### Run Container

```bash
docker run -d -p 5000:5000 incident-system
```

Open your browser at:
👉 [http://localhost:5000](http://localhost:5000)

---

## 💾 Sample Data

Example of test incidents:

| ID | Title                     | Priority | Status   | Assigned To     |
| -- | ------------------------- | -------- | -------- | -----------     |
| 1  | API not responding        | High     | Open     | Admin           |
| 2  | Database connection issue | Medium   | Resolved | Sai Karthik     |


---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch (`feature/your-feature`)
3. Commit and push changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use and modify.

**Kona Sai Karthik**
💼 GitHub: [@Kona147](https://github.com/Kona147)

🌐 Live Demo: [Incident Management Portal](https://neglected-wizard-q56p7jr54r5f9pr9-5000.app.github.dev/)

🚧 Future Enhancements

Here are a few ideas planned for future releases:

🔐 User Authentication: Add secure login for Admin and Users

🧠 AI-based Incident Categorization: Auto-assign priority based on issue description

📊 Dashboard Analytics: Display metrics for open, closed, and recurring incidents

🔄 CI/CD Integration: Automate build and deployment using GitHub Actions

🌍 Multi-User Role System: Add Supervisor and Developer roles

💬 Real-Time Notifications: Enable WebSocket-based live updates

☁️ Cloud Deployment: Host on AWS / Google Cloud / Render



**Kona Sai Karthik**
💼 GitHub: [@Kona147](https://github.com/Kona147)
