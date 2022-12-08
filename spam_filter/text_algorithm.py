import utils
import trainingcorpus
import math


corpus = trainingcorpus.TrainingCorpus("spam-data-12-s75-h25/1")

# Count words
spam_words = list()
ham_words = list()

# for spam_text in corpus.spam_texts():   # TODO - function spam_texts(). I want to recieve only clean text (noly small letters and spaces)
#     spam_words += spam_text.strip().split()

# for ham_text in corpus.ham_texts():     #TODO - the same thing
#     ham_words += ham_text.strip().split()

#TEST
for mail, spam_text in corpus.spams():
    spam_words += spam_text.strip().split()
for mail, ham_text in corpus.hams():
    ham_words += ham_text.strip().split()

common_words = set(spam_words).intersection(set(ham_words))


# Count frecuences
spam_word_with_freq = dict()
for word in common_words:
    spam_word_with_freq[word] = spam_words.count(word) / len(spam_words)

ham_word_with_freq = dict()
for word in common_words:
    ham_word_with_freq[word] = ham_words.count(word) / len(ham_words)


# TEST
# print(spam_word_with_freq)
# print()
# print(ham_word_with_freq)

#######################
### END OF TRAINING ###
#######################
# We should save spam_word_with_freq and ham_word_with_freq 



#######################
####### TESTING #######
#######################

# text_to_test = "I love your mom".split()
with open("spam-data-12-s75-h25/2/0002.24b47bb3ce90708ae29d0aec1da08610") as file:
    text_to_test = file.read().strip().split()

valid_words = [word for word in text_to_test if word in spam_word_with_freq]

spam_probs = [spam_word_with_freq[word] for word in valid_words]
ham_probs = [ham_word_with_freq[word] for word in valid_words]

#TEST
for w in text_to_test:
    if w in valid_words:
        print(f"{w} : {spam_word_with_freq[w]}")

spam_score = sum([math.log(p) for p in spam_probs]) + math.log(corpus.START_SPAM_PROB)
ham_score = sum([math.log(p) for p in ham_probs]) + math.log(1 - corpus.START_SPAM_PROB)

# TEST
print(f"Spam score: {spam_score}")
print(f"Ham score: {ham_score}")
print("SPAM") if spam_score >= ham_score else print("OK")
