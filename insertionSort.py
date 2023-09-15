import time

def insertion_sort(data, drawData, timeTick):
    n = len(data)
    for i in range(1,n):
        key = data[i]
        j = i-1
        while j>=0 and data[j]>key:
            data[j + 1] = data[j]
            j = j - 1
        color_arr = []
        for k in range(n):
            if k == i:
                color_arr.append('red')
            elif k == j+1:
                color_arr.append('yellow')
            else:
                color_arr.append('green')
        drawData(data,color_arr)
        data[j + 1] = key
        time.sleep(timeTick)
        drawData(data,color_arr)
        time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])
