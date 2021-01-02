import re

# Specifying grammar patterns
pattern_list = [ r"~([^%~\n ]*)", r"%([\w+][?\w]*)"]
token_regex = re.compile(r"{}|{}".format(pattern_list[1],pattern_list[0]))

def analyze_grammar(filepath):
    result = []
    # Opening grammar file
    with open(filepath, 'r') as reader:
        # Reading all lines
        lines = reader.readlines()

    # Removing blank lines
    while '\n' in lines: lines.remove('\n')

    # Finding all tokens
    for i in range(len(lines)):
        tokens = token_regex.findall(lines[i])
        tokens_list = []

        # Generating final list from entry
        for token in tokens:
            if (token[0]):
                tokens_list.append("%"+token[0])
            elif (token[1]):
                tokens_list.append("~"+token[1])

        # Adding new product rule
        result.append(tokens_list)

    return result


def print_grammar(grammar):
    for rule in grammar:
        tmp = list(rule)
        tmp[0] = tmp[0] + " := "
        result = " ".join(tmp)
        print(result)
