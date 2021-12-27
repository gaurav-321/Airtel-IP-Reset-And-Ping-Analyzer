import time
import requests
from selenium import webdriver as uc
from pythonping import ping
from selenium.webdriver.common.by import By

options = uc.ChromeOptions()
options.headless = True
browser = uc.Chrome(options=options)

server1, ping_1 = "63.251.126.126", 80  # Server to ping and expected latency
server2, ping_2 = '3.6.0.0', 35  # Server to ping and expected latency


def get_ping():
    ping_result = ping(target=server1, count=30, timeout=2)
    ping_result_2 = ping(target=server2, count=30, timeout=2)
    return ping_result.rtt_min_ms, ping_result_2.rtt_min_ms


def get_my_current_info():
    while True:
        try:
            ip_data = requests.get("https://ipinfo.io/json").json()
            ping_ms = get_ping()
            print("    ".join([ip_data['ip'], ip_data['region'], ip_data['city'], f"{ping_ms}"]))
            return ping_ms
        except Exception as e:
            time.sleep(1)


def login():
    browser.get("http://192.168.1.1")
    browser.find_element(By.ID, "Frm_Username").send_keys("admin")
    browser.find_element(By.ID, "Frm_Password").send_keys("admin")
    browser.find_element(By.ID, "LoginId").click()
    browser.find_element(By.ID, "internet").click()
    browser.find_element(By.ID, "internetConfig").click()
    browser.find_element(By.ID, "instName_Internet:1").click()


def reset_net():
    while True:
        ping_ms = get_my_current_info()
        if float(ping_ms[0]) < ping_1 and float(ping_ms[1] < ping_2):
            print("Found Most Revelant ip")
            break
        browser.find_element(By.ID, "VLANID:1").clear()
        browser.find_element(By.ID, "VLANID:1").send_keys("101")
        browser.find_element(By.ID, "Btn_apply_internet:1").click()
        time.sleep(2)
        browser.find_element(By.ID, "VLANID:1").clear()
        browser.find_element(By.ID, "VLANID:1").send_keys("100")
        browser.find_element(By.ID, "Btn_apply_internet:1").click()


def main():
    browser.implicitly_wait(10)
    login()
    reset_net()
    time.sleep(3)


main()
