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
