import re

def camel_to_lowdash(word):
    word=word.group(0)
    res=''+word[0].lower()
    for letter in word[1:]:
        if letter.isupper():
            res+='_'+letter.lower()
        else:
            res+=letter
    return res

def remove_camel(text_string):
    camel=re.compile(r"([a-z]+([A-Z][a-z]+)+)|([A-Z][a-z]+){2,}")
    return re.sub(camel, camel_to_lowdash, text_string)

