def second_max(a):

    # Find the maximum element in the list
    max_element = max(a)

    # Remove the maximum element from the list
    a.remove(max_element)

    # Find the new maximum, which is the second largest
    second_largest = max(a)

    return second_largest

#example
input = [1, 22, 33]
print(f"List: {input}")

result = second_max(input)

print(f"Second largest element: {result}")
