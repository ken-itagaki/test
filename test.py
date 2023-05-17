from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome()
driver.set_page_load_timeout(1)

count =0

def input(path,key):
    input_element = driver.find_element(By.XPATH,path)
    input_text = input_element.get_attribute("value")
    if input_text != key:
        print(input_text,"is wrong")
        driver.find_element(By.XPATH,path).clear()
        driver.find_element(By.XPATH,path).send_keys(key)
        global count
        count = 1

def dropdown(path,key):
    dropdown_element = driver.find_element(By.XPATH,path)
    dropdown = Select(dropdown_element)
    selected_option = dropdown.first_selected_option
    selected_text = selected_option.text
    if selected_text != key:
        print(selected_text,"is wrong")
        dropdown.select_by_visible_text(key)
        global count
        count = 1

def radio(path,key):
    radio_element = driver.find_element(By.XPATH,path)
    if not radio_element.is_selected():
        driver.find_element(By.TAG_NAME,"body").send_keys(Keys.END)
        print(key,"is wrong")
        time.sleep(2)
        radio_element.click()
        global count
        count =1
        time.sleep(3)
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass

def button(path):
    driver.find_element(By.TAG_NAME,"body").send_keys(Keys.END)
    time.sleep(2)
    button = driver.find_element(By.XPATH,path)
    button.click()
    time.sleep(2)
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except:
        pass
    print("save")
    time.sleep(3)

try:
    driver.get('http://192.168.110.201/setting.html')
    time.sleep(1)
    radio('//*[@id="setting-sandby-off"]',"In Operation")
    input('//*[@id="ip-address"]',"192.168.110.201")
    input('//*[@id="ip-mask"]',"255.255.255.0")
    input('//*[@id="ip-gateway"]',"192.168.110.1")
    input('//*[@id="destination-ip"]',"255.255.255.255")
    input('//*[@id="destination-lidar-port"]',"2321")
    dropdown('//*[@id="setting-spin-rate"]',"600")
    dropdown('//*[@id="setting-lidar-mode"]',"Dual Return")
    dropdown('//*[@id="setting-udp-sequence"]',"OFF")
    input('//*[@id="sync-angle"]',"180")
    dropdown('//*[@id="setting-trigger-method"]',"Angle Based")
    dropdown('//*[@id="setting-clock-source"]',"PTP")
    dropdown('//*[@id="ptp_profile"]',"1588v2")
    dropdown('//*[@id="ptp-network-transport"]',"UDP/IP")
    input('//*[@id="ptp-domain-number"]',"0")
    input('//*[@id="ptp-loginte-number"]',"1")
    input('//*[@id="ptp-logsinte-number"]',"1")
    input('//*[@id="ptp-logmdinte-number"]',"0")
    dropdown('//*[@id="NoiseFilter"]',"ON")
    dropdown('//*[@id="ReflectivityMapping"]',"Linear Mapping")

    if count == 1:
        button('//*[@id="save"]/button')

    driver.get('http://192.168.110.201/config_angle.html')
    count = 0
    time.sleep(1)
    dropdown('//*[@id="setting-lidar-range-method"]',"For all channels")
    input('//*[@id="start-angle"]',"90.0")
    input('//*[@id="end-angle"]',"270.0")

    if count == 1:
            button('//*[@id="save"]/button')
    
    try:
        driver.get('http://192.168.110.201/special_setting.html')
        time.sleep(1)
        element = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="security-code"]')))
        driver.find_element(By.XPATH,'//*[@id="security-code"]').send_keys("921223")
        element = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="save_code_range"]')))
        button = driver.find_element(By.XPATH,'//*[@id="save_code_range"]')
        button.click()
        time.sleep(1)
        try:
            alert = driver.switch_to.alert
            alert.accept() 
        except:
            pass
    except:
        pass

    time.sleep(1)
    input('//*[@id="code-range-low"]',"205")
    input('//*[@id="code-range-high"]',"205")

    if count == 1:
        button('//*[@id="save_code_range"]')
    print("OK")

