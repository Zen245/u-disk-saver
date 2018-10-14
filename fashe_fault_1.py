import smtplib

from email.mime.text import MIMEText

from email.mime.image import MIMEImage

from email.mime.multipart import MIMEMultipart

from email.mime.application import MIMEApplication 



        


fromaddr = 'test223@163.com'

password = 'test223'

toaddrs = ['test223@163.com']

         

content = 'Sorry, there is a fault with the file. [FileNotFoundError]'

textApart = MIMEText(content)

         

               



            

         

                
m = MIMEMultipart()

m.attach(textApart)


                
m['Subject'] = '[FileNotFoundError]'

         

try:

        server = smtplib.SMTP('smtp.163.com')

        server.login(fromaddr,password)

        server.sendmail(fromaddr, toaddrs, m.as_string())

        server.quit()

except smtplib.SMTPException as e:

        pass


