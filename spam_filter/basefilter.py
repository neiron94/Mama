import corpus
import utils
import os

class BaseFilter():

    def test(self, path):
        corp = corpus.Corpus(path)
        result = dict()

        for name, body in corp.emails():
            result[name] = self.test_one_mail(body)

        pred_path = os.path.join(path, "!prediction.txt")
        utils.write_classification_to_file(pred_path, result)

    
    def test_one_mail(self, text):
        ''' Returns "SPAM" or "OK" '''
        pass


    def train(self, path):
        pass