except TimeoutException:
    try:
        driver.get('http://192.168.110.202/setting.html')
        time.sleep(1)
        radio('//*[@id="setting-sandby-off"]',"In Operation")
        input('//*[@id="ip-address"]',"192.168.110.202")
        input('//*[@id="ip-mask"]',"255.255.255.0")
        input('//*[@id="ip-gateway"]',"192.168.110.1")
        input('//*[@id="destination-ip"]',"255.255.255.255")
        input('//*[@id="destination-lidar-port"]',"2322")
        dropdown('//*[@id="setting-spin-rate"]',"600")
        dropdown('//*[@id="setting-lidar-mode"]',"Dual Return")
        dropdown('//*[@id="setting-udp-sequence"]',"OFF")
        input('//*[@id="sync-angle"]',"270")
        dropdown('//*[@id="setting-trigger-method"]',"Angle Based")
        dropdown('//*[@id="setting-clock-source"]',"PTP")
        dropdown('//*[@id="ptp_profile"]',"1588v2")
        dropdown('//*[@id="ptp-network-transport"]',"UDP/IP")
        input('//*[@id="ptp-domain-number"]',"0")
        input('//*[@id="ptp-loginte-number"]',"1")
        input('//*[@id="ptp-logsinte-number"]',"1")
        input('//*[@id="ptp-logmdinte-number"]',"0")
        dropdown('//*[@id="NoiseFilter"]',"ON")
        dropdown('//*[@id="ReflectivityMapping"]',"Linear Mapping")

        if count == 1:
            button('//*[@id="save"]/button')

        driver.get('http://192.168.110.202/config_angle.html')
        count = 0
        time.sleep(1)
        dropdown('//*[@id="setting-lidar-range-method"]',"For all channels")
        input('//*[@id="start-angle"]',"90.0")
        input('//*[@id="end-angle"]',"357.0")

        if count == 1:
            button('//*[@id="save"]/button')
        
        try:
            driver.get('http://192.168.110.202/special_setting.html')
            time.sleep(1)
            element = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="security-code"]')))
            driver.find_element(By.XPATH,'//*[@id="security-code"]').send_keys("921223")
            element = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="save_code_range"]')))
            button = driver.find_element(By.XPATH,'//*[@id="save_code_range"]')
            button.click()
            time.sleep(1)
            try:
                alert = driver.switch_to.alert
                alert.accept() 
            except:
                pass
        except:
            pass

        time.sleep(1)
        input('//*[@id="code-range-low"]',"210")
        input('//*[@id="code-range-high"]',"210")

        if count == 1:
            button('//*[@id="save_code_range"]')
        print("OK")

    except TimeoutException:
        try:
            driver.get('http://192.168.110.204/setting.html')
            time.sleep(1)
            radio('//*[@id="setting-sandby-off"]',"In Operation")
            input('//*[@id="ip-address"]',"192.168.110.204")
            input('//*[@id="ip-mask"]',"255.255.255.0")
            input('//*[@id="ip-gateway"]',"192.168.110.1")
            input('//*[@id="destination-ip"]',"255.255.255.255")
            input('//*[@id="destination-lidar-port"]',"2324")
            dropdown('//*[@id="setting-spin-rate"]',"600")
            dropdown('//*[@id="setting-lidar-mode"]',"Dual Return")
            dropdown('//*[@id="setting-udp-sequence"]',"OFF")
            input('//*[@id="sync-angle"]',"0")
            dropdown('//*[@id="setting-trigger-method"]',"Angle Based")
            dropdown('//*[@id="setting-clock-source"]',"PTP")
            dropdown('//*[@id="ptp_profile"]',"1588v2")
            dropdown('//*[@id="ptp-network-transport"]',"UDP/IP")
            input('//*[@id="ptp-domain-number"]',"0")
            input('//*[@id="ptp-loginte-number"]',"1")
            input('//*[@id="ptp-logsinte-number"]',"1")
            input('//*[@id="ptp-logmdinte-number"]',"0")
            dropdown('//*[@id="NoiseFilter"]',"ON")
            dropdown('//*[@id="ReflectivityMapping"]',"Linear Mapping")

            if count == 1:
                button('//*[@id="save"]/button')

            driver.get('http://192.168.110.204/config_angle.html')
            count = 0
            time.sleep(1)
            dropdown('//*[@id="setting-lidar-range-method"]',"For all channels")
            input('//*[@id="start-angle"]',"90.0")
            input('//*[@id="end-angle"]',"270.0")

            if count == 1:
                button('//*[@id="save"]/button')
            
            try:
                driver.get('http://192.168.110.204/special_setting.html')
                time.sleep(1)
                element = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="security-code"]')))
                driver.find_element(By.XPATH,'//*[@id="security-code"]').send_keys("921223")
                element = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="save_code_range"]')))
                button = driver.find_element(By.XPATH,'//*[@id="save_code_range"]')
                button.click()
                time.sleep(1)
                try:
                    alert = driver.switch_to.alert
                    alert.accept() 
                except:
                    pass
            except:
                pass

            time.sleep(1)
            input('//*[@id="code-range-low"]',"220")
            input('//*[@id="code-range-high"]',"220")

            if count == 1:
                button('//*[@id="save_code_range"]')
            print("OK")
        except TimeoutException:
            try:
                driver.get('http://192.168.120.203/setting.html')
                time.sleep(1)
                radio('//*[@id="setting-sandby-off"]',"In Operation")
                input('//*[@id="ip-address"]',"192.168.120.203")
                input('//*[@id="ip-mask"]',"255.255.255.0")
                input('//*[@id="ip-gateway"]',"192.168.120.1")
                input('//*[@id="destination-ip"]',"255.255.255.255")
                input('//*[@id="destination-lidar-port"]',"2323")
                dropdown('//*[@id="setting-spin-rate"]',"600")
                dropdown('//*[@id="setting-lidar-mode"]',"Dual Return")
                dropdown('//*[@id="setting-udp-sequence"]',"OFF")
                input('//*[@id="sync-angle"]',"270")
                dropdown('//*[@id="setting-trigger-method"]',"Angle Based")
                dropdown('//*[@id="setting-clock-source"]',"PTP")
                dropdown('//*[@id="ptp_profile"]',"1588v2")
                dropdown('//*[@id="ptp-network-transport"]',"UDP/IP")
                input('//*[@id="ptp-domain-number"]',"0")
                input('//*[@id="ptp-loginte-number"]',"1")
                input('//*[@id="ptp-logsinte-number"]',"1")
                input('//*[@id="ptp-logmdinte-number"]',"0")
                dropdown('//*[@id="NoiseFilter"]',"ON")
                dropdown('//*[@id="ReflectivityMapping"]',"Linear Mapping")

                if count == 1:
                    button('//*[@id="save"]/button')

                driver.get('http://192.168.120.203/config_angle.html')
                count = 0
                time.sleep(1)
                dropdown('//*[@id="setting-lidar-range-method"]',"For all channels")
                input('//*[@id="start-angle"]',"3.0")
                input('//*[@id="end-angle"]',"270.0")

                if count == 1:
                    button('//*[@id="save"]/button')
                
                try:
                    driver.get('http://192.168.110.202/special_setting.html')
                    time.sleep(1)
                    element = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="security-code"]')))
                    driver.find_element(By.XPATH,'//*[@id="security-code"]').send_keys("921223")
                    element = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="save_code_range"]')))
                    button = driver.find_element(By.XPATH,'//*[@id="save_code_range"]')
                    button.click()
                    time.sleep(1)
                    try:
                        alert = driver.switch_to.alert
                        alert.accept() 
                    except:
                        pass
                except:
                    pass

                time.sleep(1)
                input('//*[@id="code-range-low"]',"215")
                input('//*[@id="code-range-high"]',"215")

                if count == 1:
                    button('//*[@id="save_code_range"]')
                print("OK")
            except TimeoutException:
                print("アクセスできませんでした")
finally:
    driver.quit()


