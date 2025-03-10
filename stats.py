def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_symbols(text):
    char_count = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in char_count:
            char_count[lowercase_char] += 1
        else:
            char_count[lowercase_char] = 1
    return char_count

    
def get_sorted_list(char_count):
    # Create an empty list to store our dictionaries
    char_list = []
    
    # Iterate through each key-value pair in the char_count dictionary
    for char, count in char_count.items():
        # Create a new dictionary for this character and its count
        char_dict = {"char": char, "count": count}
        # Add this dictionary to our list
        char_list.append(char_dict)
    
    # Now char_list is a list of dictionaries, each with 'char' and 'count' keys
    # Next, we need to sort it
    
    # Define a function to tell sort() which value to use for sorting
    def sort_on(dict):
        return dict["count"]
    
    # Sort the list in descending order by count
    char_list.sort(reverse=True, key=sort_on)
    
    # Return the sorted list
    return char_list
