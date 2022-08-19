# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python

# import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDRGID_API_KEY = (
    "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"
)

html_content_path = "sendgrid/sendgrid_template.html"

with open(html_content_path, "r", encoding='utf-8') as f:
    email_template = f.read()

message = Mail(
    # from_email='from_email@example.com',
    from_email="mail@olehkharkevych.com",
    # to_emails='to@example.com',
    to_emails="oleg.kharkevich@gmail.com",
    # subject='Sending with Twilio SendGrid is Fun',
    subject="Welcome to Smedesk",
    # html_content='<strong>and easy to do anywhere, even with Python</strong>'
    html_content=email_template
)

try:
    # sg = SendGridAPIClient(os.environ.get("SENDRGID_API_KEY"))
    sg = SendGridAPIClient(api_key=SENDRGID_API_KEY)
    response = sg.send(message)

    print(response.status_code)
    print(response.body)
    print(response.headers)

except Exception as e:
    # print(e.message)
    print(e)

# ###1st Output:###
# 202
# b''
# Server: nginx
# Date: Fri, 19 Aug 2022 15:45:26 GMT
# Content-Length: 0
# Connection: close
# X-Message-Id: aipKi6FdSti3zcjyagFd_g
# Access-Control-Allow-Origin: https://sendgrid.api-docs.io
# Access-Control-Allow-Methods: POST
# Access-Control-Allow-Headers: Authorization, Content-Type, On-behalf-of,
# x-sg-elas-acl
# Access-Control-Max-Age: 600
# X-No-CORS-Reason: https://sendgrid.com/docs/Classroom/Basics/API/cors.html
# Strict-Transport-Security: max-age=600; includeSubDomains

# ###2nd Output (with template)###
# 202
# b''
# Server: nginx
# Date: Fri, 19 Aug 2022 18:51:15 GMT
# Content-Length: 0
# Connection: close
# X-Message-Id: Km9eJ6bbQ6a46u8_VfB5Bg
# Access-Control-Allow-Origin: https://sendgrid.api-docs.io
# Access-Control-Allow-Methods: POST
# Access-Control-Allow-Headers: Authorization, Content-Type, On-behalf-of,
# x-sg-elas-acl
# Access-Control-Max-Age: 600
# X-No-CORS-Reason: https://sendgrid.com/docs/Classroom/Basics/API/cors.html
# Strict-Transport-Security: max-age=600; includeSubDomains
