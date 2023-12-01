def main():
    array = [12, 45, 67, 89, 34, 67, 12, 45, 100]
    size = len(array)
    max = array[0]
    for i in range(1, size):
        if array[i] > max:
            max = array[i]
    print("Nilai terbesar dari array adalah : {}".format(max))

if __name__ == "__main__":
    main()