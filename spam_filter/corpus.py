import os


class Corpus:
    '''
    Corpus to read email contents
    '''

    def __init__(self, path):
        '''
        Initialization of corpus

        :param path:    path to folder with emails (string)
        '''
        META_CHARS = "!."   # Characters of metafile begining

        self.SPAM_TAG = "SPAM"
        self.HAM_TAG = "OK"
        self.path = path
        self.files = [i for i in os.listdir(path) if i[0] not in META_CHARS]


    def emails(self):
        '''
        Reads emails (generator)

        :yield:    email filename and its content (tuple)
        '''
        for filename in self.files:
            content = self.open_file(filename)  # Read email content
            yield (filename, content)
        

    def open_file(self, filename):
        '''
        Reads file's content
        
        :param filename:    name of file to read (string)
        :return:            file content (string)
        :raise:             FileNotFoundError - Invalid directory of file
        '''
        try:    # Valid directory control 
            file_path = os.path.join(self.path, filename)
            with open(file_path, encoding="utf-8") as file:
                return file.read()   # Read file content
        except:
            print("ERROR: Invalid directory! (check if this directory exists)")
            raise FileNotFoundError
