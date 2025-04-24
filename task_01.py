"""Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель, використовуючи з'єднувачі, у порядку, який призведе до найменших витрат. Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів. Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати."""

import heapq


def min_cost_to_connect_cables(cables):
    # Transform the list into a min-heap in O(n) time
    heapq.heapify(cables)
    total_cost = 0

    # Continue until only one cable remains
    while len(cables) > 1:
        # Remove and return the smallest element in O(log n)
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Cost of connection
        current_cost = first + second
        total_cost += current_cost

        # Push combined cable back into heap
        heapq.heappush(cables, current_cost)

    return total_cost


# Function test
cables1 = [1]
cables2 = [1, 2, 3]
cables3 = [8, 4, 6, 12]
cables4 = [48, 10, 13, 19, 32, 23, 12, 11]

print(min_cost_to_connect_cables(cables1))
print(min_cost_to_connect_cables(cables2))
print(min_cost_to_connect_cables(cables3))
print(min_cost_to_connect_cables(cables4))
