import os

class Corpus():
    def __init__(self, path_to_emails):
        self.path_to_emails = path_to_emails


    def emails(self):
        emails = os.listdir(self.path_to_emails)

        for email in emails:
            if not email.startswith("!"):   # if not a file with metainformation
                full_path = os.path.join(self.path_to_emails, email)

                with open(full_path, "r", encoding='utf-8') as file:
                    body = file.read()

                yield (email, body)
