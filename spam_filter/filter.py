import basefilter
import trainingcorpus
import utils
import os
from math import log

class MyFilter(basefilter.BaseFilter):

    def __init__(self):
        super().__init__()
        self.spam_word_with_freq = dict()   #TODO - pre-training
        self.ham_word_with_freq = dict()
    

    def train(self, path):
        train_corpus = trainingcorpus.TrainingCorpus(path)

        # Count words
        spam_words = list()
        ham_words = list()

        for spam_text in train_corpus.spam_texts():   # TODO - function spam_texts(). I want to recieve only clean text (only small letters and spaces)
            spam_words += spam_text.strip().split()

        for ham_text in train_corpus.ham_texts():     #TODO - the same thing
            ham_words += ham_text.strip().split()

        common_words = set(spam_words).intersection(set(ham_words))

        # Count frecuences
        for word in common_words:
            self.spam_word_with_freq[word] = spam_words.count(word) / len(spam_words)

        for word in common_words:
            self.ham_word_with_freq[word] = ham_words.count(word) / len(ham_words)


    def predict(self, path, filename):

        file_path = os.path.join(path, filename)
        plain_text, email_attrs, html_count = utils.parse_email(file_path)

        spam_score = ham_score = 0

        spam_score, ham_score = self.test_text(plain_text)
        spam_score, ham_score = self.other_tests()   #TODO - decide what it returns

        self.predictions[filename] = "SPAM" if spam_score >= ham_score else "OK"


    def test_text(self, text):

        START_SPAM_PROB = 0.3

        text = text.strip().split()

        valid_words = [word for word in text if word in self.spam_word_with_freq]

        spam_probs = [self.spam_word_with_freq[word] for word in valid_words]
        ham_probs = [self.ham_word_with_freq[word] for word in valid_words]

        spam_score = sum([log(p) for p in spam_probs]) + log(START_SPAM_PROB)
        ham_score = sum([log(p) for p in ham_probs]) + log(START_SPAM_PROB)

        return (spam_score, ham_score)
