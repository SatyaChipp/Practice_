#####count freq of words in text file
word_count= dict()

with open(r'C:/Users/Jen/Downloads/resumes/PracticeCodeM/cantrbry/plrabn12.txt', 'r') as fi:
    for line in fi:
        words = line.split()
        prepared_words = [w.lower() for w in words]
        for w in prepared_words:
            word_count[w] = 1 if w not in word_count else word_count[w]+1
def most_commmon_words(num=10):
    sorted_words = sorted(word_count, key=word_count.get, reverse=True)
    return sorted_words[:num]

pprint_here = '\n'.join(most_commmon_words(5))

print(pprint_here)
