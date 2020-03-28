<div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/1200px-Instagram_logo_2016.svg.png" alt="drawing" width="100"/>

# instaBot 
**An Instagram bot that can track who unfollows an account.**


## Running the bot
- If you don't have Python download it [here](https://www.python.org/downloads/)
- If you don't have pip, run `sudo easy_install pip`
- Check if you have virtualenv by running `pip list`
  - If you don't have it, install it by running `sudo pip install virtualenv`
- cd into the repo then run the following commands: <br/>
`virtualenv -p python3 venv` <br/>
`source venv/bin/activate` <br/>
`pip3 install selenium` (in your venv)
  - Sanity check: Your terminal ps1/prompt should now start with `(venv)`
- Download the [ChromeDriver](https://chromedriver.chromium.org/downloads)
  - Check your Chrome version by clicking the 3 dots in the top right of your browser 
  - Click "Help"
  - Click "About Google Chrome"
  - Download the corresponding driver for your OS and unzip the file in your downloads
  - Move the ChromeDriver to /usr/local/bin by typing `mv ~/Downloads/chromedriver /usr/local/bin`
    - If you're getting a permission denied error run `sudo mv ~/Downloads/chromedriver /usr/local/bin`
- Enter in your Instagram username and password as strings in resources.py with the text editor of your choice
- Run main.py via command line with your Python version
  - ex: `python3 main.py` <br/>
  <br/>
You're all set! Watch the bot work its magic :)

### Resources
  - Credits go to [@Code Drip](https://www.youtube.com/watch?v=d2GBO_QjRlo&) for the idea and bulk of the code
