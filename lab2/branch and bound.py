def branch_and_bound(capacity, items):
    items = sorted(items, key=lambda x: x[1]/x[0], reverse=True)
    n = len(items)
    max_value = 0
    node = (0, 0, capacity, 0)
    stack = [node]
    operations = 0
    while stack:
        i, value, room, bound = stack.pop()
        if i == n:
            if value > max_value:
                max_value = value
            continue
        if items[i][0] <= room:
            operations += 1
            with_i = (i+1, value+items[i][1], room-items[i][0], bound)
            if with_i[1]+with_i[3] > max_value:
                stack.append(with_i)
        without_i = (i+1, value, room, bound+items[i][1])
        if without_i[3] > max_value:
            stack.append(without_i)
        operations += 1
    return max_value, operations


capacity = 165
items = [(23, 92), (31, 57), (29, 49), (44, 68), (53, 60), (38, 43), (63, 67), (85, 84), (89,87), (82, 72)]
result, operations = branch_and_bound(capacity, items)

print(f"Maximum value: {result}")
print(f"Number of operations: {operations}")
