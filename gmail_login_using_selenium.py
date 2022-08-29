if __name__=='__main__':
    import undetected_chromedriver.v2 as uc
    import time
    from selenium.webdriver.common.keys import Keys

    GMAIL = '' # Enter your gmail account here.
    PASSWORD = '' # Enter your gmail password here.
    chrome_options = uc.ChromeOptions()

    chrome_options.add_argument("--disable-extensions")

    chrome_options.add_argument("--disable-popup-blocking")

    chrome_options.add_argument("--profile-directory=Default")

    chrome_options.add_argument("--disable-plugins-discovery")

    chrome_options.add_argument("--incognito")

    chrome_options.add_argument("user_agent=DN")

    driver = uc.Chrome(options=chrome_options)

    driver.delete_all_cookies()

    driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")

    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(GMAIL)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(Keys.RETURN)
    time.sleep(2)
    driver.find_element_by_name("password").send_keys(PASSWORD)
    time.sleep(2)
    driver.find_element_by_id("passwordNext").click()
    time.sleep(2)
    driver.get("https://mail.google.com/mail/u/0/#inbox")
    time.sleep(2)
