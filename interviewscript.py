def decode(message_file_path):
    with open(message_file_path, 'r') as file:
        lines = file.readlines()
        
    # Parse the file to create a dictionary {number: word}
    num_word_dict = {}
    for line in lines:
        parts = line.split()
        num_word_dict[int(parts[0])] = " ".join(parts[1:])
    
    # Calculate the lines in the pyramid
    num_lines = 1
    while (num_lines * (num_lines + 1)) // 2 <= max(num_word_dict.keys()):
        num_lines += 1
    num_lines -= 1  # Adjust to fit exactly the number of words
    
    # Select the words that are at the end of each pyramid line
    message_words = []
    current_num = 1
    for i in range(1, num_lines + 1):
        current_num += i - 1
        message_words.append(num_word_dict[current_num])
    
    # Construct the message
    decoded_message = " ".join(message_words)
    return decoded_message

# Actual file path
message = decode('example.txt')
print(message)
