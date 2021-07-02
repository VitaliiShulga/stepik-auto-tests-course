from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name('button').click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id('input_value').text
    y = calc(int(x))

    browser.find_element_by_id('answer').send_keys(str(y))
    #input_answer.send_keys(str(y))
    browser.find_element_by_tag_name('button').click()

finally:
    time.sleep(5)
    browser.quit()