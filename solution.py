#!/usr/bin/env python3
import numpy as np


def knapsack(company_data, limit_amount):
    """
    The following solution is a dynamic programming algorithm to a well-known 0/1 Knapsack problem.
    The code has adapted to the solution of a supplier trying to maximize profit by picking buyers.
    NOTE: This code will change the 'picked' field of 'company_data" field. Make a copy if you don't want this.
    :param company_data: dictionary/object that has information about each buyer's amount, price and picked or not
    :param limit_amount: the amount of resources that the supplier has
    :return: the maximum profit that the supplier can make with given list of buyers and limited amount of resources
    """
    cache = np.zeros((len(company_data) + 1, limit_amount + 1), dtype=np.int)
    for company in range(len(data) + 1):
        for amount in range(limit_amount + 1):
            # Using 0 company or having 0 resource
            if (company == 0) | (amount == 0):
                cache[company][amount] = 0
            # If we can use this company amount, try to use it if it produces max
            elif data[company - 1]['amount'] <= amount:
                # Take the maximum between using this company and a combination of companies before it and less
                # resources, and not using this company but  a combination of companies before it with the resources
                cache[company][amount] = max(
                    data[company - 1]['price'] + cache[company - 1][amount - data[company - 1]['amount']],
                    cache[company - 1][amount]
                )
            # If we can't use the company amount, use a combination of companies before it with the resources
            else:
                cache[company][amount] = cache[company - 1][amount]

    # Traceback the solution
    left_over = limit_amount

    # Starting backward (trying to use all companies with the given amount of resources)
    for company in reversed(range(1, len(company_data)+1)):
        # If the combination of companies before this company produces the same max of profit, we don't use this company
        # Otherwise, we use this company. Subtract the amount of resources that we'd sell to them away.
        if (left_over > 0) and (cache[company][left_over] != cache[company-1][left_over]):
            company_data[company-1]['picked'] = True
            left_over -= company_data[company-1]['amount']
        else:
            company_data[company-1]['picked'] = False
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
        print("Maximum profit with {0} unit of resources is: {1}".format(max_amount, max_profit))
        print("The following companies has been picked:")
        print("Amount\tPrice")
        for company in data:
            if company['picked']:
                print("%s\t%s" % (company['amount'], company['price']))
