from selenium import webdriver
import time
from resources import username, password

class instaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
        self.driver.get("https://www.instagram.com/")
        ###DEBUG###
        # print(username)
        # print(password)
        ###########
        time.sleep(2)

    def login(self):
        username_field = self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(self.username)
        password_field = self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(self.password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        time.sleep(7)

        self.driver.find_element_by_xpath("//button[contains(text(), \"Not Now\")]")\
            .click()
        time.sleep(2)

    def myProfile(self):
        self.driver.find_element_by_xpath("//a[contains(@href, \"/{}\")]"\
            .format(self.username)).click()
        time.sleep(2)

    def getFollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href, \"/followers/\")]")\
            .click()
        time.sleep(2)
        self.followers = self._get_names()

    def getFollowing(self):
        self.driver.find_element_by_xpath("//a[contains(@href, \"/following/\")]")\
            .click()
        time.sleep(2)
        self.following = self._get_names()

    def getUnfollowers(self):
        unfollowers = [name for name in self.following if name not in self.followers]
        unfollowers.sort()
        print("Unfollowers: " + str(unfollowers))

    def getNotFollowing(self):
        notFollowing = [name for name in self.followers if name not in self.following]
        notFollowing.sort()
        print("Not Following: " + str(notFollowing))

    def _get_names(self):
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        curr, last = 1, 0
        while last != curr:
            last = curr
            time.sleep(1)
            curr = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name("a")
        names = [name.text for name in links if name.text != ""]
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        time.sleep(1)
        return names

myBot = instaBot(username, password)

myBot.login()
myBot.myProfile()
myBot.getFollowers()
myBot.getFollowing()
myBot.getUnfollowers()
myBot.getNotFollowing()