# You are given the following code:
"""Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:"""


class Order:
    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy

    def final_price(self):
        if self.discount_strategy is None:
            return self.price
        else:
            return self.discount_strategy(self)


def morning_discount(order):
    return order.price * 0.5


def elder_discount(order):
    return order.price * 0.1


# additional non-discount strategy
order_0 = Order(100)
assert order_0.final_price() == 100

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50

order_2 = Order(100, elder_discount)
assert order_2.final_price() == 10
