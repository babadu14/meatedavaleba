from django.core.management import BaseCommand
from  shop.models import Item, Category, Tag, Image

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        categories = Category.objects.with_item_count()
        for category in categories:
            print(category.name, category.items_count)

            
        items = Item.objects.with_tag_count()
        for item in items:
            print(item.name, item.tags_count)

        tags = Tag.objects.popular_tags(2)
        for tag in tags:
            print(tag.name, tag.items_count)