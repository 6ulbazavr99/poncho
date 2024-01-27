from django.core.mail import send_mail

from decouple import config as config_settings
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created

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


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    subject = 'Сброс пароля в Poncho!'
    message = (
        f'Здравствуйте!\n\n'
        f'Для сброса пароля на вашем аккаунте в Poncho! вам необходимо ввести следующий код:\n'
        f'\n'
        f'{reset_password_token.key}\n\n'
        f'Если вы не запрашивали сброс пароля, проигнорируйте это письмо.\n'
        f'С наилучшими пожеланиями,\n'
        f'Команда Poncho!'
    )
    from_email = config_settings('EMAIL_HOST_USER')
    to_email = reset_password_token.user.email

    send_mail(subject, message, from_email, [to_email], fail_silently=False)
