def fractional_knapsack(weights, profits, capacity):
    ratios = [(profits[i] / weights[i], weights[i], profits[i]) for i in range(len(weights))]
    ratios.sort(reverse=True)
    total_profit = 0
    selected_weights = [0] * len(weights)
    
    for ratio, weight, profit in ratios:
        if capacity == 0:
            break
        elif capacity >= weight:
            selected_weights[weights.index(weight)] = weight
            total_profit += profit
            capacity -= weight
        else:
            fraction = capacity / weight
            selected_weights[weights.index(weight)] = fraction * weight
            total_profit += fraction * profit
            capacity = 0
    
    return total_profit, selected_weights

print("Dhruv Varshney \nA2305221157")
num_items = int(input("Enter the number of items: "))
weights = []
profits = []
for i in range(num_items):
    weight = float(input("Enter the weight of item {}: ".format(i+1)))
    profit = float(input("Enter the profit of item {}: ".format(i+1)))
    weights.append(weight)
    profits.append(profit)


capacity = float(input("Enter the capacity of the knapsack: "))
max_profit, selected_weights = fractional_knapsack(weights, profits, capacity)
print("Maximum profit that can be obtained:", max_profit)
print("Selected weights:", selected_weights)