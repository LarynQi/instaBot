from selenium import webdriver
import time
from resources import username, password
from webdriver_manager.chrome import ChromeDriverManager
import matplotlib.pyplot as plt
import operator

class instaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
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
        time.sleep(5)

    def getFollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href, \"/followers/\")]")\
            .click()
        time.sleep(3)
        self.followers = self._get_names()

    def getFollowing(self):
        self.driver.find_element_by_xpath("//a[contains(@href, \"/following/\")]")\
            .click()
        time.sleep(3)
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
            time.sleep(3)
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

    def getDevotion(self):
        scroll = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/article/div")
        curr, last = 1, 0
        while last != curr:
            last = curr
            time.sleep(1)
            curr = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll)
        links = scroll.find_elements_by_tag_name("a")
        scores = dict()
        for name in self.followers:
            scores[name] = 0
        for i in range(0, len(links)):
            links[i].click()
            time.sleep(3)
            comments = self.getComments()
            # time.sleep(30)
            self.driver.find_element_by_xpath("//button[@class=\"sqdOP yWX7d     _8A5w5    \"]").click()
            time.sleep(2)
            names = self.getLikes()
            for name in names:
                # scores[name] = scores.get(name, 0) + (1 / (i + 1))
                if name in self.followers:
                    # scores[name] = scores.get(name, 0) + (1 / (i + 1))
                    scores[name] += (1 / (i + 1))
            for name in comments:
                if name in self.followers:
                    scores[name] += (3 / (i + 1))
                # scores[name] = scores.get(name, 0) + (3 / (i + 1))
            # self.driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/div/div[2]/button")\
            # .click()
            self.driver.find_element_by_xpath("/html/body/div[4]/div[3]").click()
        self.scale_scores(scores)
        self.plot(scores)

        # print(scores['heylucylee'])
    def scale_scores(self, scores):
        max_val = max(scores.values())
        for name in scores:
            scores[name] = round(10 * (scores[name] / max_val), 2)
    def plot(self, scores):
        # sorting: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
        # names = list(scores.keys())
        # values = []
        # for k in names:
        #     values.append(scores[k])
        sorted_scores = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
        names = []
        values = []
        all_names = []
        all_values = []
        count = 0
        for t in sorted_scores:
            if count < 10:
                names.append(t[0])
                values.append(t[1])
            all_names.append(t[0])
            all_values.append(t[1])
            count += 1
            
        reversed_scores = sorted_scores[::-1]
        r_names = []
        r_values = []
        count = 0
        for t in reversed_scores:
            r_names.append(t[0])
            r_values.append(t[1])
            count += 1
            if count == 10:
                break
        fig = plt.figure(figsize=(15, 7.5))
        # fig, axs = plt.subplots(2)
        fig.suptitle(f'Devotion of {self.username}\'s Top 10 Instagram Followers', fontsize=18)
        # https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot
        plt.rcParams.update({'font.size': 9})


        plt.bar(names, values)
        # axs[1].bar(all_names, all_values)
        # bins = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
        # n, bins, patches = axs[1].hist(all_values, bins, facecolor='green',histtype='bar', rwidth=0.25)


        # plt.plot(bins, 'r--', linewidth=1)
        # plt.axis(True)
        plt.ylabel('Devotion Score', fontsize=14)
        plt.xlabel('Followers', fontsize=14)
        # font = {'family' : 'normal',
        # 'weight' : 'bold',
        # 'size'   : 22}
        # matplotlib.rc('font', **font)
        plt.show(block=False)

        query = '_'
        while query != '' and query != 'q':
            query = input("Whose devotion score would you like to see?\n")
            if query == 'all':
                result = ''
                count = 0
                for name in all_names:
                    count += 1
                    result += f'{count}. {name} - {scores[name]}\n'
                print(result)
            elif query in scores:
                # print(f'{query}\'s devotion score: {scores[query]}')
                print(f'{all_names.index(query) + 1}. {query} - {scores[query]}\n')
            elif query != '' and query != 'q':
                print(f'ERROR: {query} is not one of your followers\n')
        quit()
        # plt.figure(figsize=(15, 10))
        # fig, axs = plt.subplots(2, 1, constrained_layout=True)
        # fig.suptitle(f'Devotion of {self.username}\'s Instagram followers')
        # axs[0].bar(names, values)
        # axs[0].set_title('Top 10')
        # axs[1].bar(r_names, r_values)
        # axs[1].set_title('Bottom 10')
        # plt.rcParams.update({'font.size': 9})
        # axs[0].set_xlabel('Followers')
        # axs[0].set_ylabel('Devotion Score')

        # axs[1].set_xlabel('Followers')
        # axs[1].set_ylabel('Devotion Score')

        # plt.show(block=False)

    def getLikes(self):
        # scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]")
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div")
        curr, last = 1, 0
        names = set()
        links = self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div").find_elements_by_tag_name("a")
        for l in links:
            if l.text != "":
                names.add(l.text)
        while last != curr:
            last = curr
            curr = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
            time.sleep(1.25)
            links = self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div").find_elements_by_tag_name("a")
            for l in links:
                if l.text != "":
                    names.add(l.text)
        # links = self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div").find_elements_by_tag_name("a")
        # names = [name.text for name in links if name.text != ""]

        time.sleep(1)
        # print(names)
        print(len(names))
        # self.driver.find_element_by_xpath('//button[@class=\"wpO6b \"]').click()
        # self.driver.find_element_by_xpath('/html/body/div[4]/div[3]').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div/div[2]/button').click()
        return names
    def getComments(self):
        #load comments
        while True:
            try:
                self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[1]/ul/li/div').click()
            except:
                break
        links = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[1]').find_elements_by_tag_name("a")
        # names = [name.text for name in links if name.text != "" and name.get_attribute("class") == "_2dbep qNELH kIKUG"]
        names = [name.text for name in links if name.text != "" and name.get_attribute("class") == "sqdOP yWX7d     _8A5w5   ZIAjV " and name.text != username]
        # weeks ago is "gU-I7"
        # print(names)
        return names

    months = dict()
    # months['January'] = 
    def getDate(self):
        time = self.driver.find_element_by_xpath('//time[@class=\"_1o9PC Nzb55\"]').text




def main():
    try:
        myBot = instaBot(username, password)
        myBot.login()
        myBot.myProfile()
        myBot.getFollowers()
        myBot.getDevotion()
    except Exception as e:
        print(e)
        myBot.driver.quit()
        main()
# myBot = instaBot(username, password)
# myBot.login()
# myBot.myProfile()
# myBot.getFollowers()
# myBot.getDevotion()
main()


# myBot.getFollowers()
# myBot.getFollowing()
# myBot.getUnfollowers()
# myBot.getNotFollowing()