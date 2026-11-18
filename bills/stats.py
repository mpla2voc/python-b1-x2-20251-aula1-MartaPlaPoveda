from .item import Bill, Product
from .entity import Buyer, Seller



class OrderType:
    # Do not change this enum
    ASC = 0
    DES = 1


class Statistics:
    def __init__(self, bills: list[Bill]):
        # Do not change this method
        self.bills = bills

    def find_top_sell_product(self) -> (Product, int):
        products_count = {}

        for bill in self.bills:
            for product in bill.products:
                products_count[product] = products_count.get(product, 0) + 1

        top_product = max(products_count, key=products_count.get)

        return (top_product, products_count[top_product])

    def find_top_two_sellers(self) -> list:
        sellers_total = {}

        for bill in self.bills:
            sellers_total[bill.seller] = (sellers_total.get(bill.seller, 0) + bill.calculate_total())

        ordered_sellers = sorted(
            sellers_total.items(),
            key=lambda item: item[1],
            reverse=True
            )

        return [seller for seller, total in ordered_sellers[:2]]

    def find_buyer_lowest_total_purchases(self) -> (Buyer, float):
        lowest_total = {}

        for bill in self.bills:
            lowest_total[bill.buyer] = (lowest_total.get(bill.buyer, 0) + bill.calculate_total())

        buyer = min(lowest_total, key=lowest_total.get)

        return (buyer, lowest_total[buyer])

    def order_products_by_tax(self, order_type: OrderType) -> tuple:
        products_tax = {}

        for bill in self.bills:
            for product in bill.products:
                products_tax[product] = product.calculate_total_taxes()

        if order_type == OrderType.ASC:
            ordered_products = sorted(
                products_tax.items(),
                key=lambda item: item[1]
                )
        else:
            ordered_products = sorted(
                products_tax.items(),
                key=lambda item: item[1],
                reverse=True
                )

        return ordered_products

    def show(self):
        # Do not change this method
        print("Bills")
        for bill in self.bills:
            bill.print()
