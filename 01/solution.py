def unique_char_finder(str_value: str) -> int:
    char_counts = {}
    
    for char in str_value:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
            
    for index, value in enumerate(str_value):
        if char_counts[value] == 1:
            return index
    return -1

    

print(unique_char_finder("memhlovel"))