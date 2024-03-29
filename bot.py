from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException
import time
import random

#Path of your chrome web driver
chrome_webDriver_path = "path of your chrome webdriver"
#eg.- "C:\\Users\\danish\\Downloads\\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
min_followers_limit = 125
loginUsername = "yourUsername"
loginPassword = "yourPassword"
no_of_dm_to_send = 20
#list of usernames to send DM
target_lst = ['bts_x_blackpink_fan.47', 's_radha_krishna_premik', 'sumaira_14_khan']



# Create Chrome WebDriver with custom options
chrome_options = Options()
chrome_prefs = {"profile.default_content_setting_values": {"images": 1, "plugins": 2}}
chrome_options.add_experimental_option("prefs", chrome_prefs)
s = Service(chrome_webDriver_path)


driver = webdriver.Chrome(service = s, options=chrome_options)
no_of_dm_send = 0
no_of_low_profile_ids = 0
total_no_of_targets_hit = 0
driver.get("https://www.instagram.com/")


target_lst = list(set(target_lst))

def get_delay():
    n = random.randint(5,7)
    time.sleep(n)

def get_small_delay():
    n = random.randint(2,3)
    time.sleep(n)

def log_in(loginUsername,loginPassword):
    print("Initializing log in...")
    get_delay()
    #getting username field
    username = driver.find_element_by_xpath("""/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input""")
    username.send_keys(loginUsername)

    #getting password field
    password = driver.find_element_by_xpath("""/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input""")
    password.send_keys(loginPassword)

    #clicking log in button
    driver.find_element_by_xpath("""/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div""").click()
    get_delay()
    
    print("Logged in succesfully...")
    get_small_delay()

    try:
        #Trying to click on Save account's "Not now" button to not save the password
        driver.find_element_by_xpath("""//*[contains(text(),'Not now')]""").click()
        time.sleep(2)
    except NoSuchElementException:
        ij=0
    time.sleep(4)
    try:
        #Trying to click on "Not now" button on the "Turn on notifications" dialog
        driver.find_element_by_xpath("""//*[contains(text(),'Not Now')]""").click()

    except NoSuchElementException:
        ij=0

def search_profile(acc_username):

    username_link = "https://www.instagram.com/"
    username_link += acc_username

    #going to profile
    driver.get(username_link)

def follow():
    #Clicking on follow button
    driver.find_element_by_xpath("""//*[contains(text(),'Follow')]""").click()

def goTo_msg():
    #clicking on messege
    driver.find_element_by_xpath("""//div[contains(text(),'Message')]""").click()
    
def type_msg():
    #Getting message box and Clicking on it
    message_sec = driver.find_element_by_xpath("""/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p""")
    message_sec.click()
    #Pasting the coppied text to message
    message_sec.send_keys(Keys.CONTROL, 'v')

def send_msg():
    #clicking send message
    driver.find_element_by_xpath("""/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]""").click()

def notHighProfile(target):
    #Checking if the target account has required no. of followers or not
    try:
        followersCount = int(driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span").get_attribute("title").replace(",",""))

        if followersCount > min_followers_limit:
            #print("Yes a high profile: ",target)
            return False
        else:
            #print("Not a high profile: ",target)
            return True
    #Excepting all errors
    except NoSuchElementException:
        #print("Not a high profile: ",target)
        return True
    ##xcepting value errors that occurs
    except ValueError:
        #print("Not a high profile: ",target)
        return True


#Main flow
log_in(loginUsername,loginPassword)
get_delay()
#Running a loop to get target accounts
for target in target_lst:
    
    total_no_of_targets_hit += 1
    print("\n\n\n\n\n\n-> No. of DMs sent: ",no_of_dm_send)
    print("-> No. of low profile users: ",no_of_low_profile_ids)
    print("-> Total no. of target hitted: ",total_no_of_targets_hit)

    #Searching the profile
    search_profile(target)
    print("Searching profile: ", target)
    get_delay()
    #Removing the target's username from target list
    target_lst.remove(target)
    #Checking the account's followers count 
    if notHighProfile(target):
        print("Acoount skipped...")
        no_of_low_profile_ids +=  1
        continue
    #Trying to follow
    try:
        time.sleep(3)
        follow()
        print("Trying to follow")
    
    except NoSuchElementException:
        print("Account already followed... Skipping to next profile...")
        continue
    
    get_delay()

    #Trying to go to the message section
    try:
        get_small_delay()
        goTo_msg()
        print("Trying to go to msg section...")
    
    except NoSuchElementException:
        print("Unable to go to msg... Skipping to next profle...")
        continue
    except ElementClickInterceptedException:
        print("Unable to go to msg... Skipping to next profle...")
        continue
    except Exception as e:
        print("Unable to go to msg... Skipping to next profle...")
        continue
    
    get_delay()

    #Trying to type the message
    try:
        time.sleep(1)
        type_msg()
        print("Typing the msg...")
        time.sleep(1)
    except NoSuchElementException:
        print("Message not allowed... Skipping to next profile...")
        continue
    except StaleElementReferenceException:
        print("Message not allowed... Skipping to next profile...")
        continue
    #Trying to send the message
    try:
        time.sleep(1)
        send_msg()
        print("Sending the msg...")
    except NoSuchElementException:
        print("Unable to send the msg... Skipping to next profile")
        continue
    except ElementClickInterceptedException:
        print("Unable to send the msg... Skipping to next profile")
        continue
    no_of_dm_send += 1    
    
    get_small_delay()

    #Chcking if the a desired no. of dm are send
    if no_of_dm_send == no_of_dm_to_send:
        print(target_lst)
        print("Take some rest... 20 DMs sent succesfully!!!")
        break

print("\n\n\n\n\n\nAccount list empty!!!")
