import re

# Specifying grammar patterns
pattern_list = [ r"~([^%~ ]*)", r"%([\w+][?\w]*)"]
terminal_regex = re.compile(pattern_list[0])
nonterminal_regex = re.compile(pattern_list[1])
token_regex = re.compile(r"{}|{}".format(pattern_list[0],pattern_list[1]))

# Opening grammar file
with open("grammar_comment.txt", 'r') as reader:
    # Reading all lines
    lines = reader.readlines()

    # Removing blank lines
    while '\n' in lines: lines.remove('\n')

    # Finding all terminals and nonterminals
    tokens = token_regex.findall(s)

    
