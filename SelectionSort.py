import numpy as np
import matplotlib.pyplot as plt

def SelectionSort(arr):
   n = len(arr)
   x = np.arange(0, n, 1)

   # Create the plot
   fig, ax = plt.subplots()
   bars = ax.bar(x, arr)
   ax.set_title('Selection Sort Visualization')
   ax.set_xlabel('Index')
   ax.set_ylabel('Value')
   ax.set_xticks(x)

   # Set speed
   spd = 0.05
   
   for i in range(n):
        # Index of least element
        li = i
        bars[li].set_color('green')
        for j in range(i+1, n):
            bars[j].set_color('red')
            plt.pause(spd)
            if arr[j] < arr[li]:
                bars[li].set_color('#1f77b4')
                li = j
                bars[li].set_color('green')
                plt.pause(spd)

            else:
                bars[j].set_color('#1f77b4')
                plt.pause(spd)

            if j==n-1:
                bars[li].set_color('#1f77b4')
                plt.pause(spd)
        
        # Swap minimum
        arr[i], arr[li] = arr[li], arr[i]
        bars[i].set_height(arr[i])
        bars[li].set_height(arr[li])
        bars[i].set_color('orange')
        plt.pause(spd)

   for i, value in enumerate(arr):
       plt.text(i, value, str(value), ha='center', va='bottom')
   plt.show()
        
arr = np.random.randint(0, 100, 15)
# arr = [1,2,3,4,5,6,7,8,9,10]
# arr = [10,9,8,7,6,5,4,3,2,1]
print("Input: ",arr)
SelectionSort(arr)
print("Output: ",arr)