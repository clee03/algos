
def main():
    print("Insertion Sort")
    a1 = [5,2,4,6,1,3]
    insertion_sort(a1)

def insertion_sort(a):
    print("start: " + str(a))

    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while ((i >= 0) and (a[i] > key)):
            print("compare " + str(a[i]) + " is > " + str(key))
            a[i + 1] = a[i]
            print("move key " + str(key) + " to index " + str(i))
            i = i - 1
        a[i + 1] = key
        print("round " + str(j) + ": " + str(a))

    print("final: " + str(a))


if __name__ == "__main__":
    main()