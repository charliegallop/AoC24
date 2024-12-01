from collections import Counter
from pathlib import Path


def read_lists_file(data_path: Path) -> tuple[list[int], list[int]]:
    data = data_path.open("r").read().splitlines()
    list1 = []
    list2 = []
    for line in data:
        item1, item2 = line.split("   ")
        list1.append(int(item1))
        list2.append(int(item2))

    return list1, list2

def calc_total_diff(list1: list[int], list2: list[int]) -> int:
    list1.sort()
    list2.sort()
    return sum([abs(a - b) for a, b in zip(list1, list2)])

def calc_similarity_score(list1: list[int], list2: list[int]) -> int:
    counts = Counter(list2)
    return sum([a * counts[a] for a in list1])

if __name__ == "__main__":
    data_path = Path("./data.txt")

    print("####   Part One ####")

    list1, list2 = read_lists_file(data_path)
    total_diff = calc_total_diff(list1, list2)
    print(f"Sum of total_diff: {total_diff}")


    print("####   Part Dos ####")

    data_path2 = Path("./data_2.txt")

    list1, list2 = read_lists_file(data_path2)
    similarity_score = calc_similarity_score(list1, list2)

    print(f"Similarirty score: {similarity_score}")
