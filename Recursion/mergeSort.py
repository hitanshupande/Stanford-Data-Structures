def mergeSort(a):
    size = len(a)
    if size>1:
        if size%2!=0:
            size = size+1
        mid = int(size/2)
        left = a[:mid]
        right = a[mid:]
        mergeSort(left)
        mergeSort(right)
        i,j,k=0,0,0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    a = [3, 6, 7, 1, 9, 5, 2, 8, 4, 4]
    print("List before sort: ", a)
    mergeSort(a)
    print("List after sort: ", a)

