from django.db.models import (
    Case,
    When,
    Value,
    CharField,
)


def get_full_category_title():
    return Case(
        When(product__category__title="E", then=Value("Earrings")),
        When(product__category__title="B", then=Value("Bracelets")),
        When(product__category__title="N", then=Value("Necklaces")),
        When(product__category__title="R", then=Value("Rings")),
        default=Value("Unknown Category"),
        output_field=CharField(),
    )
