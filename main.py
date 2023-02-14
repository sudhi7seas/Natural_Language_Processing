#Step 1:
# To download the wordnet
import nltk
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

#create a lemmatizer instance which later could be used to get the root
lemmatizer = WordNetLemmatizer()

#Step 4:
#Download the punkt pakage
nltk.download('punkt')

#Step 2:
#sentence = 'Vegetables are types of plants.'

#Step 3:
#Tokenizing the sentences
# use sentence.lower() for the lower case version of the sentence
#sentence_tokens = nltk.word_tokenize(sentence.lower())

#Step 7:
# Download the 'averaged_perceptron_tagger'
nltk.download('averaged_perceptron_tagger')

#Step 6:
#Create pos_tags (part of speech tags) for each tokens. As we are not sure of the lemma type as verb or noun.


#Step 5 and Step 8:
# Iterate over each tokens and pass these words into lemmatize method


def lemma_fun(sent):
  sentence_tokens = nltk.word_tokenize(sent.lower())
  pos_tags = nltk.pos_tag(sentence_tokens)
  
  sentence_lemmas = []
  for token, pos_tag in zip(sentence_tokens, pos_tags):
    if pos_tag[1][0].lower() in ['n','v','a','r']:
      lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
      sentence_lemmas.append(lemma)

#Call the function and compare 2 sentences
l1 = lemma_fun('Vegetables are types of plants.')

l2 = lemma_fun('A vegetable is a type of plant')

print(l1==l2)





