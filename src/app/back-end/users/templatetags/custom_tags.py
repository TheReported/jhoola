from django import template

register = template.Library()


@register.simple_tag
def is_product_occupied(product_id, duration, occupied_products, date):
    date_products = occupied_products.get(date, [])
    return "disabled" if (product_id, duration) in date_products else ""
