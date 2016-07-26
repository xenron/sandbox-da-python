

def my_sort(target, reverse=False):
    target.sort(reverse=reverse)


if __name__ == '__main__':
    # 正序
    arr1 = [13, 12, 14]
    my_sort(arr1, reverse=False)
    print(arr1)
    # 倒序
    arr2 = [13, 12, 14]
    my_sort(arr2, reverse=True)
    print(arr2)
