from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def before_scenario(context, scenario):
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    context.driver = webdriver.Firefox(options=opts)
    context.driver.implicitly_wait(5)

def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
