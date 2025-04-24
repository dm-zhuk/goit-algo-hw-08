"""Дано k відсортованих списків цілих чисел. Ваше завдання — об'єднати їх у один відсортований список. Тепер при виконанні завдання ви повинні використати мінімальну купу для ефективного злиття кількох відсортованих списків в один відсортований список. Реалізуйте функцію merge_k_lists, яка приймає на вхід список відсортованих списків та повертає відсортований список.

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
Відсортований список: [1, 1, 2, 3, 4, 4, 5, 6]
"""

import heapq


def merge_k_lists(lists):
    result = []
    heap = []
    for i, list in enumerate(lists):
        if list:
            heapq.heappush(heap, (list[0], i, 0))

    while heap:
        val, list_idx, val_idx = heapq.heappop(heap)
        result.append(val)

        if val_idx + 1 < len(lists[list_idx]):
            next_val_idx = val_idx + 1
            heapq.heappush(
                heap, (lists[list_idx][next_val_idx], list_idx, next_val_idx)
            )

    return result


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
