# Gmail-login-using-selenium

This is a simple way to automate your gmail sign in using selenium. The normal selenium webdriver fails while implementing the gmail sign in (You can still sign in using normal selenium webdriver if you have a g-suite domain mail). So I used the undetected-chromedriver for this process. It can be found in <a href="https://github.com/ultrafunkamsterdam/undetected-chromedriver" target="blank">this</a> github repo. If you install the undetectable chromedriver, you need not download and install your browser executable like you do with the selenium webdriver.The version 2 of this webdriver finds the browser executable automatically. However, this webdriver doesn't work in the headless mode. But as the developer of this chromedriver says, it is still work in progress so you can expect it to support headless mode in future versions.

## Installations ##
You need to install two modules for running your gmail automation. They are selenium and undetectable_chromedriver.<br><br>
Install selenium by copying this and pasting in your command prompt or terminal<br>
```
pip install selenium
```
<br>
Install undetected chromedriver by copying this and pasting in your command prompt or terminal<br>

```
pip install undetected-chromedriver
```
<br>
