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
      if 0 <= index <= self._size():
            return self._data[index]
      else:
         raise IndexError
   def _left_child_index(self, index):
      return index * 2 + 1
   def _right_child_index(self, index):
      return index * 2 + 2
   def _parent_index(self, index):
      return (index-1) // 2
   def _parent(self, index):
       return self._value_at(self._parent_index(index))
   def _left_child(self, index):
      child_index = self._left_child_index(index)
      if child_index >= self._size():
         return None
      else:
         return self._value_at(child_index)
   def _right_child(self, index):
      child_index = self._right_child_index(index)
      if child_index >= self._size():
         return None
      else:
         return self._value_at(child_index)
   def _has_left_child(self, index):
      return self._left_child(index) is not None
   def _has_right_child(self, index):
      return self._right_child(index) is not None
   def _greater_child_index(self, index):
      if self._has_left_child(index) and self._has_right_child(index):
         return max(self._left_child_index(index), self._right_child_index(index), key=self._value_at)
      elif self._has_left_child(index):
         return self._left_child_index(index)
      elif self._has_right_child(index):
         return self._right_child_index(index)
      else:
         return None
   def _obeys_heap_property_at_index(self, index):
      if self._has_left_child(index) or self._has_right_child(index):
         return self._value_at(index) >= self._value_at(self._greater_child_index(index)) 
      else:
         return True
   def _swap(self, target, source):
      temp = self._value_at(target)
      self._data[target] = self._value_at(source)
      self._data[source] = temp
   def _sift_down(self, index):
      if self._obeys_heap_property_at_index(index):
         return
      else:
         swap_index = self._greater_child_index(index)
         self._swap(index, swap_index)
         self._sift_down(swap_index)
   def _sift_up(self, index):
      if index == 0 or self._obeys_heap_property_at_index(index):
         return
      else:
         self._swap(index, self._parent_index(index))
         self._sift_up(self._parent_index(index))
         
