import numpy as np
import matplotlib.pyplot as plt

def InsertionSort(arr):
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

    for i in range(1, n):
        ex = i
        bars[i].set_color('green')
        for j in range(i-1,-1,-1):
            bars[j].set_color('red')
            plt.pause(spd)
            if  arr[j] > arr[ex]:
                arr[j+1], arr[j] = arr[j], arr[ex]
                ex = j
                bars[j+1].set_height(arr[j+1])
                bars[j].set_height(arr[j])
                bars[j+1].set_color('orange')
                bars[j].set_color('green')
                plt.pause(spd)
            else:
                bars[j].set_color('orange')
                plt.pause(spd)
                break

        bars[ex].set_color('orange')

    plt.show()

arr = np.random.randint(0, 100, 15)
# arr = [1,2,3,4,5,6,7,8,9,10]
# arr = [10,9,8,7,6,5,4,3,2,1]
print("Input: ",arr)
InsertionSort(arr)
print("Output: ",arr)