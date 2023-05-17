from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

async def get_user_info(urlnum):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--single-process")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument('window-size=1920x1080')
        chrome_options.add_argument("disable-gpu")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        url = "https://pams.postech.ac.kr/postech/cmm/fms/sharePortfolio.do?uuid=" + urlnum + "&pAll=Y"
        driver.get(url)
    except:
        raise Exception('webdriver 접속이 정상적으로 잘 이루어 지지 않았습니다')

    #기본정보 불러오기
    basicInfo_list = []
    try:
        table = driver.find_element("xpath", '//*[@id="movebox1"]/div/table')
        tbody = table.find_element("tag name", "tbody")
        trs = tbody.find_elements("tag name", "tr")
    except:
        raise Exception('Failed to access pams site correctly. 다른 세션이 있는지 확인해 주세요.')

    for tr in trs:
        tds = tr.find_elements("tag name", "td")
        for td in tds:
            basicInfo_list.append(td.text)

    #교내활동 불러오기
    schoolAct_list = []

    try:
        div = driver.find_element("id", "ncrListDiv")
        table = div.find_element("tag name", "table")
        tbody = table.find_element("tag name", "tbody")
        trs = tbody.find_elements("tag name", "tr")
    except:
        raise Exception('Failed to access pams site correctly. 다른 세션이 있는지 확인해 주세요.')

    for tr in trs:
        tds = tr.find_elements("tag name", "td")
        for td in tds:
            schoolAct_list.append(td.text)


    #학생단체활동 불러오기
    clubAct_list = []
    try:
        div = driver.find_element("id", "inActListDiv")
        table = div.find_element("tag name", "table")
        tbody = table.find_element("tag name", "tbody")
        trs = tbody.find_elements("tag name", "tr")
    except:
        raise Exception('Failed to access pams site correctly. 다른 세션이 있는지 확인해 주세요.')

    for tr in trs:
        tds = tr.find_elements("tag name", "td")
        for td in tds:
            clubAct_list.append(td.text)

    #봉사활동 불러오기
    volunteer_list = []
    try:
        div = driver.find_element("id", "outActListDiv1")
        table = div.find_element("tag name", "table")
        tbody = table.find_element("tag name", "tbody")
        trs = tbody.find_elements("tag name", "tr")
    except:
        raise Exception('Failed to access pams site correctly. 다른 세션이 있는지 확인해 주세요.')

    for tr in trs:
        tds = tr.find_elements("tag name", "td")
        for td in tds:
            volunteer_list.append(td.text)


    #대외활동 불러오기
    extraAct_list = []
    try:
        div = driver.find_element("id", "outActListDiv2")
        table = div.find_element("tag name", "table")
        tbody = table.find_element("tag name", "tbody")
        trs = tbody.find_elements("tag name", "tr")
    except:
        raise Exception('Failed to access pams site correctly. 다른 세션이 있는지 확인해 주세요.')

    for tr in trs:
        tds = tr.find_elements("tag name", "td")
        for td in tds:
            extraAct_list.append(td.text)

    driver.close()
    return basicInfo_list, schoolAct_list, clubAct_list, volunteer_list, extraAct_list
