def my_func(arg1, arg2, arg3):
    kit = [arg1, arg2, arg3]
    kit.remove(min(arg1, arg2, arg3))
    return sum(kit)


print(my_func(11, 15, 9))
