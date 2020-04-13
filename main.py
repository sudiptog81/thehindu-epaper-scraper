import os
from time import sleep
from datetime import datetime
from pyvirtualdisplay import Display
from notify_run import Notify
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

notify = Notify()

display = Display(visible=0, size=(1336, 768))
display.start()

download_dir = '/media/volume-extra/theHindu/' + \
    str(datetime.today().strftime('%d-%m-%Y'))
profile = {
    'download.prompt_for_download': False,
    'download.default_directory': download_dir,
    'download.directory_upgrade': True,
    'plugins.always_open_pdf_externally': True,
}

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', profile)

browser = webdriver.Chrome(options=options, service_log_path='/dev/null')
browser.get('https://epaper.thehindu.com/Login/LandingPage')

try:
    sleep(5)
    browser.find_element_by_id('btnIagree').click()
    sleep(5)
    browser.find_element_by_id('txtNumber1').send_keys('YOUR-EMAIL')
    sleep(5)
    browser.find_element_by_id('txtPassword').send_keys('YOUR-PASSWORD')
    sleep(5)
    browser.find_element_by_class_name('btn-signup').click()
    sleep(10)
    browser.execute_script('DownloadEditionPdf();')
    sleep(15)
    print('SUCCESS: Saved The Hindu ePaper at ' + \
          str(datetime.today().strftime('%d-%m-%Y %H:%M:%S')))
    notify.send('SAVED: The Hindu ' + \
          str(datetime.today().strftime('%d-%m-%Y')))
except Exception as e:
    print('FAILED: Could Not Save PDF')
    print(str(e))
    notify.send('FAILURE: The Hindu ' + \
          str(datetime.today().strftime('%d-%m-%Y')))
finally:
    browser.quit()
    display.stop()

