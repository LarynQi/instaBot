# instaBot
[logo]: https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/1200px-Instagram_logo_2016.svg.png "Instagram logo"
An Instagram bot that can track who unfollows an account.

## Running the bot

- Check if you have virtualenv by running `pip list`
  - If you don't have it, install it by running `sudo pip install virtual env`
- cd into your working directory
- `virtualenv -p python3 venv`
- `source venv/bin/activate`
- `pip3 install selenium` in your venv
  - should say `(venv)` in the root of your terminal
- download the ChromeDriver from https://chromedriver.chromium.org/downloads
  - check your chrome version by clicking the 3 dots in the top right of your browser 
  - click "Help"
  - click "About Google Chrome"
  - download the corresponding driver for your OS
  - move the ChromeDriver to /usr/local/bin by typing `mv ~/Downloads/chromedriver /usr/local/bin`
 - run main.py using command line with your Python version
  - ex: `python3 main.py`
 done!

### Resources
  - credit goes to @Code Drip on YouTube for the idea and bulk of the code
    - [YouTube Video](https://www.youtube.com/watch?v=d2GBO_QjRlo&)
