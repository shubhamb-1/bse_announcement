from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from logic import add_to_db
import time
from threading import Timer



def fetch_new_data():

    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=options)

    url = "https://www.bseindia.com/corporates/ann.html"
    driver.get(url)


    table_ele = driver.find_elements(By.XPATH,"/html/body/div[1]/div[5]/div[2]/div/div[3]/div/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[4]/td")
    insert_li = list()

    for element in table_ele:
        if element:
            temp_dict = dict()
            element = element.find_elements(By.TAG_NAME,'tr')
            company_name ,company_id ,announcement,announcement_type,announcement_link,unique_id = None,None,None,None,None,None
            for i,ele in enumerate(element):
                announcement_time = None
                if i%3==0:
                    announcement_details = ele.find_elements(By.TAG_NAME,'td')
                    temp_split = announcement_details[0].text.split('-')
                    temp_dict['company_name'] = temp_split[0]
                    temp_dict['company_id'] = temp_split[1].strip()
                    temp_dict['announcement'] = temp_split[2]
                    print(temp_dict['company_name'],'|',temp_dict['company_id'],'|',temp_dict['announcement'])
                    temp_dict['announcement_type'] = announcement_details[1].text
                    temp_dict['announcement_link'] = announcement_details[2].find_elements(By.TAG_NAME,'a')[0].get_attribute("href")
                if i%3==1:
                    announcement_time =  ele.find_elements(By.TAG_NAME,'b')[0].text
                    temp_dict['announcement_time'] = datetime.strptime(announcement_time, "%d-%m-%Y %H:%M:%S")
                    print(temp_dict['announcement_time'])
                    temp_dict['unique_id'] = str(temp_dict['company_id']).strip()+str(temp_dict['announcement_time'].strftime("%H%M%S")).strip()
                    print(temp_dict['unique_id'])
                    insert_li.append(temp_dict)
                    #add_to_db(unique_id,company_name,company_id,announcement,announcement_type,announcement_link,announcement_time)
    add_to_db(insert_li)

def fetch_periodically():
    while True:
        t = Timer(30.0, fetch_new_data)
        t.start()
        time.sleep(10)



if __name__ == "__main__":
    fetch_periodically()
