# import smtplib
#
# from email.mime.text import MIMEText
#
# msg = MIMEText('Testing some Mailgun awesomness')
# msg['Subject'] = "Bingo!"
# msg['From']    = 'przypomnienia@ubezpieczenia-magro.pl'
# msg['To']      = "robert.patryk.grzelak@gmail.com"
#
# s = smtplib.SMTP('ubezpieczenia-magro.home.pl:25')
#
# s.login('przypomnienia@ubezpieczenia-magro.pl', 'dsrhsR3P')
# s.sendmail(msg['From'], msg['To'], msg.as_string())
# s.quit()


import smtplib
from email.mime.text import MIMEText

msg = MIMEText('10.04.2020 g.10')
msg['Subject'] = 'Wolny termin w "Piotr i Paweł"'
msg['From'] = 'robert.patryk.grzelak@gmail.com'
msg['To'] = "robert.patryk.grzelak@gmail.com"

s = smtplib.SMTP('smtp.mailgun.org', 587)

s.login(os.environ.get("EMAIL_HOST_USER"),
        os.environ.get("EMAIL_HOST_PASSWORD"))
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()
