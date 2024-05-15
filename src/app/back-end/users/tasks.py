from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage


@shared_task
def user_created(data, hotel):
    subject = 'Welcome to Jhoola!'
    message = f"""
We are delighted to have you with us, {data["first_name"]} {data["last_name"]}! We hope your stay at our hotel will
be absolutely exceptional.

Username: {data["username"]}
Hotel name: {hotel}
Password : {data["password"]}

We hope you enjoy all the amenities and services we offer during your visit!
Please remember to keep your password secure at all times to ensure the safety of your account and personal information.
"""
    from_email = settings.EMAIL_HOST_USER
    to_email = [data['email']]
    mail_sent = send_mail(subject, message, from_email, to_email, fail_silently=False)
    return mail_sent


@shared_task
def contact_support(cd):
    subject = f'{cd["name"]} - {cd["subject"]}'
    message = cd['message']
    from_email = cd['email']
    to_email = [settings.EMAIL_HOST_USER]
    email = EmailMessage(
        subject,
        message,
        from_email,
        to_email,
        reply_to=[from_email],
    )

    email.send()
