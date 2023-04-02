def sequenceExists(main, seq):
    # check if the sequence length is greater than the main array
    if len(seq) > len(main):
        return False
    
    # loop through the main array and find the first element of the sequence
    for i in range(len(main)):
        if main[i] == seq[0]:
            # if the first element is found, check if the rest of the sequence exists
            if seq == main[i:i+len(seq)]:
                return True
    
    # if the sequence is not found, return false
    return False

# example usage
main = [20, 7, 8, 10, 2, 5, 6]
print(sequenceExists(main, [7, 8])) # should print True
print(sequenceExists(main, [8, 7])) # should print False
print(sequenceExists(main, [7, 10])) # should print False