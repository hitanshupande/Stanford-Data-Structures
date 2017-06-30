def mergeCount(a):
    global count
    size = len(a)
    if size>1:
        if size%2!=0:
            size = size+1
        mid = int(size/2)
        left = a[:mid]
        right = a[mid:]
        mergeCount(left)
        mergeCount(right)
        i,j,k=0,0,0
        x,y = left,right
        for k in range(len(x)+len(y)+1):
            if x[i] <= y[j]:
                a[k] = x[i]
                i += 1
                if i == len(x) and j != len(y):
                    while j != len(y):
                        k += 1
                        a[k] = y[j]
                        j += 1
                    break
            elif x[i] > y[j]:
                a[k] = y[j]
                j += 1
                count += (len(x) - i)
                if j == len(y) and i != len(x):
                    while i != len(x):
                        k += 1
                        a[k] = x[i]
                        i += 1
                    break
    return count


if __name__ == '__main__':
    a = [1,3,5,2,4,6]
    count = 0
    print("List before sort: ", a)
    count = mergeCount(a)
    print("Number of inversions", count)

