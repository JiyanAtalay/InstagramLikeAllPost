from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
url = "https://www.instagram.com/"
driver.get(url)
sleep(12)
# Login
user_name = driver.find_elements(By.TAG_NAME, "input")
user_name[0].send_keys("") # Nick
user_name[1].send_keys("") # Password

sleep(3)
# Click Login button
login_button = driver.find_elements(By.TAG_NAME, "button")
login_button[-2].click()

sleep(15)
# Pass Save Login Information?
not_now_button = driver.find_element(By.XPATH, "//div[@role='button']").click()

sleep(25)
# Pass Open Notifications
not_now_button2 = driver.find_elements(By.TAG_NAME, "button")
not_now_button2[-1].click()

sleep(10)

driver.get("https://www.instagram.com/") # Add nick name

sleep(30)
# Chose the first post
first_post = driver.find_elements(By.XPATH, "//div[@class='_aagw']")
first_post[0].click()

sleep(14)
# Like first post
like_button = driver.find_element(By.XPATH, "//span[@class='_aamw']")
like_button.click()

sleep(3)
# Skip to post 2
next_button = driver.find_elements(By.XPATH,"//button[@class='_abl-']")
next_button[0].click()

sleep(5)
# Like all post
i = 0
a = "number of posts -1"
while i<=a:
    try:
        like_button = driver.find_element(By.XPATH, "//span[@class='_aamw']")
        like_button.click()

        sleep(2)

        next_button = driver.find_elements(By.XPATH,"//button[@class='_abl-']")
        next_button[1].click()

        sleep(3)
        i +=1
    except IndexError:
        print("Done")
        break
    

driver.close()
