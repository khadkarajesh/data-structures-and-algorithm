def insertion_sort(data):
    for i in range(0, len(data) - 1):
        j = i + 1
        key = data[j]
        while j > 0 and key < data[j - 1]:
            data[j] = data[j - 1]
            j = j - 1
        data[j] = key
    return data


if __name__ == '__main__':
    print(insertion_sort([51, 50, 49, 47, 48]))
