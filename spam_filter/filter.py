#   Used materials:
#   1) Algorithm idea for test_text() function:
#   https://youtu.be/VQZxLPEdIpE

import basefilter
from trainingcorpus import TrainingCorpus
import utils
import os
from math import log

class MyFilter(basefilter.BaseFilter):

    def __init__(self):
        '''
        Initialization of filter
        '''
        super().__init__()

        # Dictionaries with trained information for testing emails
        self.spam_word_with_freq = dict()
        self.ham_word_with_freq = dict()

        #TODO - read self.bad_words from file
        #TODO - pre-training
    

    def train(self, path):
        '''
        Trains filter with given set of emails

        Side effects:   fills self.ham/spam_word_with_freq
        :param path:    path to directory with emails for training (string)
        '''
        train_corpus = TrainingCorpus(path)

        # Count spam and ham words in all emails
        spam_words = list()
        ham_words = list()

        for spam_text in train_corpus.spams():
            spam_words += spam_text.strip().split()

        for ham_text in train_corpus.hams():
            ham_words += ham_text.strip().split()

        # Find common words for spam and ham
        common_words = set(spam_words).intersection(set(ham_words))

        # Count frequencies of spam and ham words
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
        # Getting necessary information from email content
        file_path = os.path.join(path, filename)
        plain_text, email_attrs, html_count = utils.parse_email(file_path)

        # Empty text is more likely a SPAM
        if plain_text == "":
            self.predictions[filename] = "SPAM"
            return
            #TODO - check quality without this condition
        
        # Probabilities of email being spam or ham
        spam_score = ham_score = 0

        # Getting start spam and ham scores by words frequency algorithm
        spam_score, ham_score = self.test_text(plain_text)

        if "Subject" in email_attrs:
            for word in self.bad_words:
                if word in email_attrs["Subject"].lower():
                    spam_score += 100
                    #TODO - create bad words dictionary (word : cost)
        
        # if html_count > 10:
        #     spam_score += 50
        #TODO - test with html_count later

        # Final decision for current email
        self.predictions[filename] = "SPAM" if spam_score >= ham_score else "OK"


    def test_text(self, text):
        '''
        Tests text of email

        :param text: clean text (only words written with small letters) (string)
        :return:     counted spam_score and ham_score (tuple)
        '''
        # Start probability of email being a SPAM
        START_SPAM_PROB = 0.3

        text = text.strip().split()

        # Only common words for spam and ham are counted
        # self.spam_word_with_freq.keys() == self.ham_word_with_freq.keys()
        valid_words = [word for word in text if word in self.spam_word_with_freq]

        # Some mathematics here. Watch video from "used materials" for more info
        spam_probs = [self.spam_word_with_freq[word] for word in valid_words]
        ham_probs = [self.ham_word_with_freq[word] for word in valid_words]

        spam_score = sum([log(p) for p in spam_probs]) + log(START_SPAM_PROB)
        ham_score = sum([log(p) for p in ham_probs]) + log(1 - START_SPAM_PROB)

        return (spam_score, ham_score)
