from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from fake_useragent import UserAgent
import csv


def entrance_exam():
    url = "https://diemthi.vnexpress.net/diem-thi-lop-10#area=2&college=0&q="
    for sbd in range(9000, 189292):
        userAgent = UserAgent()
        myoptions = webdriver.EdgeOptions()
        myoptions.add_argument(f'user-agent={userAgent.random}')
        scraper = webdriver.Edge(options=myoptions)
        scraper.get(f"{url}{sbd}")
        try:
            WebDriverWait(scraper, 30).until(presence_of_element_located((By.XPATH, '//*[@id="result"]/div[2]/div[2]/div/div[3]/div/table/tbody/tr/td[8]/strong')))
        except Exception:
            continue

        literature = scraper.find_element(By.XPATH, '//*[@id="result"]/div[2]/div[2]/div/div[3]/div/table/tbody/tr/td[4]')
        english =  scraper.find_element(By.XPATH, '//*[@id="result"]/div[2]/div[2]/div/div[3]/div/table/tbody/tr/td[5]')
        math = scraper.find_element(By.XPATH, '//*[@id="result"]/div[2]/div[2]/div/div[3]/div/table/tbody/tr/td[6]')
        major =  scraper.find_element(By.XPATH, '//*[@id="result"]/div[2]/div[2]/div/div[3]/div/table/tbody/tr/td[7]')
        total = scraper.find_element(By.XPATH, '//*[@id="result"]/div[2]/div[2]/div/div[3]/div/table/tbody/tr/td[8]/strong')

        with open("tracuudiem.csv", "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow((f"{sbd}", f"{literature.text}", f"{english.text}", f"{math.text}", f"{major.text}", f"{total.text}"))

entrance_exam()
print('Printing complete!')
