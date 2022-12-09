from corpus import Corpus
import utils
import os


class TrainingCorpus(Corpus):
    '''
    Corpus to train filter
    '''

    def __init__(self, path):
        super().__init__(path)

        data_path = os.path.join(self.path, "!truth.txt")
        self.data = utils.read_classification_from_file(data_path)


    def get_class(self, filename):
        '''
        Function to get file clasification from thruth file

        :param filename:    name of file with email (string)
        :return:            clasification of email (string)
        '''
        if self.data[filename] == self.SPAM_TAG:
            return self.SPAM_TAG
        else: 
            return self.HAM_TAG


    def is_spam(self, filename):
        '''
        Function to recognise spam email

        :param filename:    name of file with email (string)
        :return:            True if it's spam message, False if not (bool)
        '''
        return True if self.get_class(filename) == self.SPAM_TAG else False


    def is_ham(self, filename):
        '''
        Function to recognise ham email

        :param filename:    name of file with email (string)
        :return:            True if it's ham message, False if not (bool)
        '''
        return True if self.get_class(filename) == self.HAM_TAG else False


    def spams(self):
        '''
        Function (generator) to read spam emails

        :return:    email filename and its content (tuple)
        '''
        PLAIN_TEXT = 0  # Index of text in returned tuple after parsing email

        for filename in self.files:
            if self.is_spam(filename):
                file_path = os.path.join(self.path, filename)
                plain_text = utils.parse_email(file_path)[PLAIN_TEXT]
                yield plain_text


    def hams(self):
        '''
        Function (generator) to read ham emails

        :return:    email filename and its content (tuple)
        '''
        PLAIN_TEXT = 0  # Index of text in returned tuple after parsing email

        for filename in self.files:
            if self.is_ham(filename):
                file_path = os.path.join(self.path, filename)
                plain_text = utils.parse_email(file_path)[PLAIN_TEXT]
                yield plain_text
