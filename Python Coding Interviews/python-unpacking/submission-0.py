from typing import List, Tuple


from typing import List

def sum_3_integers(triplet: List[int]) -> int:
    total = 0

    for num in triplet:
        total += num

    return total


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    multiply = 1

    for num in box_dimensions:
        multiply *= num

    return multiply


    pass
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
