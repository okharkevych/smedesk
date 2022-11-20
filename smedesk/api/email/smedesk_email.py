from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

FROM_EMAIL: str = 'mail@olehkharkevych.com'
SIGNUP_TEMPLATE: str = 'd-d2da6fb2ecb64c91b6ec1747c3b47d53'


def send_email(to_email: str, template: str):
    message: Mail = Mail(
        from_email=FROM_EMAIL,
        to_emails=to_email
    )
    message.template_id = template

    sg = SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
    response = sg.send(message=message)

    print(f'Response code: {response.status_code}')
    print(f'Response body: {response.body}')
    print(f'Response headers: {response.headers}')
    print('Message sent!')
