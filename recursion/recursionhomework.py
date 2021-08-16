def sum_func(n):

    #Base Case
    if len(str(n)) == 1:
        return n
    
    else:
        return n%10 + sum_func(n//10)

print(sum_func(4321))

def word_split(phrase, list_of_words, output = None):
    if output is None:
        output = []

    for word in list_of_words:

        if phrase.startswith(word):

            output.append(word)

            return word_split(phrase[len(word):], list_of_words, output)
    
    return output

print(word_split('iamlegend',['i', 'am', 'out','legend']))
