from email.parser import BytesParser
from email.policy import default
import re
import string

path = "materials/data/1/"
file_name = "00002.9438920e9a55591b18e60d1ed37d992b"
file_path = path + file_name

with open(file_path, 'rb') as fp:
    msg = BytesParser(policy=default).parse(fp)

# msg.keys() - System fields
# msg.values() - Values of system fields
# msg.get_payload() - Email Body

msg_body = msg.get_payload().lower()

# Clean from html tags
pattern = r"<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>"
count_html_tag = len(re.findall(pattern, msg_body))
plain_text = re.compile(pattern).sub('', msg_body)

# Clean from gaps in words 
pattern = r"""=
"""
plain_text = re.compile(pattern).sub('', plain_text)

# Clean from numbers 
pattern = r"\d+"
plain_text = re.compile(pattern).sub('', plain_text)

# Clean from punctiation
plain_text = plain_text.translate(str.maketrans("", "", string.punctuation))

print(plain_text)

