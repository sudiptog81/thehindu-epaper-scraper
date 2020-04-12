# The Hindu ePaper Scraper

Script for scraping the e-paper of the prestigious English daily 'The Hindu'. The edition and city of the newspaper can be selected by logging in to the portal manually and selecting the edition. The script downloads the edition selected in one's profile. This script is written for UNIX.

This script uses the Selenium WebDriver to open a Chromium window in a Virtual Display, by leveraging Xvfb, and navigates to the login page of The Hindu e-Paper portal. It closes any popup displayed on the login page and proceeds to enter the credentials and submitting the login form. Credentials have to be provided in place of `YOUR-EMAIL` and `YOUR-PASSWORD` in `main.py`.

Once the web application of 'The Hindu e-Paper' loads successfully, it invokes the JavaScript function that is responsible for downloading all the pages of the newspaper as a PDF.

The PDF is then downloaded to a predefined location which is `/media/volume-extra/theHindu/<date-in-dd-mm-yyyy>` by default and can be overridden by replacing this path in all of the files.

This PDF is then uploaded to a MEGA folder and then deleted from the local machine. The PDF can then be accessed from all devices supported by the MEGA clients. One may override the behaviour of the script in `upload.py` to change the uploading and cleanup logic.

## Sample Downloads

[View The Hindu ePaper folder on MEGA](https://mega.nz/folder/GF9Xnbxa#ynPVRk1nT63le5rpA9IxCw)

## Quick Start

  - Open a terminal and navigate to the directory where you have cloned the repository.
  - Change `YOUR-EMAIL` and `YOUR-PASSWORD` in `main.py`.
  - Change `/media/volume-extra/theHindu/` to the absolute location where you want the e-Papers to be downloaded in `main.py` as well as `upload.py`. This folder must exist before running the script.
  - Install all dependencies from PyPI using the command `pip install -r requirements.txt`.
  - Run the script by executing `./scrape.sh`.

## Scheduling the Job

One can schedule the task to be run daily at 06:00 AM (take care of the time zone) using cron jobs. Open the cron table using the command `crontab -e` and add the line `0 6 * * * /location/to/scrape.sh` to the end of the file and save the file. The task will run automatically and the latest edition of 'The Hindu' will be uploaded to the MEGA folder everyday by 06:05 AM.

## Author

Sudipto Ghosh ([sudipto.ghosh.pro](https://sudipto.ghosh.pro))

## License

Source code is distributed under the MIT License.

All rights to the textual and non-textual media sourced from 'The Hindu e-Paper' using this script are reserved by The Hindy Group Publishing Pvt Ltd.
