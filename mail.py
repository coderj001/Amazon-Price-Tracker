import os,json
from json import JSONDecodeError,JSONDecoder,JSONEncoder
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

class Mail:
    def __init__(self):
        pass
    def insertInfo(self):
        if os.path.exists("mail"):
            with open("mail","rb") as fs:
                js=fs.read().decode('utf-8')
                data=json.loads(js)
                return data
        else:
            with open("mail","wb") as fs:
                data={'email':input('Email: '),
                'pass':input('Password: ')}
                fs.write(json.dumps(data).encode())
                return data
    def checkInfo(self):
        print('''
        1. Keep Previous Details
        2. Change Details
        3. Exit
        ''')
        try:
            ch=input('Enter: ')
            if ch == '1':
                data=self.insertInfo()
                return data
            elif ch == '2':
                print('Deleting previous details.....')
                os.remove('mail')
                data=self.insertInfo()
                return data
            elif ch == '3':
                print('Exit')
                return None
            else:
                print('invalid choice.')
        except (JSONDecodeError,KeyboardInterrupt):
            print("Error due to keyboard interaption.")
            print("Sorry to tell you that your previous details about email and passwd may be deleted.")
    def SentMail(self,info):
        data=self.insertInfo()
        if not data == None:
            try:
                sender_email = data['email']
                receiver_email = data['email']
                password=data['pass']
                img_data=open(info['screenshort'], 'rb').read()
                message = MIMEMultipart("alternative")
                message["Subject"] = "Due to change in price on {}".format(info['product_name'])
                message["From"] = sender_email
                message["To"] = receiver_email
                image = MIMEImage(img_data, name=os.path.basename(info['screenshort']))
                html="""
                    <html>
                        <body>
                            <p>Hi,There Your Product: {} Has A Change In Price.</p>
                            <h3><b>Price: </b> {}</h3>
                            <a href='{}'> Click Here </a>
                        </body>
                    </html>
                """.format(info['product_name'],info['price'],info['url'])
                p1=MIMEText(html, "html")
                message.attach(p1)
                message.attach(image)
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(
                        sender_email, receiver_email, message.as_string()
                    )
                print('Sent...')
            except Exception as e:
                print('Error: ',e)
                print('Go to link: https://www.google.com/settings/security/lesssecureapps')
                print('Sign to acct. and enable less secure')