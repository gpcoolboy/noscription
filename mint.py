from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time,sys,subprocess
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# 用户浏览器目录
chromeUserDir = sys.argv[1] if len(sys.argv)>1 and sys.argv[1] != None else "D:/workspaces/noscription/ChromeConfig"
# 测试标识
testFlag = sys.argv[2] if len(sys.argv)>2 and sys.argv[2] != None else ""

def initChrome():
    EXEC_DIR_PATH = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    USER_DIR_PATH = chromeUserDir
    command = [EXEC_DIR_PATH, '--remote-debugging-port=12800', '--remote-allow-origins=*', '--user-data-dir='+USER_DIR_PATH]
    subprocess.Popen(command, shell=True)
    time.sleep(1)
    # 定义浏览器设置
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("start-maximized")
    # chrome_options.add_argument('--profile-directory=Default')
    # chrome_options.add_argument('--user-data-dir=' + USER_DIR_PATH)
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:12800")
    # 不加载图片
    #chrome_options.add_argument('blink-settings=imagesEnabled=false')
    # 禁用GPU加速
    chrome_options.add_argument('--disable-gpu')
    # 加载浏览器设置
    driver = webdriver.Chrome(options=chrome_options,service=ChromeService(ChromeDriverManager().install()))
    # 设置窗口大小
    driver.set_window_size(1200, 1000)
    driver.get("https://noscription.org/")
    time.sleep(2)
    return driver


def main():
    driver = initChrome()
    if testFlag != "test":
        while True:
            try:
                handles = driver.window_handles
                if len(handles)>1:
                    driver.switch_to.window(handles[-1])
                    driver.find_element(By.XPATH,"//input[@class='okui-input-input']").send_keys("123456789")
                    driver.find_element(By.XPATH,"//button[@type='submit']").click()
                    break
            except:
                pass
            time.sleep(1)
        driver.switch_to.window(handles[0])
        driver.find_element(By.XPATH,"//button[@id=':r4:']").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH,"//input[@class='PrivateSwitchBase-input css-1m9pwf3']").click()
        time.sleep(3)
        while True:
            try:
                driver.find_element(By.XPATH,"//button[@id=':rc:']").click()
                print("按下启动按钮")
                break
            except:
                pass
            time.sleep(1)
        while True:
            try:
                handles = driver.window_handles
                if len(handles)>1:
                    driver.switch_to.window(handles[-1])
                    driver.find_element(By.XPATH,"//button[@class='okui-btn btn-lg btn-fill-highlight mobile _action-button_1ntoe_1']").click()
                    time.sleep(1)
            except:
                pass
            time.sleep(1)
    else:
        print("进入调试模式")
if __name__ == '__main__':
    main()