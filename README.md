# rudilexanalyzer: Rudimentary Lexical Analyzer by Python
It's a simple lexical analyzer which accepts grammar with .txt extension, tokenize it, and store tokens in python list data structure. It can be useful for the later syntactical analyzer, like LR1 parser, LL1 parser, etc.<br> Provided grammars in this repository are based on [Java Language Grammars](https://docs.oracle.com/javase/specs/jls/se12/html/jls-2.html#jls-2.1).

## Grammar notation conventions
For more readability and ease of analyzing input grammar should have the following requirements:

 1. Each line of the text file should have only one product rule.
 2. Each non-terminal token should start with ```%``` character.
 3. Each terminal token should start with ```~``` character.
 4. Non-terminals should contain only ASCII alphabetical characters, digits, or underscores ```_```.
 5. Terminals can consist of "any" character except ```%``` and ```~``` and space.
 6. Immediately after the left-hand side of the rule these characters ```:=``` are necessary.
 7. Analyzer will ignore all characters out of the mentioned rules.
 
 ## How to Write Grammar
 Following simple grammar is a part of Java language grammar:
 ```
BreakStatement:
    break ;
    break Identifier ;
 ```
 Terminals are keyword ```break``` and semicolon ```;```.<br>
 Non-terminals are ```BreakStatement``` and ```Identifier```.<br>
 As mentioned notations are necessary this grammar should written like this in .txt file:
 ```
 %BreakStatement := ~break ~;
 %BreakStatement := ~break %Identifier ~;
 ```
 
 ## How to Run Code Snippet
 It's just a python script. Provide grammar rules in a text file in the same directory. Then call ```analyze_grammar``` function for tokenizing grammar. Its argument is path to the text file. There is an auxiliary function, ```print_grammar```, which is for printing grammar line by line. You could pass returned object of first call to the latter function in order to examine results.<br>
 
 This Project is a part of *Compiler Design* course which is one of *Kharazmi University*'s courses.
