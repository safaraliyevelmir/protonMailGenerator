import time

from selenium.webdriver.common.by import By
import pyautogui

from utlis import randomize, max_tries, get_driver




class ProtonRegistration:

    def __init__(self) -> None:
        self.driver = get_driver()
        self.driver.get("https://mail.protonmail.com/create/new?language=en")


    def generateUserInformation(self) -> tuple[str, str]:
        """Generate random username and password"""
        username = randomize('-s',5)+randomize('-s',5)+randomize('-s',5)
        password = randomize('-p',16)
        return username, password
    
    @max_tries(3)
    def select_free_account(self) -> None:
        # Select free account
        freeAccount = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/main/div/div[1]/div[2]/div[3]/button')
        if freeAccount:
            freeAccount.click()

        # Select email for verification
        verifyType = self.driver.find_element(By.XPATH, '//*[@id="label_1"]')   
        if verifyType: 
            verifyType.click()

    def registrationFirstStep(self, username: str, password: str) -> None:
        # I fill username and password
        #TODO: use selenium to fill username (pyautogui is not reliable). but selenium can't handle to fill username
        pyautogui.keyUp('tab'); pyautogui.keyDown('tab'); time.sleep(2); pyautogui.typewrite(username)
        time.sleep(len(username) * 0.1)

        passwordInput = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        passwordConfirmInput = self.driver.find_element(By.XPATH, '//*[@id="repeat-password"]')
        submitButton = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/main/div[1]/div[2]/form/button')

        passwordInput.send_keys(password)
        passwordConfirmInput.send_keys(password)
        submitButton.click()

        self.select_free_account()
        
    def sendVerificationCode(self, verificationCode: int) -> None:
        verificationCodeInput = self.driver.find_element(By.XPATH, '//*[@id="verification"]')
        verificationCodeSubmit = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/main/div/div[2]/button[1]')
        verificationCodeInput.send_keys(verificationCode)
        verificationCodeSubmit.click()
        
    def displayName(self, displayName: str = randomize('-l', 9)):
        """Set display name if you don't want to use random display name"""
        displayNameInput = self.driver.find_element(By.XPATH, '//*[@id="displayName"]')
        submit = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/main/div/div[2]/form/button')
        if displayNameInput:
            displayNameInput.send_keys(displayName)
            submit.click()

    def recoveryMethodSkip(self) -> None:
        """Skip recovery method"""
        skipButton = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/main/div/div[2]/form/button[2]')
        skipButton.click()
        warningConfirm = self.driver.find_element(By.XPATH, '/html/body/div[4]/dialog/div/div[3]/div/button[1]')
        if warningConfirm:
            warningConfirm.click()


    def emailVerify(self, email: str) -> None:
        emailInput = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/main/div/div[2]/div/div[2]/div[2]/div[1]/div/div/input')
        emailVerifyButton = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/main/div/div[2]/div/div[2]/button')
        emailInput.send_keys(email)
        if emailVerifyButton:
            emailVerifyButton.click()    

    
