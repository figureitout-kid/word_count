#open file, 
# iterate through text,
# create a dictionary, 
# set key to word in file, 
# and value to number of times it appears. 
# print key, value

# def make_letter_counts_dict(phrase):
#     """Return dict of letters and # of occurrences in phrase."""

#     letter_counts = {}

#     for letter in phrase:
#         letter_counts[letter] = letter_counts.get(letter, 0) + 1

#     return letter_counts

# def word_count(file):

#     open_file = open(file) # open the file

#     new_dict = {}
#     for word in file:
#         new_dict[word] = new_dict.get(word, 0) + 1 
#     return print(new_dict)


def word_count(file):

    poem = open(file,'r') # open the file

    # new_dict = {}
    # for line in open_file:
    #     for word in line:
    #         new_dict[word] = new_dict.get(word, 0) + 1 
    #     return print(.items())

    new_dict = {}

    for line in poem: 
        words = line.split(' ')
        for word in words:
            new_dict[word] = new_dict.get(word, 0) + 1
            if word == " ":
                continue
    
    for word, number in new_dict.items():
        print(f'{word} {number}')
