![Cloud Support Toolkit](toolsbanner.png)

# ☁️ Cloud Support Toolkit

A collection of real-world diagnostic tools built for cloud and SaaS support engineers.

Created to demonstrate technical troubleshooting skills in DNS, HTTP, SSO, and connectivity.

---

## 🔧 Tools Included

| Tool               | Description                                                   |
|--------------------|---------------------------------------------------------------|
| `dns_diag.py`      | Resolves A, MX, CNAME, and TXT DNS records for a given domain |
| `http_status.py`   | Checks HTTP/HTTPS response status and latency                 |
| `ping_check.sh`    | Pings multiple hosts and displays basic latency info          |
| `sso_metadata.py`  | Outputs sample SAML metadata XML from a mock IdP              |

---

## 📦 Requirements

- Python 3.x
- Bash (or Git Bash on Windows)
- Internet access

Install dependencies:

```bash
pip install dnspython requests
```

---

## 🚀 How to Run

```bash
# DNS Record Lookup
python tools/dns_diag.py google.com

# HTTP Status & Latency Check
python tools/http_status.py https://github.com

# Ping Multiple Hosts
./tools/ping_check.sh google.com github.com

# SSO Metadata Viewer
python tools/sso_metadata.py https://login.example-idp.com
```

---

## 📁 Project Structure

```
cloud-support-toolkit/
├── README.md
├── .gitignore
├── tools/
│   ├── dns_diag.py
│   ├── http_status.py
│   ├── ping_check.sh
│   └── sso_metadata.py
```

---

## 📌 Why This Matters

These tools represent the real work done by technical support engineers in cloud environments — quick diagnostics, scriptable tooling, and API familiarity.

---

## 🔗 Author

**Tinashe Muzungu**  
GitHub: [nashe223]  
LinkedIn: https://www.linkedin.com/in/tinashe-m-96991b57/

