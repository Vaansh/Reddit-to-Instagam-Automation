import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import applescript_filepicker
import time

options = Options()
options.add_argument('')    #User agent to be used; Example: user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/85.0.4183.72 Mobile/15E148 Safari/604.1
driver = webdriver.Chrome(chrome_options=options, executable_path='')   #Example: /usr/local/bin/chromedriver

def logintoig(username, password):    
    #Link to login
    igurl = 'https://www.instagram.com/?hl=en'

    #process of login
    driver.get(igurl)
    time.sleep(5)    
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[2]/button').click()
    time.sleep(5)
    
    usr = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/div/label/input')
    usr.click()
    usr.send_keys(username)

    pwd = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[4]/div/label/input')
    pwd.click()
    pwd.send_keys(password)

    driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[6]/button/div').click()
    time.sleep(15)
    currenturl = driver.current_url    

    #Bypass suspicious login attempt; Code is recieved through email
    try:
        if "challenge" in currenturl:
            driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/div[3]/form/span/button').click()
            code = input('Enter the security code recieved:')
            driver.find_element_by_xpath('//*[@id="security_code"]').click()
            driver.find_element_by_xpath('//*[@id="security_code"]').send_keys(code)
            driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/div[2]/form/span/button').click()        
            time.sleep(15)            
    except:
        pass           

    time.sleep(3)
    
    #Close pop-ups by instagram, if any
    try:
        if driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/button'):
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/button').click()
            time.sleep(5)              
    except:
        pass
    
    time.sleep(3)

    try:
        if driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]'):
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
            time.sleep(5)                                
    except:
        pass

    time.sleep(3)

    #If wrong security code is entered, brought back to login again
    currenturl = driver.current_url    
    if(currenturl==igurl):
        logintoig(username, password)
    else:
        pass  

def uploadtoig(fullPath, caption,post):                                     
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]').click()
    time.sleep(1)

    #Choose file using applescript
    time.sleep(1)    
    applescript_filepicker.chooseFile(fullPath)    
    time.sleep(3)
    
    driver.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]/button').click()
    time.sleep(3)

    #Enter the caption, no emojis can be included
    textarea = driver.find_element_by_css_selector('#react-root > section > div.A9bvI > section.IpSxo > div.NfvXc > textarea')
    textarea.click()
    time.sleep(1)
    textarea.clear()
    time.sleep(1)
    textarea.send_keys(caption)

    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]/button').click()
    time.sleep(5)

    #Close pop-ups after posting, if any
    try:
        if driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]'):
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
            time.sleep(5)  
    except:
        pass

    time.sleep(5)
    
    try:
        if driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/button'):
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/button').click()
            time.sleep(5)
    except:
        pass        

    #Sleep for desired time
    time.sleep(post)