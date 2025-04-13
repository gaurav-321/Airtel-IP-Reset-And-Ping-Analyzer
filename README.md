# Airtel IP Reset And Ping Analyzer

This project automates resetting your Airtel router IP address through its web interface, and analyzes network performance by pinging specific servers. It's useful for optimizing latency by cycling through different public IPs.

---

## ✨ Description
Automate the process of resetting your Airtel router's IP address and continuously ping specific servers to monitor network performance. This tool helps in identifying optimal IP addresses that offer the best latency, ensuring a smoother internet experience.

---

## 🚀 Features
- **Automated Login:** Logs into your router's web interface using Selenium.
- **Ping-Based Latency Checks:** Continuously pings specified servers to measure latency.
- **Optimal IP Search:** Keeps resetting until an optimal IP with low latency is found.
- **Real-Time Logging:** Tracks and logs IP, location, and ping data.

---

## 🛠️ Installation
### Prerequisites
- Python 3.x
- Google Chrome browser
- Chrome WebDriver (must be in your PATH)

### Install Dependencies
Install required Python packages by running:

```bash
pip install -r requirements.txt
```

---

## 📦 Usage
1. **Modify Settings:**
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
   - Logs into your router's web interface.
   - Continuously resets the connection using VLAN switch.
   - Pings two servers and checks for low latency.
   - Stops once an optimal IP/latency is found.

---

## 🧪 Tests
This project includes basic tests to ensure that all dependencies are installed correctly. Run the following command to execute the tests:

```bash
pytest
```

Note: Ensure you have `pytest` installed and configured properly in your environment.

---

## 📁 Project Structure
```
Airtel_IP_Reset_And_Ping_Analyzer/
├── main.py          # Main script to automate IP reset & ping.
├── requirements.txt # List of all required Python packages.
└── README.md        # Project documentation.
```

- `main.py`: Contains the logic for automating the router reset and latency check.
- `requirements.txt`: Lists all dependencies that need to be installed.
- `README.md`: This file.

---

## 🙌 Contributing
Contributions are welcome! If you have any improvements, bug fixes, or suggestions, please fork this repository and submit a pull request. Contributions should follow the guidelines provided in the [CONTRIBUTING.md](https://github.com/gag3301v/Airtel_IP_Reset_And_Ping_Analyzer/blob/master/CONTRIBUTING.md) file.

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/gag3301v/Airtel_IP_Reset_And_Ping_Analyzer/blob/master/LICENSE) file for details.

---

## 🙏 Credits
Developed for personal use with Airtel broadband routers. Contributions and pull requests are welcome if you adapt it for other ISPs or router models.