
def replace(line, word, new_word):
    new_line = line
    for i in range(line.count(word)):
        start_index = new_line.find(word) #returns the starting index of the word
        new_line = new_line[:start_index] + new_word + new_line[start_index + len(word):]
    return new_line