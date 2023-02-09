#step 1:
x = 'was'
y = 'is'

x == y

#step 2:
from nltk.stem import WordNetLemmatizer

#create a lemmatizer instance which later could be used to get the root
lemmatizer = WordNetLemmatizer()

#step 3:
# to download the wordnet
import nltk
nltk.download('wordnet')

#step 2:
#use the above created lemmatizer instance to get the root 'lemma'
lemma_x = lemmatizer.lemmatize(x, 'v') # verb

lemma_y = lemmatizer.lemmatize(y, 'v') # verb

print(lemma_x==lemma_y)




