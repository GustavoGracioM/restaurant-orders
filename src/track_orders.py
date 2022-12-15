from src.analyze_log import (
    get_max,
    get_min,
    infos_client,
    infos_requests,
)


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def add_new_order(self, customer, order, day):
        self.list.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        orders = infos_client(self.list, customer)[0]
        return get_max(orders)[0]

    def get_never_ordered_per_customer(self, customer):
        order = set(infos_requests(self.list)[0].keys())
        order_customer = set(infos_client(self.list, customer)[0].keys())
        return order_customer.symmetric_difference(order)

    def get_days_never_visited_per_customer(self, customer):
        days = set(infos_requests(self.list)[1].keys())
        days_customer = set(infos_client(self.list, customer)[1].keys())
        return days_customer.symmetric_difference(days)

    def get_busiest_day(self):
        days = infos_requests(self.list)[1]
        return get_max(days)[0]

    def get_least_busy_day(self):
        days = infos_requests(self.list)[1]
        return get_min(days)[0]
