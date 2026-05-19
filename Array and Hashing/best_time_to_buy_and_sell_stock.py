def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        current_price = prices[i]

        profit = current_price - min_price

        if profit > max_profit:
            max_profit = profit

        if current_price < min_price:
            min_price = current_price

    return max_profit

prices = [7,1,5,3,6,4]

print(maxProfit(prices))