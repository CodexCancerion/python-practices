def prompt_nums():
    num_list = [0,0,0]
    print("1. Enter any number: ")
    num_list[0] = int(input())
    print("2. Enter any number: ")
    num_list[1] = int(input())
    print("3. Enter any number: ")
    num_list[2] = int(input())
    return num_list

num_list = prompt_nums()
print(num_list)
sorted_nums = num_list
temp = 0
if num_list[0] < num_list[1] and num_list[1] < num_list[2]:
    sorted_nums[0] = num_list[0]
    if num_list[1] < num_list[2]:
        sorted_nums[1] = num_list[1]
        sorted_nums[2] = num_list[2]
    else:
        sorted_nums[1] = num_list[2]
        sorted_nums[2] = num_list[1]
elif num_list[1] < num_list[0] and num_list[1] < num_list[2]:
    sorted_nums[0] = num_list[1]
    if num_list[0] < num_list[2]:
        sorted_nums[1] = num_list[0]
        sorted_nums[2] = num_list[2]
    else:
        sorted_nums[1] = num_list[2]
        sorted_nums[2] = num_list[0]
elif num_list[2] < num_list[0] and num_list[2] < num_list[1]:
    sorted_nums[0] = num_list[2]
    if num_list[0] < num_list[1]:
        sorted_nums[1] = num_list[0]
        sorted_nums[2] = num_list[1]
    else:
        sorted_nums[1] = num_list[1]
        sorted_nums[2] = num_list[0]
        
print(sorted_nums)