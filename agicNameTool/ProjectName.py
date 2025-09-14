import re

def projectName(name):

    newName = re.sub(r'Issue ', 'ATC_', name)
    newName = re.sub(r': ', '_', newName)
    newName = re.sub(r'"', '', newName)
    newName = re.sub(r"'", ' ', newName)
    newName = re.sub(r",", ' ', newName)

    newName = toCamelCase(newName)

    return newName

def toCamelCase(text):
    parts = text.split('_')
    result = []
    
    for part in parts:
        if part.isdigit() or part.isupper():
            result.append(part)
        else:
            # Converte spazi in camelCase
            words = part.split()
            camel_part = ''.join(word.capitalize() for word in words)
            result.append(camel_part)
    
    return '_'.join(result)