def knapsack_2_approx(items, capacity):
    operation_count = 0

    # Сортировка элементов по убыванию стоимости на единицу веса
    sorted_items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)
    operation_count += len(items) * (len(items) - 1) // 2  # операции сортировки

    # Жадное добавление элементов в рюкзак
    total_weight = 0
    total_value = 0
    for weight, value in sorted_items:
        operation_count += 1  # операция сравнения
        if total_weight + weight <= capacity:
            total_weight += weight
            total_value += value
            operation_count += 2  # операции сложения

    return total_value, operation_count

items = [(10, 60), (20, 100), (30, 120), (40, 240), (50, 300), (60, 360), (70, 420), (80, 500), (90, 540), (100, 600)]
capacity = 250

result, operations = knapsack_2_approx(items, capacity)
print("Max cost (2-approx):", result)
print("Count operations:", operations)