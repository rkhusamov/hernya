import re

def camel_to_lowdash(word):
    res=''+word[0].lower()
    for letter in word[1:]:
        if letter.isupper():
            res+='_'+letter.lower()
        else:
            res+=letter
    return res


def remove_camel(string):
    camel=re.compile(r"([a-z]+([A-Z][a-z]+)+)|([A-Z][a-z]+){2,}")
    
    return re.sub(camel, camel_to_lowdash, string)

