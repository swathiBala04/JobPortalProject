from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from datetime import datetime

import time

start_time = datetime.now()
#start_date = date.today()
#print(start_date)
#print(start_time)


# Job_Category = []
# Date_Time_Scrapped = []
# Searched_Job_Title =[]
# Job_Portal= []
# Job_Date_Posted = []
# Job_Title = []
# Job_Company_Name = []
# Job_Location = []
# Job_Phone_No = []
# Job_Email = []
# Job_Link = []
# Job_Description = []



searched_job_title = []
job_title = []
company_name = []
location = []
description =[]
job_link =[]
time_stamp = []


driver = webdriver.Chrome(executable_path="/Users/SB/WebDriver/chromedriver")
driver.get("https://www.monster.com/jobs/search/")
# sleep(2)
driver.maximize_window()


Monster_data = pd.DataFrame(columns=['Job Category' , 'Date Time Scrapped', 'Searched Job Title' , 'Position', 'CompanyName', 'Location','JobLink','TimeStamp', 'Description'])
# print the Title of the page
d = driver.title
print(d)

# Search for Job Title Textbox and pass value:
jobTitleSearch = driver.find_element_by_xpath("//input[@name='q' and @type='text']").send_keys('SDET')
print("Searched_job_title = SDET")
actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.perform()

# Search for Location Textbox and pass value:
# locationSearch = driver.find_element_by_xpath("//input[@name='where' and @type='text']").send_keys('Dallas')
actions.send_keys(Keys.TAB)
actions.perform()

# click search button:
searchButton = driver.find_element_by_xpath("//button[@type='submit' and @class='sc-dlfnbm doIxYG sc-BXqHe dVaZve ds-button']").click()
sleep(2)



# To extract Data Job Title, Company name, Location:
Job_count = list(driver.find_elements_by_class_name("results-card "))
print(type(Job_count), len(Job_count), Job_count.__sizeof__())

# for i in Job_count:
#
#     job_title = i.find_element_by_tag_name("h2")
#     company_name = i.find_element_by_tag_name("h3")
#     location = i.find_element_by_class_name("card-job-location")
#     description = i.find_element_by_xpath("//div[@name='sanitizedHtml']")
#     print("POSITION: " + job_title.text + " COMPANY_NAME: ", company_name.text + " JOB_LOCATION: ", location.text, "description: ", description.text)
#     driver.execute_script("window.scrollTo(0,50)")
#     sleep(2)


Job_count = len(driver.find_elements_by_class_name("results-card "))
print(Job_count)
for i in range(1, Job_count):

    if (i==11):
        #print("entering")
        nextPage = driver.find_element_by_tag_name("h2").click()
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()
        sleep(5)
        #print(i)
        jobTitle_xpath = '//*[@id="card-view-panel"]/div/div[1]/div[' + str(
            i) + ']/div[1]/div[1]/div/div[1]/div[2]/a/h2'
        company_name_xpath = '//*[@id="card-view-panel"]/div/div[1]/div[' + str(
            i) + ']/div[1]/div[1]/div/div[1]/div[2]/h3'
        location_xpath = '//*[@id="card-view-panel"]/div/div[1]/div[' + str(
            i) + ']/div[1]/div[1]/div/div[1]/div[2]/span'
        descrpition_xpath = "//*[@id='card-view-panel']/div/div[1]/div["+str(i)+"]/div[2]/div[1]/div"
        job_link_xpath = '//*[@id="card-view-panel"]/div/div[1]/div['+str(i)+']/div[1]/div[1]/div/div[1]/div[2]/a'
        time_stamp_xpath = '//*[@id="card-view-panel"]/div/div[1]/div['+str(i)+']/div[2]/div[2]/div/div'

        job_title = driver.find_element_by_xpath(jobTitle_xpath)
        company_name = driver.find_element_by_xpath(company_name_xpath)
        location = driver.find_element_by_xpath(location_xpath)
        description = driver.find_element_by_xpath(descrpition_xpath)
        job_link = driver.find_element_by_xpath(job_link_xpath).get_attribute("href")
        time_stamp = driver.find_element_by_xpath(time_stamp_xpath)

        # print(str(i)+"." + " POSITION:" + job_title.text + "  COMPANY_NAME:"  + company_name.text + "  JOB_LOCATION:" +
        #       location.text + " JOB_LINK: " + job_link+ " TIME_STAMP:" + time_stamp.text +" DESCRIPITION:" + description.text)
    else:
        #print(i)
        company_name_xpath = "//*[@id='card-view-panel']/div/div[1]/div[" + str(i) + " ]/div[1]/div[1]/div/div[1]/div[2]/h3"
        jobTitle_xpath = '//*[@id="card-view-panel"]/div/div[1]/div[' + str(i) + ']/div[1]/div[1]/div/div[1]/div[2]/a/h2'
        location_xpath = '//*[@id="card-view-panel"]/div/div[1]/div[' + str(i) + ']/div[1]/div[1]/div/div[1]/div[2]/span'
        descrpition_xpath = "//*[@id='card-view-panel']/div/div[1]/div["+str(i)+"]/div[2]/div[1]/div"
        job_link_xpath = '//*[@id="card-view-panel"]/div/div[1]/div['+str(i)+']/div[1]/div[1]/div/div[1]/div[2]/a'
        time_stamp_xpath = '//*[@id="card-view-panel"]/div/div[1]/div['+str(i)+']/div[2]/div[2]/div/div'

        job_title = driver.find_element_by_xpath(jobTitle_xpath)
        company_name = driver.find_element_by_xpath(company_name_xpath)
        location = driver.find_element_by_xpath(location_xpath)
        job_link = driver.find_element_by_xpath(job_link_xpath).get_attribute("href")
        time_stamp = driver.find_element_by_xpath(time_stamp_xpath)

        description = driver.find_element_by_xpath(descrpition_xpath)

        # print(str(i)+"."+ " POSITION:" + job_title.text + "  COMPANY_NAME:" + company_name + "  JOB_LOCATION:" + location.text +
        #      " JOB_LINK: " +job_link
        #      + " TIME_STAMP:" + time_stamp.text +" DESCRIPTION:" + description.text)

        #print(job_title, "company name " + company_name, location)
        Monster_data.loc[len(Monster_data)] = ['QA', start_time, 'SDET' , job_title.text, company_name.text, location.text,job_link, time_stamp.text, description.text]
print(Monster_data)
Monster_data.to_csv('NewMonster.csv')


#Monster_data.to_csv('MonsterData.csv')
#print(Monster_data)

driver.quit()
# end_time = time.time()
# print(end_time - start_time)
