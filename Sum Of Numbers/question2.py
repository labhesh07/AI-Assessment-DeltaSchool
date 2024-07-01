def sum_of_numbers():
    #  input from the user
    user_input = input("Enter a list of numbers separated by spaces: ")
    string_list = user_input.split()
    
    numbers = [int(i) for i in string_list]
    
    # the sum of the list of numbers
    Sum = sum(numbers)
    
    return Sum

print("The sum of the numbers is:",sum_of_numbers())