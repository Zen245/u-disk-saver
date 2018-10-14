import smtplib

from email.mime.text import MIMEText

from email.mime.image import MIMEImage

from email.mime.multipart import MIMEMultipart

from email.mime.application import MIMEApplication 

#调用smtplib模块，其中MIMEText是文档
#MIMEImage是图片，MIMEMultipart是多类型文件

        


fromaddr = 'test223@163.com'

password = 'test223'

toaddrs = ['test223@163.com']

         

content = '[SUCCESS] We already send you the file. Have a good day.'
content += '\n                              ---Greetings from T**3'

textApart = MIMEText(content)#邮件正文，使用\n换行

         

#发送zip格式文件         

zipFile = 'copy_data.zip'

zipApart = MIMEApplication(open(zipFile, 'rb').read())

zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

            

         
#将文字与附件带入m开始发送
                
m = MIMEMultipart()

m.attach(textApart)
m.attach(zipApart)

#邮件标题                
m['Subject'] = '[SUCCESS]'
      

try:

        server = smtplib.SMTP('smtp.163.com')

        server.login(fromaddr,password)

        server.sendmail(fromaddr, toaddrs, m.as_string())

        server.quit()

except smtplib.SMTPException as e:

        pass

sign_4 = True
