def max_product_subsequence(lst):
    max_product = 1
    current_product = 1
    max_subsequence = []
    current_subsequence = []

    for num in lst:
        if not current_subsequence or num == current_subsequence[-1]:
            current_product *= num
            current_subsequence.append(num)

            if current_product > max_product or (current_product == max_product and len(current_subsequence) > len(max_subsequence)):
                max_product = current_product
                max_subsequence = current_subsequence[:]
        else:            
            current_product = num
            current_subsequence = [num]


    return max_subsequence, max_product

# Test the function
lst = [1, 2, 2, 2, 4, 4]
sequence, product = max_product_subsequence(lst)
print("Sequence:", sequence)
print("Product:", product)

