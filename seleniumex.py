from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

url = "https://www.bseindia.com/corporates/ann.html"
driver.get(url)

# wait = WebDriverWait(driver, 10)
# wait.until(EC.presence_of_element_located((By.ID, "announcementTable")))

# company_name = driver.find_elements_by_xpath("//[@id='lblann']/table/tbody/tr[4]/td/table[3]")
# description = driver.find_elements_by_xpath("//td[@class='TTRow_right'][1]")
# time = driver.find_elements_by_xpath("//td[@class='TTRow_right'][2]")

# print(company_name)

#//*[@id="lblann"]/table/tbody/tr[4]/td/table[3]

#
# Working
# test = driver.find_elements(By.XPATH,"/html/body/div[1]/div[5]/div[2]/div/div[3]/div/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[4]/td")
# print(test[0].text)
# for element in test:
#     print(element.text)
#     links = element.find_elements(By.CLASS_NAME,"tablebluelink")
#     for link in links:
#         print(link.get_attribute("href"))

# Working
# /html/body/div[1]/div[5]/div[2]/div/div[3]/div/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[4]/td
# /html/body/div[1]/div[5]/div[2]/div/div[3]/div/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table[1]