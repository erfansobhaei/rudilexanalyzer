import re

terminal_pattern = re.compile(r"~([^%~ ]*)")
nonterminal_pattern = re.compile(r"%([\w+][?\w]*)")
