# semantic-analysis-nlp
Created an algorithm to extract meaning from the text data, using spacy library.

ALGORITHM:

1.Take every sentence from the text.
2.Get all the verbs from the extracted sentence.
3.For every verb in the extracted sentence, store everything what is left to the verb in a separate list, and everything right to the verb in different list.
4.Do it for all the sentences.
5.Finally, create a csv file, with the columns “Left to the verb”, “Verb”, and “right to the verb”.

