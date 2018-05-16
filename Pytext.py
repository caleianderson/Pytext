#! /usr/bin/python
import smtplib

email = ""#email for a gmail account here

password = ""#password for a gmail account here

#to get phone number
num = input("What phone number?")
#to hard code it
#num = ""#put phone number here


#to get service provider
sp = input("Which service provider \n 1.At&t \n 2.Tmobile \n 3.Verizon \n 4.Sprint \n 5.Cricket \n")
#to hard code it
#sp = ""#put number of service proveder here

if(sp == "1"):
    sp = "@txt.att.net"
elif(sp == "2"):
    sp = "@tmomail.net"
elif(sp == "3"):
    sp = "@vtext.com"
elif(sp == "4"):
    sp = "@messaging.sprintpcs.com"
elif(sp == "5"):
    sp = "@sms.cricketwireless.net"
else:
    print("Not a valid option please restart app")
    exit()

print("delivery adress: "+num+sp)

sentfrom = email
sentto = num+sp
msg = input("What would you like to say?\n")
email_text = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (sentfrom, sentto, " ", msg)

print("formatting done")


print("trying to connect")
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.ehlo()
print("connected")
server.login(email,password)
print("logged in")

server.sendmail(sentfrom,sentto,email_text)
server.quit()
print("text sent!")
