def count_chars(text):
    txtleng = len(text)
    return(txtleng)

def count_words(text):
    wordcount = len(text.split())
    return(wordcount)

def count_sentences(text):
    count = text.count(".")
    count1 = text.count("!")
    count2 = text.count("?")
    product = count + count1 + count2
    return(product)