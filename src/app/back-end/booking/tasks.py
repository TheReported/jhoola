import stripe
from celery import shared_task
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


@shared_task
def booking_created(success_url, cancel_url, metadata, line_items):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        metadata=metadata,
        success_url=success_url,
        cancel_url=cancel_url,
    )
    return session.url
