def main():
    print("Insertion Sort")
    a1 = [5,2,4,6,1,3]
    insertion_sort(a1)

def insertion_sort(a):
    print("start: " + str(a))

    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        # swap
        while ((i >= 0) and (a[i] > key)):
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key

    print("final: " + str(a))


if __name__ == "__main__":
    main()