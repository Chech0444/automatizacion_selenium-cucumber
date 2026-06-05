import os

BROWSER = os.getenv("BROWSER", "firefox").lower()

def before_scenario(context, scenario):
    if BROWSER == "chrome":
        from selenium.webdriver.chrome.options import Options
        from selenium import webdriver
        opts = Options()
        opts.add_argument("--headless")
        opts.add_argument("--no-sandbox")
        chrome_bin = os.getenv("CHROME_BINARY")
        if chrome_bin:
            opts.binary_location = chrome_bin
        context.driver = webdriver.Chrome(options=opts)
    else:
        from selenium.webdriver.firefox.options import Options
        from selenium import webdriver
        opts = Options()
        opts.add_argument("--headless")
        context.driver = webdriver.Firefox(options=opts)

    context.driver.implicitly_wait(5)

def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
