def read_classification_from_file(file_name):
    data = dict()
    with open(file_name, "r", encoding='utf-8') as file:
        for line in file:
            words = line.strip().split()
            # words[0] - name of email, words[1] - SPAM/OK
            data[words[0]] = words[1]
    return data


def write_classification_to_file(file_name, data):
    with open(file_name, "w", encoding='utf-8') as file:
        # data is dictionary, where key - name of file, value - SPAM/OK
        for mail, status in data.items():
            file.write(mail + ' ' + status + '\n')
