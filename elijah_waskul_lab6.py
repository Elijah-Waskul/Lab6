"""
Elijah Waskul
10/6/2024
Lab 6 - Lists
"""




# Problem 1
# Arithmetic with corresponding elements of multiple lists.
# Here are several test cases. Uncomment them one at a time to ensure your code works.

# Test 1 - correct answer = 8
# list1, list2, list3 = [1, 2, 3], [4, 5, 6], [7, 8, 9]

# Test 2 - correct answer = 21
# list1, list2, list3 = [5, -2, 4], [3, 12, 9], [8, 4, -6]

# Test 3 - correct answer = 0
# list1, list2, list3 = [], [], []

# Test 4 - correct answer = -7
# list1, list2, list3 = [7, 3, 5, 7, 1], [2, 2, 3, -3, 4], [5, 6, 5, 4, 5]

# Test 5
# list1, list2, list3 = [4, 4], [3, 2], [8, 9, 1]

# Test 6
# list1, list2, list3 = [6.3, 8.4, 9.2], [-1.2, 7.6, 3.2], [4.1, -2.1, 9.6]

def arithmetic_lists(list1, list2, list3):
    if len(list1) != len(list2) or len(list2) != len(list3):
        return "All lists are required to be the same length."
    
    result = 0
    for i in range(len(list1)):
        result += list1[i] * list2[i] - list3[i]
    
    return result
    
# Problem 2
def create_new_list(list1, list2, list3):
    if len(list1) != len(list2) or len(list2) != len(list3):
        return "All lists are required to be the same length."
    
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i] * list2[i] - list3[i])
    
    return new_list
    
# Problem 3

    # Test 1 - Mean = 3, Median = 3
data_set_1 = [3, 2, 1, 4, 5]

# Test 2 - Mean = 6.1146, Median = 6
data_set_2 = [
    10, 8, 5, 3, 6, 8, 8, 6, 7, 3, 6, 4, 6, 10, 6, 6, 9, 6, 10, 8, 
    4, 6, 5, 7, 4, 5, 2, 4, 2, 6, 10, 3, 2, 5, 5, 6, 4, 3, 2, 9, 3, 
    5, 9, 9, 9, 6, 7, 5, 5, 6, 5, 8, 10, 4, 9, 3, 3, 10, 7, 8, 2, 6, 
    4, 7, 9, 9, 8, 8, 3, 9, 7, 4, 3, 9, 8, 4, 9, 3, 7, 2, 10, 10, 8, 
    6, 4, 7, 10, 8, 4, 4, 5, 4, 9, 3, 8, 2, 5, 8, 10, 5, 10, 7, 2, 
    3, 3, 5, 3, 4, 8, 10, 9, 7, 5, 9, 5, 5, 2, 6, 10, 9, 4, 2, 9, 
    10, 7, 10, 8, 4, 10, 6, 10, 10, 4, 2, 6, 2, 3, 5, 8, 5, 10, 8, 
    7, 5, 10, 7, 5, 9, 5, 5, 10, 5, 7, 2, 3, 2, 2
]

  #Test3 - Think carefully about what the output should be!
data_set_3 = []

data = data_set_1

def calculate_mean_median(data):
    if not data:
        return
    mean = sum(data) / len(data)
    data_sorted = sorted(data)
    n = len(data_sorted)
    if n % 2 == 1:
        median = data_sorted[n // 2]
    else:
        median = (data_sorted[n // 2 - 1] + data_sorted[n // 2]) / 2
    return mean, median

mean, median = calculate_mean_median(data)
print(f"Mean: {mean}, Median: {median}")
