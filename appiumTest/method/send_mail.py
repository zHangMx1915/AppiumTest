import smtplib
from email.mime.text import MIMEText
import re
from file_tools import operation_json
"""发送邮件"""


def get_data():
    return operation_json.get_config('email')


class SendEmail:

    def __init__(self):
        self.data = get_data()
        self.send_users = self.data.get("send_user")
        self.passwords = self.data.get("password")
        self.user_list = self.data.get("Receipt")        # 收件人邮箱
        self.email_user = []

    # 发送邮件
    def send_email(self, log_text):
        for i in self.user_list:
            name_str = r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$'
            if re.match(name_str, i):
                self.email_user.append(i)
            else:
                print('Error！请检查接收的邮箱账号!你这样写:%s' % i)
        email_host = 'smtp.163.com'
        user = 'ZhangMx' + '<' + self.send_users + '>'
        message = MIMEText(log_text, _subtype='plain', _charset='utf-8')
        message['Subject'] = 'App测试通知邮件'
        message['From'] = user
        message['To'] = ';'.join(self.email_user)
        server = smtplib.SMTP()
        server.connect(host=email_host)
        server.login(self.send_users, self.passwords)
        server.sendmail(user, self.email_user, message.as_string())
        server.close()
