"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    # TODO: Count the number of occurences of each word in s
    string = s.split(" ")
    # set comprehension so we only have unique values
    
   # li=[]
  #  for word in string:
   #     li.append((word,string.count(word)))
    
   # print li

    wordcount = {word: string.count(word) for word in string}
#    print wordcount
    wordcounttup = [(word, count) for word, count in wordcount.items()]

    wordcounttup.sort(key=lambda tup: (-tup[1], tup[0]))

    top_n = wordcounttup[:n]

    return top_n
             
    