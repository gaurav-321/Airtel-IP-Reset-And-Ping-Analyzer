# Airtel IP Reset And Ping Analyzer
This script allows the user to reset their internet connection by resetting the IP address of the router through its web interface.

## Requirements
- python 3.x
- requests
- selenium
- pythonping
- Chrome browser
- Chrome webdriver
## Installation
Install the required packages:

Copy code
```
pip install requests selenium pythonping
```
## Usage
To use this script, modify the following lines to match your router's IP address, login credentials and ping servers:

```
browser.get("http://192.168.1.1")
browser.find_element(By.ID, "Frm_Username").send_keys("admin")
browser.find_element(By.ID, "Frm_Password").send_keys("admin")
server1, ping_1 = "63.251.126.126", 80
server2, ping_2 = '3.6.0.0', 35
```
Then, run the script:

```
python reset_ip.py
```
The script will continuously reset the IP address of the router until a desirable IP is obtained (as determined by the latency of pings to the specified servers). The resulting IP, region, city and ping latencies will be printed to the console.

## Notes
- This script was tested on a specific router with specific web interface elements. Modifications may be needed for different router models or interfaces.
- The Chrome webdriver must be installed and added to the PATH for the script to work.
- The script may need to be modified to work with other browsers besides Chrome.
