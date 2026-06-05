from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("la app esta corriendo")
def step_la_app_corriendo(context):
    context.driver.get("http://127.0.0.1:5000")

@when("voy a la pagina de login")
def step_ir_login(context):
    context.driver.get("http://127.0.0.1:5000/login")

@when('ingreso "{value}" en el campo "{field}"')
def step_ingresar_campo(context, value, field):
    elem = context.driver.find_element(By.NAME, field)
    elem.clear()
    elem.send_keys(value)

@when('hago click en "{text}"')
def step_click(context, text):
    btn = context.driver.find_element(By.XPATH, f"//button[text()='{text}']")
    btn.click()

@then('veo el texto "{text}"')
def step_ver_texto(context, text):
    WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{text}')]"))
    )
    assert text in context.driver.page_source
