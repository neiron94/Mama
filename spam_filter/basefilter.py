from corpus import Corpus
import utils
import os


class BaseFilter:
    '''
    Base Filter functionality
    '''

    def __init__(self):
        '''
        Initialization of filter
        '''
        self.predictions = {} # Dictionary of predictions filter made


    def train(self, path):
        '''
        Function to filter learning
        :param path:    path to folder with emails (string)
        '''
        pass


    def test(self, path):
        '''
        Function to write result of predictions
        :param path:    path to folder with emails (string)
        '''
        OUTP = "!prediction.txt"  # Filename to write result of prediction

        corpus = Corpus(path)   # Filter's corpus
        for file in corpus.emails():   # Make predictions
            self.predict(path, file[0])

        # Write predictions to file
        prediction_path = os.path.join(path, OUTP)
        utils.write_classification_to_file(prediction_path, self.predictions)

    
    def predict(self, path, filename):
        '''
        Function to make prediction
        Side effects: Fill self.predictions with {filename:prediction}
        :param path:        path to directory with tested emails (string)
        :param filename:    name of email (string)
        '''
        pass
