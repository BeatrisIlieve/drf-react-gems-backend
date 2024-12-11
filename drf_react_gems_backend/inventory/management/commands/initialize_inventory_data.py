import os
import django
from django.core.management.base import (
    BaseCommand,
)


from drf_react_gems_backend.product.models import (
    Product,
)

from drf_react_gems_backend.inventory.models import (
    Inventory,
)


class Command(BaseCommand):
    help = "Initialize data for your Django app"

    def handle(self, *args, **options):
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "drf_react_gems_backend.settings"
        )
        django.setup()

        self.stdout.write(self.style.SUCCESS("Starting data initialization..."))

        self.bulk_create_inventory()

        self.stdout.write(
            self.style.SUCCESS("Data initialization completed successfully.")
        )

    def bulk_create_inventory(self):
        products = Product.objects.all()

        Inventory.objects.bulk_create(
            [
                Inventory(quantity=3, product=products[0], size=4.05, price=43000.00),
                Inventory(quantity=3, product=products[0], size=4.98, price=44000.00),
                Inventory(quantity=3, product=products[0], size=5.86, price=45000.00),
                Inventory(quantity=3, product=products[1], size=4.05, price=43000.00),
                Inventory(quantity=3, product=products[1], size=4.98, price=44000.00),
                Inventory(quantity=3, product=products[1], size=5.86, price=45000.00),
                Inventory(quantity=3, product=products[2], size=4.05, price=43000.00),
                Inventory(quantity=3, product=products[2], size=4.98, price=44000.00),
                Inventory(quantity=3, product=products[2], size=5.86, price=45000.00),
                Inventory(quantity=3, product=products[3], size=15.02, price=34000.00),
                Inventory(quantity=3, product=products[3], size=17.08, price=35000.00),
                Inventory(quantity=3, product=products[3], size=19.03, price=36000.00),
                Inventory(quantity=3, product=products[4], size=15.02, price=34000.00),
                Inventory(quantity=3, product=products[4], size=17.08, price=35000.00),
                Inventory(quantity=3, product=products[4], size=19.03, price=36000.00),
                Inventory(quantity=3, product=products[5], size=15.02, price=34000.00),
                Inventory(quantity=3, product=products[5], size=17.08, price=35000.00),
                Inventory(quantity=3, product=products[5], size=19.03, price=36000.00),
                Inventory(quantity=3, product=products[6], size=40.64, price=55000.00),
                Inventory(quantity=3, product=products[6], size=43.18, price=56000.00),
                Inventory(quantity=3, product=products[6], size=45.71, price=57000.00),
                Inventory(quantity=3, product=products[7], size=40.64, price=55000.00),
                Inventory(quantity=3, product=products[7], size=43.18, price=56000.00),
                Inventory(quantity=3, product=products[7], size=45.71, price=57000.00),
                Inventory(quantity=3, product=products[8], size=40.64, price=55000.00),
                Inventory(quantity=3, product=products[8], size=43.18, price=56000.00),
                Inventory(quantity=3, product=products[8], size=45.71, price=57000.00),
                Inventory(quantity=3, product=products[9], size=4.07, price=23000.00),
                Inventory(quantity=3, product=products[9], size=4.09, price=24000.00),
                Inventory(quantity=3, product=products[9], size=5.05, price=25000.00),
                Inventory(quantity=3, product=products[10], size=4.07, price=23000.00),
                Inventory(quantity=3, product=products[10], size=4.09, price=24000.00),
                Inventory(quantity=3, product=products[10], size=5.05, price=25000.00),
                Inventory(quantity=3, product=products[11], size=4.07, price=23000.00),
                Inventory(quantity=3, product=products[11], size=4.09, price=24000.00),
                Inventory(quantity=3, product=products[11], size=5.05, price=25000.00),
                Inventory(quantity=3, product=products[12], size=2.73, price=8000.00),
                Inventory(quantity=3, product=products[13], size=2.73, price=8000.00),
                Inventory(quantity=3, product=products[14], size=2.73, price=8000.00),
                Inventory(quantity=3, product=products[15], size=40.64, price=47000.00),
                Inventory(quantity=3, product=products[15], size=43.18, price=48000.00),
                Inventory(quantity=3, product=products[15], size=45.71, price=49000.00),
                Inventory(quantity=3, product=products[16], size=40.64, price=47000.00),
                Inventory(quantity=3, product=products[16], size=43.18, price=48000.00),
                Inventory(quantity=3, product=products[16], size=45.71, price=49000.00),
                Inventory(quantity=3, product=products[17], size=40.64, price=47000.00),
                Inventory(quantity=3, product=products[17], size=43.18, price=48000.00),
                Inventory(quantity=3, product=products[17], size=45.71, price=49000.00),
            ]
        )
