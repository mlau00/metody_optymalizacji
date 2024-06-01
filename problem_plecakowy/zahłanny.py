import sys


# Metodą zahłanną rozwiązać problem plecakowy ogólny przy wskazanych danych wejściowych
class Item:
    def __init__(self, position, price, weight, quantity):
        self.position = position
        self.price = price
        self.weight = weight
        self.quantity = quantity

    def __str__(self):
        return f'{self.position} ---> {self.price}, {self.weight}, {self.quantity}'


def print_items(items, title):
    print(title)
    for item in items:
        print(item.__str__())
    print('-----------')


def sort_by_price(list_items):
    list_items.sort(key=lambda item: item.price, reverse=True)
    return list_items


def sort_by_weight(list_items):
    list_items.sort(key=lambda item: (item.weight, -item.price), reverse=False)
    return list_items


def sort_by_profitability(list_items):
    list_items.sort(key=lambda item: item.price / item.weight, reverse=True)
    return list_items


def plecakowy():
    w_max = 100

    list_items = []

    item1 = Item(1, 9, 10, 6)
    item2 = Item(2, 9, 7, 6)
    item3 = Item(3, 6, 11, 7)
    item4 = Item(4, 7, 8, 6)
    item5 = Item(5, 9, 8, 5)
    item6 = Item(6, 11, 9, 4)

    # for item in [item1, item2, item3, item4, item5, item6]:
    #     list_items.append(item)

    # item1 = Item(1, 6, 6, 100)
    # item2 = Item(2, 4, 2, 100)
    # item3 = Item(3, 5, 3, 100)
    # item4 = Item(4, 7, 2, 100)
    # item5 = Item(5, 10, 3, 100)
    # item6 = Item(6, 2, 1, 100)

    for item in [item1, item2, item3, item4, item5, item6]:
        list_items.append(item)

    print_items(list_items, 'Initial list:')
    initial_list = list_items.copy()

    sorted_list_items = []

    user_input = input(
        'Which sort algorithm would you like to use?: 1 - Price sort, 2 - Weight sort, 3 - Profitability sort\n')

    if user_input == '1':
        sorted_list_items = sort_by_price(list_items)
        print_items(sorted_list_items, 'Price sort:')
    elif user_input == '2':
        sorted_list_items = sort_by_weight(list_items)
        print_items(sorted_list_items, 'Weight sort:')
    elif user_input == '3':
        sorted_list_items = sort_by_profitability(list_items)
        print_items(sorted_list_items, 'Profitability sort:')
    else:
        print('Invalid input')
        sys.exit()

    new_list = []
    current_weight = 0
    # index = 0
    condition = True
    while condition:
        if sorted_list_items.__len__() == 0:
            condition = False
        else:
            if current_weight < w_max:
                if sorted_list_items[0].quantity == 0:
                    sorted_list_items.pop(0)
                current_weight = current_weight + sorted_list_items[0].weight
                if current_weight <= w_max:
                    new_list.append(sorted_list_items[0])
                    sorted_list_items[0].quantity = sorted_list_items[0].quantity - 1
                else:
                    current_weight = current_weight - sorted_list_items[0].weight
                    sorted_list_items.pop(0)
            else:
                condition = False

    last_value = 0
    last_weight = 0
    for item in new_list:
        last_value = last_value + item.price
        last_weight = last_weight + item.weight

    print(f'Last value: {last_value}')
    print(f'Last weight: {last_weight}')
    print(f'Max weight: {w_max}')

    positions_list = []
    for item in initial_list:
        positions_list.append(0)

    for item in new_list:
        position = item.position - 1
        positions_list[position] = positions_list[position] + 1

    print('Vector:', '[', *positions_list, ']')


if __name__ == '__main__':
    plecakowy()
