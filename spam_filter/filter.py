#   Used materials:
#   1) Algorithm idea for test_text() function:
#   https://youtu.be/VQZxLPEdIpE

import basefilter
import trainingcorpus
import utils
import os
from math import log

class MyFilter(basefilter.BaseFilter):

    def __init__(self):
        '''
        Initialization of filter
        '''
        super().__init__()

        # Dictionaries with information for testing emails
        self.spam_word_with_freq = dict()
        self.ham_word_with_freq = dict()

        #TODO - pre-training
    

    def train(self, path):
        '''
        Trains filter with given set of emails

        :param path:    path to directory with emails for training (string)
        '''
        train_corpus = trainingcorpus.TrainingCorpus(path)

        # Count spam and ham words in all emails
        spam_words = list()
        ham_words = list()

        for spam_text in train_corpus.spams():
            spam_words += spam_text.strip().split()

        for ham_text in train_corpus.hams():
            ham_words += ham_text.strip().split()

        # Find common words for spam and ham
        common_words = set(spam_words).intersection(set(ham_words))

        # Count frequences of spam and ham words
        for word in common_words:
            self.spam_word_with_freq[word] = spam_words.count(word) / len(spam_words)

        for word in common_words:
            self.ham_word_with_freq[word] = ham_words.count(word) / len(ham_words)


    def predict(self, path, filename):
        '''
        Makes prediction for one particular email

        Side effects: Fill self.predictions with {filename:prediction}
        :param path:        path to directory with testing emails (string)
        :param filename:    name of the current email (string)
        '''

        # print(f"PREDICTION FOR FILE {filename}") #DEBUG

        # Getting necessary information from email content
        file_path = os.path.join(path, filename)
        plain_text, email_attrs, html_count = utils.parse_email(file_path)

        # Empty text is more likely a SPAM
        if plain_text == "":
            self.predictions[filename] = "SPAM"
            return
        
        # Probabilities of email being spam or ham
        spam_score = ham_score = 0

        # Counting spam and ham scores by a bunch of tests
        spam_score, ham_score = self.test_text(plain_text)
        #spam_score, ham_score = self.other_tests()   #TODO - decide what it returns

        # print(f"SPAM_SCORE = {spam_score}") #DEBUG
        # print(f"HAM_SCORE = {ham_score}") #DEBUG

        # Final decision for current email
        self.predictions[filename] = "SPAM" if spam_score >= ham_score else "OK"


    def test_text(self, text):
        '''
        Tests text of email

        :param text: clean text (only words written with small letters) (string)
        :return:     tuple (spam_score, ham_score)
        '''
        # Start probability of email being a SPAM
        START_SPAM_PROB = 0.3

        text = text.strip().split()

        valid_words = [word for word in text if word in self.spam_word_with_freq]

        spam_probs = [self.spam_word_with_freq[word] for word in valid_words]
        ham_probs = [self.ham_word_with_freq[word] for word in valid_words]

        spam_score = sum([log(p) for p in spam_probs]) + log(START_SPAM_PROB)
        ham_score = sum([log(p) for p in ham_probs]) + log(START_SPAM_PROB)

        return (spam_score, ham_score)
