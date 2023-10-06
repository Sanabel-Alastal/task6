# Q1)..
lst = [30, 75, 9, 97, 50, -4, 70, 59]
print(max(lst))
print(min(lst))
lst.sort()
print(lst)
print(lst[-4:])


# Q3)..
my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]
string_list=' '.join(my_lst)
print(string_list)

# Q4)..
my_lst = [12, 3.8, "GSG", ["sKy", "zak"]]
lst2 =  my_lst
print(lst2)
# lst2 = my_lst.copy()

# Q5)..
my_lst = ["GSG", "zakaria", 19, 9.8, "Omar"]
my_lst[2], my_lst[4] = my_lst[4], my_lst[2]
print(my_lst)

# Q6)..
nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
total = sum(nums)
print("Sum =", total)

# Q7)..
t1 = (4, 'python', 'GSG', [8, 3, 1])
t2=(9,)
t1+=t2
print(t1)

# Q8)..
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple2 = ('Java', 'C++', 7.8)
tuple3 = tuple1 +tuple2
print(tuple3)


