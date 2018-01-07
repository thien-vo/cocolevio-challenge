import numpy as np


def knapsack(company_data, limit_amount):
    cache = np.zeros((len(company_data) + 1, limit_amount + 1), dtype=np.int)
    for company in range(len(data) + 1):
        for amount in range(limit_amount + 1):
            # Using 0 company or having 0 resource
            if (company == 0) | (amount == 0):
                cache[company][amount] = 0
            # If we can use this company weight, try to use it if it produces max
            elif data[company - 1]['amount'] <= amount:
                # compare the max of using
                cache[company][amount] = max(
                    data[company - 1]['price'] + cache[company - 1][amount - data[company - 1]['amount']],
                    cache[company - 1][amount]
                )
            else:
                cache[company][amount] = cache[company - 1][amount]

    return cache[-1][-1]


if __name__ == "__main__":
    with open('input.txt') as f:
        next_line = f.readline().split()
        max_amount = int(next_line[0])
        data = []
        next_line = f.readline().split()
        while len(next_line) > 0:
            data.append(dict(amount=int(next_line[0]), price=int(next_line[1]), picked=False))
            next_line = f.readline().split()
        max_profit = knapsack(data, max_amount)
        print("Maximum profit with {0} amount of resources is: {1}".format(max_amount, max_profit))