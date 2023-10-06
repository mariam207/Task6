# Question 1
lst = [30, 75, 9, 97, 50, -4, 70, 59]
largest_num = lst[0]
smallest_num = lst[0]
for num in lst:
    if num > largest_num:
        largest_num = num
    if num < smallest_num:
        smallest_num = num
print(largest_num)
lst.remove(smallest_num)
lst.sort()
#the output in the task prints the first 4 numbers (:
print(lst[-4:])

# Question 2
print('\n')
main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python", 1]]
times_repeated = 0
for loop_lst in main_lst:
    if "python" in loop_lst:
        times_repeated += loop_lst.count("python")
print(times_repeated)

# Question 3
print('\n')
my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]
one_sentence = ""
for word in my_lst:
    word = word.capitalize()
    one_sentence += word + " "
print(one_sentence)

# Question 4
print('\n')
my_lst = [12, 3.8, "GSG", ["sKy", "zak"]]
copied_lst = []
for item in my_lst:
    copied_lst.append(item)
print(copied_lst)


# Question 5
print('\n')
third_ele = 19
my_lst = ["GSG", "zakaria", 19, 9.8, "Omar"]
my_lst[2] = my_lst[4]
my_lst[4] = third_ele
print(my_lst)

# Question 6
print('\n')
nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
Sum = 0
for num in nums:
    Sum += num
print(Sum)

# Question 7
print('\n')
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
new_num = 9
new_tuple = tuple1 + (new_num,)
print(new_tuple)

# Question 8
print('\n')
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple2 = ('Java', 'C++', 7.8)
new_tuple = tuple1 + tuple2
print(new_tuple)