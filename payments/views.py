from django.shortcuts import get_object_or_404, render
from .models import Item


def item_detail(request, item_id: int):
    item = get_object_or_404(Item, id=item_id)

    return render(
        request,
        "item_detail.html",
        {
            "item": item,
        },
    )
