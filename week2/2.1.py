def max_product_break(n):
    if n <= 1:
        return 0
    max_products = [0] * (n + 1)
    max_products[0] = max_products[1] = 0
    for i in range(2, n + 1):
        max_product = 0
        for j in range(1, i):
            max_product = max(max_product, j * (i - j))
        max_products[i] = max_product
    return max_products[n]


n = 2021
result = max_product_break(n)
print(result)
