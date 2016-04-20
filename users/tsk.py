from django.template.loader import render_to_string
from django.core.mail.message import EmailMessage
from models import SecretKey


def send_activation_mail(user):
    key = SecretKey.objects.get_or_create(user=user).secretkey
    context = {'username': user.username, 'security_key': key}
    html_content = render_to_string('massage.html', context)
    msg = EmailMessage('submit registration', html_content, 'Flancern@inbox.ru', [user.email])
    msg.content_subtype = "html"
    msg.send()
