def decode(message_file_path):
    # Initialize a dictionary to map numbers to words.
    num_word_dict = {}
    
    # Read from the file and populate the dictionary.
    with open(message_file_path, 'r') as file:
        for line in file:
            num, word = line.strip().split(maxsplit=1)
            num_word_dict[int(num)] = word
    
    # Calculate the total number of lines in the pyramid.
    total_items = len(num_word_dict)
    num_lines = 0
    while total_items > 0:
        num_lines += 1
        total_items -= num_lines
    
    # If the total number of items doesn't form a perfect pyramid, return False.
    if total_items < 0:
        return False
    
    # Construct the message from the pyramid's last numbers of each line.
    message_words = []
    current_index = 1
    for i in range(1, num_lines + 1):
        current_index += i - 1
        if current_index in num_word_dict:
            message_words.append(num_word_dict[current_index])
    
    # Return the decoded message.
    return ' '.join(message_words)

# Example usage
print(decode('example.txt'))
