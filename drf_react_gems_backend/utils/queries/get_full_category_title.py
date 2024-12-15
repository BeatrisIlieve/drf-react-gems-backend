from django.db.models import (
    Case,
    When,
    Value,
    CharField,
)


def get_full_category_title():
    return Case(
        When(product__category__title="E", then=Value("Earring")),
        When(product__category__title="B", then=Value("Bracelet")),
        When(product__category__title="N", then=Value("Necklace")),
        When(product__category__title="R", then=Value("Ring")),
        When(product__category__title="C", then=Value("Charm")),
        When(product__category__title="P", then=Value("Pendant")),
        default=Value("Unknown Category"),
        output_field=CharField(),
    )
