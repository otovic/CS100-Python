def my_factorial(n):
    if n < 1:
        return 1
    return n * my_factorial(n - 1) 

def find_lotto_combinations(selected_numbers, total_numbers):
    return my_factorial(total_numbers) / (my_factorial(selected_numbers) * my_factorial(total_numbers - selected_numbers)) 

print(find_lotto_combinations(7, 39))