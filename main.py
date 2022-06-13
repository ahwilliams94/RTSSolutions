from typing import List

class Solution:
  def aboveBelow(numbers:List, value:int):
    result = {"above": 0, "below": 0}
    for num in numbers:
      if num > value:
        result["above"] += 1
      elif num < value:
        result["below"] += 1
    return result

  def stringRotation(word:str, rotation:int):
    true_rotation = rotation % len(word)
    shift_index = len(word) - true_rotation
    end = word[:shift_index]
    beginning = word[shift_index:]
    return beginning + end
