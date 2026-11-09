prices = {"bread": 2.5, "milk": 3.0, "cheese":9.0}
def print_menu(prices):
    """Print each item and its price from he dictionary."""
    for item, price in prices.items():
        print(f"{item}: {price}")
def cart_total(prices,cart):
    """Return the total cost items in the cartthat exist in prices."""
    total = 0.0
    for item,quantity in cart.items():
        if item in prices:
         total += prices[item] * quantity
    return total
def cheapest(prices):
    """Return the name of the cheapest item without using min()."""
    if not prices:
        return None

    cheapest_item = None
    lowest_price = float('inf')
    for item, price in prices.items():
        
        if price < lowest_price:
            lowest_price = price
            cheapest_item = item
    return cheapest_item
print_menu(prices)
cart = {"bread": 2, "cheese": 1, "apples": 3}
print(cart_total(prices, cart))
print(cart_total(prices, {}))
print(cheapest(prices))
print(cheapest({"tea": 4.0, "coffee": 4.0}))
