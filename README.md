WELCOME TO MY REPOSITORY!

Prerequisites
Anaconda 3.7
Python 3.7
Pip

Installation
Fork this repository under your own control and then clone the resulting repo onto your computer. Then, create a new virutal environment with Anaconda:
1. Conda create -n #name_your_environment
2. "Conda activate #your#named#environment

Installing packages:
1. In your terminal, type "pip install -r requirements.txt"
2. pip install sendgrid
3. pip install requests
4. pip install beautifulsoup4
5. pip install chromedriver (Note: if this doesn't work, see the website scraping instructions #3)
6. pip install pytest


Website Scraping:
1. In your terminal, check to see if homebrew is installed through typing "which brew"
2. If not installed, in your terminal type "/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
3. Follow the instructions listed at: http://chromedriver.chromium.org/ and download chromedriver

Installing your Sendgrid for One Time Notifications:
1. If not previously held, sign up for a free Sendgrid account (https://signup.sendgrid.com/) and create a key with "full permissions" acces (https://app.sendgrid.com/settings/api_keys) #https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/718d10fa22072a56101c20f82229910feb7cbc20/notes/python/packages/sendgrid.md

Installing Herko For Recurring Message Notifications:
1. Ensure that the Heroku application is installed (https://devcenter.heroku.com/categories/command-line)
2. If you do not previously have one, register for a new Heroku account https://signup.heroku.com/3. I
3. In your terminal, type "heroku login"
4. In your terminal, type "heroku create my-app-name" and change my-app-name to what you desire your application's name to be
5. In your terminal, type "heroku git:remote -a my-app-name" and change my-app-name to what you desire your application's name to be
6. Configure your email and api key email; in your terminal type "heroku config:set MY_SECRET_MESSAGE="abc123" -a my-app-name" and adjust the MY_SECRET_MESSAGE and "abc123" accordingly
6. In your terminal, type "git push heroku master"
7. Optional: in your terminal, you can type "heroku run "python app/logic.py" -a your_app_name" to see if it is properly working.
8. Log into heroku from your web browser. Navigate to the "Resources" tab  your application's Heroku dashboard, search for an add-on called "Heroku Scheduler" and provision the server with a free plan. 
9. "Navigate to the "Heroku Scheduler" resource from the "Resources" tab, then click to "Add a new Job". When adding the job, choose to execute the "app/send_email.py" script at a scheduled interval (e.g. every 10 minutes), and finally click to "Save" the job."
#https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/718d10fa22072a56101c20f82229910feb7cbc20/exercises/deploy-script-production.md

Security:
1. Create a file titled ".env". Within this file, type MY_EMAIL_ADDRESS="your_email_here" and SENDGRID_API_KEY="your_API_key_here" on different lines. Your Sendgrid API Key can be found by following the "Installing your sendgrid for one time notifications #1" instructions above.
2. Create a file titled ".gitignore". Within the file, type ".env" and "__pycache__/" on different lines

Running Tests:
1. In your terminal, type "pytest"

Using this directory:
1. You must run the freestyle.py file; all other files are supplementary and should work automatically if all goes according to plan!
