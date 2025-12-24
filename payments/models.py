from django.db import models


class Item(models.Model):
    CURRENCY_USD = "usd"
    CURRENCY_EUR = "eur"

    CURRENCY_CHOICES = [
        (CURRENCY_USD, "USD"),
        (CURRENCY_EUR, "EUR"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField(
        help_text="Price in smallest currency unit (e.g. 100 cents for USD)"
    )
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default=CURRENCY_EUR,
    )

    def display_price(self) -> str:
        return f"{self.price / 100:.2f}"

    def __str__(self) -> str:
        return self.name
