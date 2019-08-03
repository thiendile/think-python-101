def cross_product(l1, l2):
    result = [0] * len(l1)
    for i in range(len(l1)):
        result[i] = l1[i - 2] * l2[i - 1] - l1[i - 1] * l2[i - 2]
    return result


print(cross_product([1, 2, 3], [4, 5, 6]))

