def bubble_sort(items: list[int]):
    for _ in range(len(items)):
        for i in range(len(items) - 1):
            a, b = items[i], items[i + 1]
            if a > b:
                items[i], items[i + 1] = items[i + 1], items[i]
    return items

if __name__ == "__main__":
    payload = [64, 56, 78, 114, 22, 45, 1, 23, 54]
    print(payload)
    print(bubble_sort(payload))
