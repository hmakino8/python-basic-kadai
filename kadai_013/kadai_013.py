price_tax_ex = 125
tax = 1.1


def get_price_with_tax(price_tax_ex: int) -> int:
    tax = 2
    if price_tax_ex < 0:
        return -1

    price_tax_in = price_tax_ex * tax
    return price_tax_in


print(get_price_with_tax(price_tax_ex))
