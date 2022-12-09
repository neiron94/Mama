from email.parser import BytesParser
from email.policy import default
import re

# Define main constants
EOL = "\n"  # "End of line" character
SEP = " "   # Separator character

def read_classification_from_file(filename):
    '''
    Function to read file and clasificate its content

    :param filename:   name of input file (string)
    :return:           clasification result (dict)
    '''
    result = {}
    with open(filename, encoding="utf-8") as file:
        for line in file:
            line = line.strip().split(SEP)  # Read and process raw line in file
            # First processed element - name of file, second - its clasification
            result[line[0]] = line[1]        
            
    return result


def write_classification_to_file(filename, data):
    '''
    Function to write clasification to output file

    :param filename:    name of output file (string)
    :param data:        clasification to write (dict)
    '''
    with open(filename, "a", encoding="utf-8") as file:
        for name, clasification in data.items():
            line = name + SEP + clasification + EOL     # Make output line
            file.write(line)                            # Write output line


def parse_email(file):
    '''
    Function to parse file with email message
    Returns tuple with plain (cleared) text of message, 
    email system attributes and count of used html tags in message 

    :param file:    file with full path (string)
    :return:        information about parsed email (tuple)
    '''
    with open(file, 'rb') as email:
        content = BytesParser(policy=default).parse(email)

    text = content.get_payload()
    if type(text) == str:   # Valid email text control
        plain_text, html_count = clean_text(text)
    else:   # In this case, text is strange reference to another email
        plain_text, html_count = "", 0

    email_attrs = {i:content[i] for i in content.keys() if i != "Date"}

    return (plain_text, email_attrs, html_count)


    
def clean_text(text):
    '''
    Function to clean raw text from email message

    :param text:    raw text to clean (string)
    :return:        plain cleaned text and count of deleted html tags (tuple)
    '''
    # Make all letters lowercased
    text = text.lower()

    # Clean from html tags
    pattern = r"<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>"
    count_html = len(re.findall(pattern, text))
    plain_text = re.compile(pattern).sub('', text)

    # Clean from gaps in words 
    pattern = r"""=
    """
    plain_text = re.compile(pattern).sub('', plain_text)

    # Clean from numbers 
    pattern = r"\d+"
    plain_text = re.compile(pattern).sub('', plain_text)

    # Clean from punctiation
    pattern = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    plain_text = plain_text.translate(str.maketrans("", "", pattern))

    return (plain_text, count_html)
