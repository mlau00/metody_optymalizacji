import sys

from knapsack import knapsack


# Metodą programowania dynamicznego rozwiązać problem plecakowy decyzyjny przy wskazanych danych wejściowych
class Item:
    def __init__(self, position, price, weight):
        self.position = position
        self.price = price
        self.weight = weight

    def __str__(self):
        return f'{self.position} ---> {self.price}, {self.weight}'


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
    # w_max = 30
    w_max = 30

    # size = [21, 11, 15, 9, 34, 25, 41, 52]
    # weight = [22, 12, 16, 10, 35, 26, 42, 53]
    # capacity = 100
    # res1 = knapsack(size, weight).solve(capacity)
    #
    # print("\nFor max_weight =", capacity)
    # print("Last value:", res1)

    list_items = []

    item1 = Item(1, 9, 10)
    item2 = Item(2, 9, 7)
    item3 = Item(3, 6, 11)
    item4 = Item(4, 7, 8)
    item5 = Item(5, 9, 8)
    item6 = Item(6, 11, 9)

    # item1 = Item(1, 21, 22)
    # item2 = Item(2, 11, 12)
    # item3 = Item(3, 15, 16)
    # item4 = Item(4, 9, 10)
    # item5 = Item(5, 34, 35)
    # item6 = Item(6, 25, 26)
    # item7 = Item(7, 41, 42)
    # item8 = Item(8, 52, 53)

    # for item in [item1, item2, item3, item4, item5, item6]:
    #     list_items.append(item)

    # item1 = Item(1, 75, 7)
    # item2 = Item(2, 150, 8)
    # item3 = Item(3, 250, 6)
    # item4 = Item(4, 35, 4)
    # item5 = Item(5, 10, 3)
    # item6 = Item(6, 100, 9)

    for item in [item1, item2, item3, item4, item5, item6]:
        list_items.append(item)

    print_items(list_items, 'Initial list:')
    initial_list = list_items.copy()

    table = []
    test = []

    for item in range(len(initial_list) + 1):
        for i in range(w_max + 1):
            test.append(0)
        table.append(test.copy())
        test.clear()

    for i in range(1, len(initial_list) + 1):
        for j in range(1, w_max + 1):
            if initial_list[i - 1].weight <= j:
                table[i][j] = initial_list[i - 1].price
                table[i][j] = max(table[i - 1][j],
                                  table[i - 1][j - initial_list[i - 1].weight] + initial_list[i - 1].price)
            if table[i - 1][j] > table[i][j]:
                table[i][j] = table[i - 1][j]

    row = 0
    column = 0
    positions = []
    for i in range(1, len(initial_list) + 1):
        if table[len(initial_list) - row][w_max - column] <= table[len(initial_list) - row - 1][w_max - column]:
            positions.append(0)
        else:
            positions.append(1)
            column = initial_list[len(initial_list) - i].weight
        row = row + 1

    positions.reverse()

    last_value = table[len(initial_list)][w_max]

    print(f'Last value: {last_value}')

    print('Vector:', '[', *positions, ']')


if __name__ == '__main__':
    plecakowy()
