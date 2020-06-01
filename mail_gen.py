import random, string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pass_min_char = 16
pass_allchar = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(pass_allchar) for x in range(pass_min_char))
password_result = password

user_min_char = 7
user_allchar = string.ascii_letters + string.digits
username = "".join(random.choice(user_allchar) for i in range(user_min_char))
username_result = username

first_name_char = 5
first_name_type = string.ascii_letters
firstname = "".join(random.choice(first_name_type) for i in range(first_name_char))
firstname_result = firstname

last_name_char = 10
last_name_type = string.ascii_letters
lastname = "".join(random.choice(first_name_type) for i in range(first_name_char))
lastname_result = lastname

print("This is your username : ",firstname_result+'.'+lastname_result+'@vfemail.net' "\nThis is your password : ",password_result)



def mail():
    driver = webdriver.Firefox(executable_path='/home/lager/pycharm/Generators/generators/geckodriver')
    driver.get('https://vfemail.net/regnorm/')

    first_name = driver.find_element_by_id('first_name')
    first_name.send_keys(firstname_result)
    last_name = driver.find_element_by_id('last_name')
    last_name.send_keys(lastname_result)

    #user_name = driver.find_element_by_id('user_name')
    #user_name.send_keys(username_result)
    passw1 = driver.find_element_by_id('passwd_1')
    passw1.send_keys(password_result)
    passw2 = driver.find_element_by_id('passwd_2')
    passw2.send_keys(password_result)

    mail_coll = "This is your username : ", firstname_result + '.' + lastname_result + '@vfemail.net' "\nThis is your password : ", password_result

    mail_doc = open('mail.txt','w+')
    mail_doc.write(mail_coll)
    mail_doc.close()
    
mail()


