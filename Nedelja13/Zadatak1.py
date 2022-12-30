def popuni(n):
    return [x for x in range(n) if x % 2 != 0]

nums_max = int(input("Unesite broj -> "))
nums = popuni(nums_max)
print(nums)

