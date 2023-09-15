import time

def selection_sort(data, drawData, timeTick):
    n = len(data)
    min_ind = 0
    for i in range(0,n-1):
        min_ind = i
        for j in range(i+1, n):
            if data[j] < data[min_ind]:
                min_ind = j
        if min_ind != i:
            t = data[i]
            data[i] = data[min_ind]
            data[min_ind] = t
            color_arr = []
            for k in range(0,n):
                if k == i:
                    color_arr.append('yellow')
                elif k == min_ind:
                    color_arr.append('red')
                else:
                    color_arr.append('green')
            drawData(data,color_arr)
            time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])
        