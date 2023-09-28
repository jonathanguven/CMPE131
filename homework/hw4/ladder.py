# 1. Combitorial Climb
def my_steps(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return my_steps(n - 1) + my_steps(n - 2)


print(my_steps(25))
print(my_steps(2))

