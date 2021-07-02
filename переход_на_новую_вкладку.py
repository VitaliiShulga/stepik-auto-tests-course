import math
import time
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    #кликаем по кнопке
    browser.find_element_by_tag_name('button').click()

    #переходим на открывшуюсь вкладку
    browser.switch_to.window(browser.window_handles[1])
    #рассчитываем функцию от х и передаем значение
    x = browser.find_element_by_id('input_value').text
    y = calc(int(x))

    browser.find_element_by_id('answer').send_keys(str(y))
    browser.find_element_by_tag_name('button').click()

finally:
    time.sleep(5)
    browser.quit()