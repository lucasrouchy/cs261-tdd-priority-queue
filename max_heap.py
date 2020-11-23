# MaxHeap: A binary 'max' heap.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_max_heap.py.
# YOUR NAME
import math
class MaxHeap:
   def __init__(self):
      self._data = []
   def _size(self):
      return len(self._data)
   
   def _is_empty(self):
      return self._size() == 0

   def _last_index(self):
      return self._size() - 1
   def _value_at(self, index):
      return self._data[index]
   def _left_child_index(self, index):
      return index * 2 + 1
   def _right_child_index(self, index):
      return index * 2 + 2
   def _parent_index(self, index):
      return math.floor((index - 1)/2)
   def _parent(self, index):
      return self._data[self._parent_index(index)]
   def _left_child(self, index):
      try:
         return self._data[self._left_child_index(index)]
      except IndexError:
         return None
   def _right_child(self, index):
      try:
         return self._data[self._right_child_index(index)]
      except IndexError:
         return None
   def _has_left_child(self, index):
      return self._left_child(index) is not None
   def _has_right_child(self, index):
      return self._right_child(index) is not None
   def _greater_child_index(self, index):
      if self._has_left_child(index) and self._has_right_child(index):
         return
      elif self._has_left_child(index):
         return self._left_child_index(index)
      elif self._has_right_child(index):
         return
      else:
         return None

