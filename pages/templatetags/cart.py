from django import template

register = template.Library ()


@register.filter (name='is_in_cart')
def is_in_cart(items, cart):
    keys = cart.keys ()
    for id in keys:
        if int (id) == items.id:
            return True
    return False;


@register.filter (name='cart_quantity')
def cart_quantity(items, cart):
    keys = cart.keys ()
    for id in keys:
        if int (id) == items.id:
            return cart.get (id)
    return 0;


@register.filter (name='price_total')
def price_total(items, cart):
    return items.itemprice * cart_quantity (items, cart)


@register.filter (name='total_cart_price')
def total_cart_price(items, cart):
    sum = 0;
    for i in items:
        sum += price_total (i, cart)

    return sum
