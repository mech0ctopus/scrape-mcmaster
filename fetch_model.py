# -*- coding: utf-8 -*-
"""
Scrape 3D models from McMaster-Carr.

Requirements: Chromedriver.exe is in the same folder as this script.
"""
from selenium import webdriver
import time

test_part_numbers=['98173A200', '7529K105', '93250A440']

def fetch_model(part_numbers, delay=3):
    if type(part_numbers) is str:
        part_numbers=[part_numbers]
    
    #Start browser
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(chrome_options=options)
    
    #For each part number
    for part_number in part_numbers:
        driver.get('https://www.mcmaster.com/#' + str(part_number) + '/')
        #Pause for page to load
        time.sleep(delay)    
        #Find and Click submit button
        try:
            try:
                submit_button=driver.find_element_by_class_name("button-save--sidebyside")
            except:
                submit_button=driver.find_element_by_class_name("button-save--stacked")
            finally:
                submit_button.click()
        except:
            print('No button found or other error occured')
        finally:
            time.sleep(delay)
            
    driver.close()
    driver.quit
    
fetch_model(test_part_numbers)