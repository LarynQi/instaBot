# instaBot
An Instagram bot that can track who unfollows an account.

## Running the bot

- check if you have virtualenv by running 'pip list'
  - if you don't have it, install it by running 'sudo pip install virtual env'
- cd into your working directory
- 'virtualenv -p python3 venv'
- 'source venv/bin/activate'
- pip3 install selenium
- download the ChromeDriver from https://chromedriver.chromium.org/downloads
  - check your chrome version by clicking the 3 dots in the top right of your browser 
  - click "Help"
  - click "About Google Chrome"
  - download the corresponding driver for your OS
  - move the ChromeDriver to /usr/local/bin by typing 'mv ~/Downloads/chromedriver /usr/local/bin'
 - run main.py using command line with python
  - ex: 'python3 main.py'
 done!

### Resources
  - credit goes to @Code Drip on YouTube for the idea and bulk of the code
    - link: https://www.youtube.com/watch?v=d2GBO_QjRlo&t=608s
