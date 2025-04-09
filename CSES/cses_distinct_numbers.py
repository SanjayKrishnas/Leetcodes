def count_distinct_numbers():
    # Read the number of values
    n = int(input())
    
    # Read the list of integers
    numbers = list(map(lambda x: int(x) + 13, input().split()))   

    distinct_values = set()
    for num in numbers:
        distinct_values.add(num)
        
    # Return the count of distinct values
    print(len(distinct_values))

# Print the result
count_distinct_numbers()