# 🛡️ OWASP Attack Playground

A beginner-friendly Python CLI project that simulates **three OWASP Top 10 vulnerabilities**. This project helps you understand and demonstrate real-world attack scenarios in a controlled and educational environment.

---

### 🔥 What This Project Covers

This playground simulates:

| OWASP Risk | Attack Type                              | File                |
|------------|-------------------------------------------|---------------------|
| A01        | Broken Access Control                     | `broken_access.py`  |
| A03        | Injection (SQLi)                          | `sql_injection.py`  |
| A07        | Identification & Authentication Failures | `weak_auth.py`      |

All wrapped inside a terminal-based CLI using `main.py`.

---

### 📂 Project Structure

```
owasp-attack-playground/
├── main.py               # Main menu-driven CLI app
├── sql_injection.py      # SQL Injection simulation
├── broken_access.py      # Access control bypass simulation
├── weak_auth.py          # Weak password checker
├── utils.py              # Common input/output helpers
└── README.md             # You're reading it!
```

---

### 🧪 How to Run

1. Clone the repo:
```bash
git clone https://github.com/YOUR_USERNAME/owasp-attack-playground.git
cd owasp-attack-playground
```

2. Run the app:
```bash
python main.py
```

---

### 💻 Demo Examples

#### 🩸 SQL Injection (A03)
```plaintext
Username: ' OR '1'='1
Password: anything
➡️ Bypasses authentication!
```

#### 🚪 Broken Access Control (A01)
```plaintext
Username: user
File: secret_admin_file.txt
➡️ Access Denied! But still displays sensitive data!
```

#### 🔑 Weak Authentication (A07)
```plaintext
Password: 123456
➡️ ❌ Weak password: Too common or short
```

---

### 🎯 Why This Project?

This project helps you:
- Understand common OWASP risks
- Simulate attacks in a CLI environment
- Practice secure coding and vulnerability analysis
- Enhance your portfolio as a Red Team Analyst

---

### 🚀 Coming Soon

- [ ] Flask-based Web UI
- [ ] AI report generation for each attack
- [ ] Exportable `.txt` or `.json` reports

---

### 🤝 Credits

Built with ❤️ by **Surya Ravi**  
Guided by AI (ChatGPT)  
Educational purpose only – do not use these techniques on live systems.

---

### 🛑 Disclaimer

> This tool is for **educational use only**. Do **not** use it to target real websites or services without permission.
