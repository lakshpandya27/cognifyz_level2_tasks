def count_word_occurrences(file_path):
    word_counts = {}

    # Open the file and read its content
    with open(file_path, 'r') as file:
        # Process each line in the file
        for line in file:
            # Split the line into words
            words = line.split()

            # Update word counts
            for word in words:
                # Remove punctuation and convert to lowercase for consistency
                cleaned_word = word.strip('.,!?\'"()[]{}').lower()

                # Update word count in the dictionary
                word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1

    # Display results in alphabetical order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[0])

    for word, count in sorted_word_counts:
        print(f'{word}: {count}')

# Example usage:
file_path = 'john.txt'
count_word_occurrences(file_path)
