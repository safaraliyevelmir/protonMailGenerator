import re
import random

from selenium.webdriver.common.by import By

from utlis import max_tries, get_driver



class DropMailMe:

    def __init__(self):
        self.driver = get_driver(headless=True)
        self.driver.get("https://dropmail.me/en/")
    
    def checkEmail(self, email):
        if "@dropmail.me" in str(email)  or "@10mail.org"  in str(email)  or "@emlpro.com" in str(email) or "@emltmp.com" in str(email): # 
            match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', str(email))
            return str(match.group(0))
        raise Exception("Email not correct")

    @max_tries(3)
    def getMailAddress(self) -> str:
        self.driver.find_element(By.XPATH, '//*[@id="app-banner-above"]/div[4]/div[1]/button[2]').click()
        self.driver.find_element(By.XPATH, f'//*[@id="dropdown"]/a[{random.randint(2,7)}]').click()
        self.driver.get(self.driver.current_url)
        mail_address = self.driver.find_element(By.XPATH, '//*[@id="app-banner-above"]/div[3]/div/div/div/span[1]').text

        if self.checkEmail(mail_address):
            return mail_address   
        raise Exception("Email not found") 

    @max_tries(5)
    def getVerificationCode(self):
        verifyEmail =  self.driver.find_element(By.XPATH, '/html/body/div[2]/div[9]/div[2]/ul/li/div[3]/div[1]/pre')
        if verifyEmail: 
            return self.proccessVerificationCode(verifyEmail)
        raise Exception("Verification code not found")


    def proccessVerificationCode(self, verifyEmail: str) -> int:
        verifyCode = re.search(r'\d+', verifyEmail.text)
        self.driver.quit()
        return int(verifyCode.group(0))
    
