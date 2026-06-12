from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import send_mail


@receiver(post_save,sender=User)
def send_activation_mail(sender,instance,created,**kwargs):
    if created:
        token=default_token_generator.make_token(instance)
        activation_url=f'{settings.FRONTEND_URL}/users/activate/{instance.id}/{token}/'
        subject='Active Your Account'
        message=f'Hi {instance.username} Please Active Your account by click link {activation_url}\n\n Thank You'
        mail_list=[instance.email]

        try:
            send_mail(subject,message,settings.EMAIL_HOST_USER,mail_list)
        except Exception as e:
            print(f'Fail to send Email to {instance.email}: {str(e)}')