import numpy as np
import matplotlib.pyplot as plt

def BubbleSort(arr):
  n = len(arr)
  x = np.arange(0, n, 1)
  swapped = False

  # Create the plot
  fig, ax = plt.subplots()
  bars = ax.bar(x, arr)
  ax.set_title('Bubble Sort Visualization')
  ax.set_xlabel('Index')
  ax.set_ylabel('Value')
  ax.set_xticks(x)

  # Set low for more speed
  spd = 0.05

  for i in range(n-1):
    for j in range(n-i-1):
      # Green for smaller, Red for larger and Orange for sorted.
      bars[j].set_color('green')
      bars[j+1].set_color('red')
      plt.pause(spd)

      if arr[j] > arr[j+1]:
        swapped = True
        # Swap data and bar heights
        arr[j], arr[j+1] = arr[j+1], arr[j]
        bars[j].set_height(arr[j])
        bars[j+1].set_height(arr[j+1])
        plt.pause(spd)
        bars[j].set_color('green')
        bars[j+1].set_color('red')

      plt.pause(spd)
      bars[j].set_color('#1f77b4')

    bars[n-i-1].set_color('orange')

    if i==n-2:
      bars[0].set_color('orange')

    # Check if any swaps occurred and break if not
    if not swapped:
      for t in range(n):
        bars[t].set_color('orange')
      break

  for i, value in enumerate(arr):
    plt.text(i, value, str(value), ha='center', va='bottom')

  plt.show()

arr = np.random.randint(0, 100, 15)
# arr = [1,2,3,4,5,6,7,8,9,10]
# arr = [10,9,8,7,6,5,4,3,2,1]
print("Input: ",arr)
BubbleSort(arr)
print("Output: ",arr)