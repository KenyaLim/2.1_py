def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

def main():
    array = [12, 45, 67, 89, 34, 67, 12, 45, 100]
    bubbleSort(array)
    print("Nilai terbesar dari array adalah : {}".format(array[-1]))
    print("Array dalam urutan menaik adalah : {}".format(array))

if __name__ == "__main__":
    main()