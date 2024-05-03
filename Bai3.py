from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.


  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    input_text = self.input_textbox.text
    number_list = list(map(int, input_text.split()))
    insertion_sort(number_list)
    output_text = ' '.join(str(num) for num in number_list)
    self.output_textbox.text = output_text

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    input_text = self.input_textbox.text
    number_list = list(map(int, input_text.split()))
    selection_sort(number_list)
    output_text = ' '.join(str(num) for num in number_list)
    self.output_textbox.text = output_text

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    input_text = self.input_textbox.text
    number_list = list(map(int, input_text.split()))
    bubble_sort(number_list)
    output_text = ' '.join(str(num) for num in number_list)
    self.output_textbox.text = output_text

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    input_text = self.input_textbox.text
    number_list = list(map(int, input_text.split()))
    merge_sort(number_list)
    output_text = ' '.join(str(num) for num in number_list)
    self.output_textbox.text = output_text
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1