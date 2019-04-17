from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'U:/geckodriver.exe')
browser.get(r'https://cnn.com')
elem = browser.find_element_by_partial_link_text('Notre Dame')
elem.click()
