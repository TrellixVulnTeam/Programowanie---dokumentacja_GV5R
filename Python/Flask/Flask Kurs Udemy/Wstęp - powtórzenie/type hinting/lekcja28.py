from typing import List

def list_avg(sequence: List[int]) -> float:
  return sum(sequence) / len(sequence)

print(list_avg([1, 45, 32]))