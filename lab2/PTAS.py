def knapsack_ptas(items, capacity, epsilon):
    operation_count = 0
    n = len(items)

    # Масштабирование стоимостей
    max_value = max(items, key=lambda x: x[1])[1]
    k = int(epsilon * max_value / n)
    scaled_items = [(w, v // k) for w, v in items]
    operation_count += n  # Операции масштабирования

    # Инициализация таблицы динамического программирования
    V = sum(v for _, v in scaled_items)
    dp = [[0] * (V + 1) for _ in range(n + 1)]
    operation_count += (n + 1) * (V + 1)  # Операции инициализации

    for i in range(1, n + 1):
        for v in range(V + 1):
            w, scaled_v = scaled_items[i - 1]
            operation_count += 1  # Операция выбора элемента

            if v >= scaled_v:
                dp[i][v] = max(dp[i - 1][v], dp[i - 1][v - scaled_v] + w)
                operation_count += 1  # Операция сравнения и присваивания
            else:
                dp[i][v] = dp[i - 1][v]
                operation_count += 1  # Операция присваивания

    # Восстановление решения
    opt_value = 0
    for v in range(V + 1):
        if dp[n][v] <= capacity:
            opt_value = max(opt_value, v * k)
            operation_count += 1  # Операция сравнения и присваивания

    return opt_value, operation_count

items = [(10, 60), (20, 100), (30, 120), (40, 240), (50, 300), (60, 360), (70, 420), (80, 500), (90, 540), (100, 600)]
capacity = 250
epsilon = 0.5

result, operations = knapsack_ptas(items, capacity, epsilon)
print("Max cost (PTAS):", result)
print("Count operations:", operations)