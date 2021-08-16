# def reversal(arr):
#     return " ".join(reversed(arr.split()))

# print(reversal(" best the "))

def rev_word(s):

    words = []
    length = len(s)
    spaces = [' ']

    i = 0

    while i < length:

        if s[i] not in spaces:

            word_start = i
            while i < length and s[i] not in spaces:

                i += 1
            
            words.append(s[word_start:i])

        i+=1
    
    return reversal(words)

def reversal(s):
    length = len(s)
    word =[]
    i = -1
    while i >= (length +(length *-2)):
        word.append(s[i])
        i-=1

    return " ".join(word)

print(rev_word("        the best    tea in the world      "))