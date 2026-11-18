import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    # TODO - Complete the function so it loads the data from the file into a list
    # The function returns a tuple that contains the list of values and the total number 
    # of values in the column
    #pass
    numbers = []
    count = 0
    with open(filepath, 'r') as infile:
        for line in infile:
            line_num = count + 1
            try:
                value = line.split('\t')[column]
            except IndexError:
                print(f"There is no valid 'list index' in column {column} in line {line_num} in file: {filepath}")
                sys.exit(1)
            count = count + 1
            try:
                num = float(value)
            except ValueError:
                continue
            if math.isnan(num):
                continue
            numbers.append(num)
    return numbers, count
        

def calculate_average(numbers:list)->float:
    # TODO - Complete the function to return the average of the list of numbers
    #pass
    return sum(numbers) / len(numbers)
    

def get_max_and_min(numbers:list)->tuple[float, float]:
    # TODO - Complete the function to return a tuple with the maximum and minimum
    # values in the list, in that order
    #pass
    return max(numbers), min(numbers)


def calculate_variance(numbers:list)->float:
    # TODO - Complete the function to return the variance of the numbers in the list
    #pass
    n = len(numbers)
    if n < 2:
        return 0.0
    average = calculate_average(numbers)
    total = 0.0
    for num in numbers:
        total += (num - average) ** 2
    return total / (n - 1)

def calculate_std_dev(numbers:list)->float:
    # TODO - Complete the function to return the standard deviation of the numbers in the list
    #pass
    return math.sqrt(calculate_variance(numbers))
    

def calculate_median(numbers:list)->float:
    # TODO - Complete the function to return the median of the numbers in the list
    #pass
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 1:
        return float(sorted_numbers[mid])
    else:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2.0