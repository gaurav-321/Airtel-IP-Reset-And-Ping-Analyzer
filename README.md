# Airtel IP Reset And Ping Analyzer

This project automates resetting your Airtel router IP address through its web interface, and analyzes network performance by pinging specific servers. It's useful for optimizing latency by cycling through different public IPs.

---

## 📦 Features
- Automated login and IP reset for routers via Selenium.
- Ping-based latency checks to specific servers.
- Continues resetting until optimal latency is achieved.
- Logs IP, location, and ping data in real-time.

---

## ⚙️ Requirements
- Python 3.x
- Google Chrome browser
- Chrome WebDriver (must be in your PATH)

### Python Packages
Install required dependencies:

```bash
pip install -r requriements.txt
```

---

## 🚀 Usage
1. **Modify Settings in `main.py`:**
   Update the following lines in `main.py` to match your router's IP and credentials:

```python
browser.get("http://192.168.1.1")
browser.find_element(By.ID, "Frm_Username").send_keys("admin")
browser.find_element(By.ID, "Frm_Password").send_keys("admin")
server1, ping_1 = "63.251.126.126", 80
server2, ping_2 = '3.6.0.0', 35
```

2. **Run the Script:**

```bash
python main.py
```

3. **What It Does:**
   - Logs into the router's web UI.
   - Continuously resets the connection using VLAN switch.
   - Pings two servers and checks for low latency.
   - Stops once a desirable IP/latency is found.

---

## 📄 Example Output
```
103.5.130.45    Maharashtra    Mumbai    (20.2, 31.1)
Found Most Relevant IP
```

---

## 🔧 Troubleshooting
- This script is tailored to a specific router model and interface. You may need to inspect your router's HTML and adjust element IDs.
- Make sure Chrome WebDriver matches your Chrome browser version.
- Add WebDriver to your system PATH or provide full path.

---

## 📁 Files
| File               | Description                              |
|--------------------|------------------------------------------|
| `main.py`          | Main script to automate IP reset & ping. |
| `requriements.txt` | List of all required Python packages.    |
| `README.md`        | Project documentation.                   |

---

## 📜 License
MIT License (or add your own).

---

## 🙏 Credits
Developed for personal use with Airtel broadband routers. Contributions and pull requests are welcome if you adapt it for other ISPs or router models.
