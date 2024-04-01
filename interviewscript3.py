def decode(message_file_path):
    with open(message_file_path, 'r') as file:
        lines = file.readlines()
        
    # Parse the file to create a dictionary {number: word}
    num_word_dict = {}
    for line in lines:
        parts = line.split()
        num_word_dict[int(parts[0])] = " ".join(parts[1:])
    
    # Initialize variables to determine the end numbers of pyramid lines
    pyramid_end_numbers = []
    total_numbers = max(num_word_dict.keys())
    step = 1
    while step * (step + 1) // 2 <= total_numbers:
        pyramid_end_numbers.append(step * (step + 1) // 2)
        step += 1

    # Select the words that are at the end of each pyramid line
    message_words = [num_word_dict[num] for num in pyramid_end_numbers if num in num_word_dict]
    
    # Construct the message
    decoded_message = " ".join(message_words)
    return decoded_message

# Example usage
message = decode('coding_qual_input.txt')
print(message)
