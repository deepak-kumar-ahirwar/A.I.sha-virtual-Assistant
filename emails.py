import smtplib

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourEmailId', 'password')
    server.sendmail('yourEmailId', to, content)
    server.close()

def sendMail():
    dict={
        "friendName":"friendEmailID",
        "nextFriendName":"EmailID"
    }