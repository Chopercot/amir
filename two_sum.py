# def two_sum(num, tar):
#     new_arr = []
#     n = any([num.count(x) > 1 for x in num])
#     for x in num:
#         ind = num.index(x)
#         z = num.pop(ind)
#         for y in num:
#             if x + y == tar:
#                 new_arr.append(x)
#             print(x, y, num)
#         print('......', z, x, num)
#         num.insert(ind, z)
#     print(n)
#     return ([num.index(x) for x in new_arr], [x for x in range(len(new_arr)) if new_arr[x] == num[x]])[n]

# def two_sum(num, tar):
#     e_num = list(enumerate(num))
#     for x in num:
#         ind = num.index(x)
#         pop = num.pop(num.index(x))
#         if pop + num[x] == tar:
#             n = [ind for x in range(len(num))]
#         num.insert(ind, pop)


def two_sum(num, tar):
    for x in range(len(num)):
        cn = num.count(num[x]) > 1
        dict_t = {y: x for x, y in list(enumerate(num))}
        pop = num.pop(x)
        print(pop, x)
        for y in range(len(num)):
            print(x, y, num, pop, num[y], dict_t, cn)
            if pop + num[y] == tar:
                return ([dict_t[pop], dict_t[num[y]]], [x, y + 1])[cn]
        num.insert(x, pop)


# Not mine, best practices
'''
def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]
'''
