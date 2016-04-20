from django.template.loader import render_to_string
from django.core.mail.message import EmailMessage
from celery import shared_task


@shared_task
def send_activation_mail(user_id, key):
    from .models import User
    user = User.objects.get(id=user_id)
    context = {
         'username': user.username, 'security_key': key
    }
    html_content = render_to_string('massage.html', context)
    msg = EmailMessage('submit registration', html_content, 'Flancern@inbox.ru',
                       [user.email])
    msg.content_subtype = "html"
    msg.send()
