import stripe
from django.conf import settings
from payments.models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY


def create_checkout_session(item: Item, success_url: str, cancel_url: str) -> str:
    session = stripe.checkout.Session.create(
        mode="payment",
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": item.currency,
                    "unit_amount": item.price,
                    "product_data": {
                        "name": item.name,
                        "description": item.description,
                    },
                },
                "quantity": 1,
            }
        ],
        success_url=success_url,
        cancel_url=cancel_url,
    )

    return session.id
