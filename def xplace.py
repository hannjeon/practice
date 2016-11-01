def xplace(text):

    for i in text:
        if i == text[0]:
            i.replace('x')

    return text

print xplace('Hello!')
