from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

def Check_my_grade():
    browser = webdriver.Chrome()
    Grade = "н/д"
    browser.get('https://result.rcoi.net/default.aspx')

    # для поиска элемента в примере используется XPath (F12 в браузере, поиск нужного элемента, ПКМ - Copy - XPath)

    # ввод данных в поля для ввода
    browser.find_element(by = By.XPATH, value='//*[@id="ctl00_LastName"]').send_keys('Ваша фамилия')
    sleep(1)
    browser.find_element(by=By.XPATH, value='//*[@id="ctl00_FirstName"]').send_keys('Ваше имя')
    sleep(1)
    browser.find_element(by=By.XPATH, value='//*[@id="ctl00_MidName"]').send_keys('Ваше отчество')
    sleep(1)
    browser.find_element(by=By.XPATH, value='//*[@id="ctl00_Number"]').send_keys('Номер вашего паспорта')

    # нажать на chechbox и кнопку
    browser.find_element(by=By.XPATH, value='//*[@id="ctl00_AcceptDataProcessing"]').click()
    browser.find_element(by=By.XPATH, value='//*[@id="ctl00_LoginButton"]').click()
    sleep(2)
    #открпытие другой ссылки
    #browser.get('https://result.rcoi.net/res_exams.aspx')
    browser.find_element(by=By.XPATH, value='//*[@id="ctl00_ParticipantMainMenu"]/div[2]/div/table/tbody/tr[3]/td[2]/a').click()
    Grade = browser.find_element(by=By.XPATH, value='/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/table/tbody/tr[3]/td[5]').text #в value вставте путь на ячейку с нужной оценкой.
    sleep(2)
    browser.close()
    return Grade

#

