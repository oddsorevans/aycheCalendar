import smtplib
import random
from connectionStrings import emailPasswd

def sendEmail(address):
    twoFactor = random.randint(100000,999999) #random 6 digit

    #create session with email
    session = smtplib.SMTP("smtp.gmail.com", 587)
    session.starttls()
    session.login("aychecalendar@gmail.com", emailPasswd)
    message = f"your 2-factor verification code is {twoFactor}"
    session.sendmail("aychecalendar@gmail.com", address, message)
    session.quit()

    return twoFactor

    # check = int(input("Enter 2-factor verification code: "))
    # if check == twoFactor:
    #     print("That is correct!")
    # else:
    #     print("Wrong you dumb dumb")

sendEmail(input("Enter email address: "))