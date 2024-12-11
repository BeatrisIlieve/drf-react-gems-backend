from django.db.models import (
    Case,
    When,
    Value,
    BooleanField,
)


def get_stock_status_per_size():
    return Case(
        When(quantity=0, then=Value(True)),
        default=Value(False),
        output_field=BooleanField(),
    )
