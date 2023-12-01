def main():
    array = [12, 45, 67, 89, 34, 67, 12, 45, 100]
    sorted_array = sorted(array)
    print("Nilai terbesar dari array adalah : {}".format(sorted_array[-1]))
    print("Array dalam urutan menaik adalah : {}".format(sorted_array))

if __name__ == "__main__":
    main()