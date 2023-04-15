from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Shop, Edition

"""
Update shop book to the newest edition and increment price of 5%.
"""


@receiver(post_save, sender=Edition)
def update_shop_book_edition_and_price(sender, instance: Edition, **kwargs):
    try:
        shop = Shop.objects.get(book=instance.book)
        if shop.edition.edition_number < instance.edition_number:
            shop.price *= 1.05
            shop.save()  # shop edition update is setted in Shop save() method.
    except:
        pass
