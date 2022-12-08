import corpus
import utils
import os

class TrainingCorpus(corpus.Corpus):

    def __init__(self, path_to_emails):
        super().__init__(path_to_emails)
        
        full_path = os.path.join(path_to_emails, "!truth.txt")

        self.truth_dict = utils.read_classification_from_file(full_path)

        spam_count = 0                                              # ADDED         Maybe it would be better to set
        for key, value in self.truth_dict.items():                  # ADDED         start_prob to ~0.3
            if value == "SPAM":                                     # ADDED         Because there are too much spam
                spam_count += 1                                     # ADDED         in out train/test sets
        self.START_SPAM_PROB = spam_count / len(self.truth_dict)    # ADDED

    
    def get_class(self, email_name):
        return self.truth_dict[email_name]


    def is_ham(self, email_name):
        return True if self.truth_dict[email_name] == "OK" else False


    def is_spam(self, email_name):
        return True if self.truth_dict[email_name] == "SPAM" else False


    def spams(self):
        emails = os.listdir(self.path_to_emails)

        for email in emails:
            if not email.startswith("!") and self.is_spam(email):
                full_path = os.path.join(self.path_to_emails, email)

                with open(full_path, "r", encoding='utf-8') as file:
                    body = file.read()

                yield (email, body)


    def hams(self):
        emails = os.listdir(self.path_to_emails)

        for email in emails:
            if not email.startswith("!") and self.is_ham(email):
                full_path = os.path.join(self.path_to_emails, email)

                with open(full_path, "r", encoding='utf-8') as file:
                    body = file.read()

                yield (email, body)
            