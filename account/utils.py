from django.core.mail import send_mail

from decouple import config as config_settings


HOST = 'localhost:8000'     # change after deploy


def send_confirmation_email(user, code):
    subject = 'Активация аккаунта в Poncho!'
    activation_link = f'http://{HOST}/api/v1/account/activate/{code}/'

    html_message = f"""
        <html>
            <body>
                <p>Здравствуйте, {user}!</p>
                <p>Для активации вашего аккаунта перейдите по следующей ссылке:</p>
                <a href="{activation_link}">{activation_link}</a>
                <p>Ссылка действительна только один раз.</p>
            </body>
        </html>
    """

    send_mail(
        subject,
        '',
        config_settings('EMAIL_HOST_USER'),
        [user],
        html_message=html_message,
        fail_silently=False,
    )
