import smtplib

print(">Making Connection to server.")
#Begin server info
server = smtplib.SMTP("smtp.gmail.com", 587)
print(">Connection has made to server.")

server.starttls()
print(">Setting up account information.")

#Get user account information
account = str(raw_input("Enter Google Talk account username: (Example: username123)"))
password = str(raw_input("Enter Google Talk account password: (Example: abc123)"))
server.login(account+'@gmail.com', password)

print(">Setting up message to be sent.")
#Get number to text:
number = int(raw_input("Enter a number to text. (Example: 1234567890) "))

#Get SMS gateway:
gateway = str(raw_input("Enter SMS Gateway domain. (AT&T: txt.att.net, T-Mobile: tmomail.net) "))

#Get message from user:
message = str(raw_input("Enter a message: "))

#Send message
server.sendmail('', number+'@'+gateway, message)
print(">Message sent!")
