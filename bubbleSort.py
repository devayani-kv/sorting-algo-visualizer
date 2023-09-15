import time

def bubble_sort(data, drawData, timeTick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                color_arr = []
                for x in range(len(data)):
                    if x == j:
                        color_arr.append('green')
                    elif x == j+1:
                        color_arr.append('blue')
                    else:
                        color_arr.append('red')
                drawData(data, color_arr)
                time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])