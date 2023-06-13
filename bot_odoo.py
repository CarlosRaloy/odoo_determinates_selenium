# Selenium librerias
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementNotInteractableException
import os
import time

def page_web():
    # Este es el webdriver definido
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Link de la la ficha del resp partner
    id_res_partner = 117585
    driver.get(f"http://odoo.raloy.com.mx:8069/web#id={id_res_partner}&view_type=form&model=res.partner&action=55&menu_id=112e")

    # Agregar datos de login
    user = driver.find_element("xpath",'//*[@id="login"]')
    user.send_keys("cgarcia@raloy.com.mx")
    user.send_keys(Keys.ENTER)

    password = driver.find_element("xpath",'//*[@id="password"]')
    password.send_keys("gr101320")
    password.send_keys(Keys.ENTER)

    # Editar la ficha de la determinante
    # Button dynamic Odoo
    wait = WebDriverWait(driver, 10)
    button_editar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@accesskey='a']")))
    button_editar.click()

    # Llenar los campos de la ficha del res partner
    wait = WebDriverWait(driver, 5)
    zip_code = driver.find_element(By.CSS_SELECTOR, "div.o_form_field_many2one.o_address_zip.o_form_field input.o_form_input.ui-autocomplete-input")
    zip_code.send_keys("00000")

    """
    time.sleep(2)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.ui-autocomplete")))
    elements = driver.find_elements(By.CSS_SELECTOR, "ul.ui-autocomplete li.ui-menu-item")

    desired_text = "[ 00000 ] Aguascalientes /"
    for element in elements:
        if desired_text in element.text:
            element.click()
            break

    """

    """wait = WebDriverWait(driver, 5)
    colonia = driver.find_element(By.CSS_SELECTOR,"div.o_form_input_dropdown input.o_form_input.ui-autocomplete-input")
    colonia.clear()
    colonia.send_keys("0447")
    colonia.send_keys(Keys.ENTER)"""

    time.sleep(5000)

    driver.quit()


page_web()