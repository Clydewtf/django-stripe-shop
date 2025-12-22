from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.conf import settings

from .models import Item
from .services.stripe_service import create_checkout_session


def item_detail(request, item_id: int):
    item = get_object_or_404(Item, id=item_id)

    return render(
        request,
        "item_detail.html",
        {"item": item, "stripe_public_key": settings.STRIPE_PUBLIC_KEY},
    )


def buy_item(request, item_id: int):
    item = get_object_or_404(Item, id=item_id)

    success_url = request.build_absolute_uri(
        reverse("item_detail", args=[item.id])
    )
    cancel_url = success_url

    session_id = create_checkout_session(
        item=item,
        success_url=success_url,
        cancel_url=cancel_url,
    )

    return JsonResponse({"session_id": session_id})
