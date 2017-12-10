my_input = 277678
n = 1

while n**2 < my_input:
    n += 2

side_len = (n**2 - (n - 2)**2) / 4
middle_len = side_len / 2
max_dist = n - 1
min_dist = max_dist / 2
side_num = n**2 - side_len

while side_num > my_input:
    side_num = side_num - side_len

middle_num = side_num + middle_len
dist = min_dist + abs(my_input - middle_num)

print(dist)
