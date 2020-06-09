#pipenv: /home/lager/.local/share/virtualenvs/mailgen-wnDkhgxz
import random, string, argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def generated():
    first_name_char = 5
    first_name_type = string.ascii_letters
    firstname = "".join(random.choice(first_name_type) for i in range(first_name_char))
    firstname_result = firstname

    last_name_char = 10
    last_name_type = string.ascii_letters
    lastname = "".join(random.choice(last_name_type) for i in range(last_name_char))
    lastname_result = lastname

    print("This is your username : ",firstname_result+'.'+lastname_result+'@vfemail.net' "\nThis is your password : ",password_result)
    driver = webdriver.Firefox(executable_path='/home/lager/PycharmProjects/Generators/mailgen/geckodriver')
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

    mail_coll = "This is your username: "+ firstname_result + '.' + lastname_result + '@vfemail.net' + "\n" + "This is your password: "+ password_result
    mail_doc = open('mail.txt','w')
    mail_doc.write(str(mail_coll))
    mail_doc.close()

#Description of the program
parser = argparse.ArgumentParser(prog='MailGen',
description='',
usage="Opens up a website with pre-filled info for creating dummy email accounts \
        \n       Type in username with format mail_gen.py -f FIRSTNAME -l LASTNAME \
        \n       Your credentials will appear in the mail.txt file \
        \n       Generate a username with -r or --random \
        \n       Username format is firstname.lastname@vfemail.com ")

#Positional arguments
parser.add_argument("-f","--firstname",
help="select your own username",
action="store")
parser.add_argument("-l","--lastname",
help="select your lastname",
action="store")

#Optional argument for randomizing username
parser.add_argument("-r", "--random",
help="randomize username",
action="store_true")
args = parser.parse_args()


pass_min_char = 20
pass_allchar = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(pass_allchar) for x in range(pass_min_char))
password_result = password



if args.random:
    generated()
    
if args.firstname and args.lastname:
    driver = webdriver.Firefox(executable_path='/home/lager/PycharmProjects/Generators/mailgen/geckodriver')
    driver.get('https://vfemail.net/regnorm/')
    first_name = driver.find_element_by_id('first_name')
    first_name.send_keys(args.firstname)
    last_name = driver.find_element_by_id('last_name')
    last_name.send_keys(args.lastname)

    passw1 = driver.find_element_by_id('passwd_1')
    passw1.send_keys(password_result)
    passw2 = driver.find_element_by_id('passwd_2')
    passw2.send_keys(password_result)
    
    mail_coll = "This is your username: " + args.firstname + '.' + args.lastname + '@vfemail.net' + "\n" + "This is your password : " + password_result
    mail_doc = open('mail.txt','w')
    mail_doc.write(str(mail_coll))
    mail_doc.close()




