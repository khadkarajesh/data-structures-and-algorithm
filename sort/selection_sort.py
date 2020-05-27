def selection_sort(data):
    for i in range(0, len(data) - 1):
        smallest_index = i
        for k in range(i + 1, len(data)):
            if data[k] < data[smallest_index]:
                smallest_index = k
        if data[i] != data[smallest_index]:
            data[i] = data[i] + data[smallest_index]
            data[smallest_index] = data[i] - data[smallest_index]
            data[i] = data[i] - data[smallest_index]
    return data


if __name__ == '__main__':
    print(selection_sort([51, 31, 40, 47, 48]))
