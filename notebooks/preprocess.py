import contractions
from nltk.corpus import stopwords
import re
from collections import Counter
import itertools
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import RegexpTokenizer
from textblob import Word
import spacy
import emoji
import nltk

nltk.download('stopwords')
# load french model
nlp = spacy.load("fr_core_news_sm")

# french stopwords
stop_words = stopwords.words('french')

print(stop_words)


def expand_contractions(text):
    return contractions.fix(text)


def convert_emojis_and_emoticons_to_word(text):
    # convert emojis to text
    text = emoji.demojize(text)
    return text


# tokenization with french text as input
def tokenization(text):
    token = RegexpTokenizer(r'\w+')
    tokenized = token.tokenize(text)
    return " ".join(tokenized)


def remove_stop_words(text):
    res = []
    for w in text.split():
        if w not in stop_words:
            res.append(w)
    return " ".join(res)[:-1]


def lemmatize_text(text):
    # Tokenizer le text en mots
    words = word_tokenize(text)

    # Initializer le legitimatise
    lemmatizer = WordNetLemmatizer()

    # Lemmatiser chaque mot
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

    # Rejoindre les mots lemmatisés en une chaîne de caractères
    lemmatized_text = ' '.join(lemmatized_words)

    return lemmatized_text


def preprocessTweet(tweetText):
    # expansion des contractions
    expanded_r = expand_contractions(tweetText)
    # remplacement des emojis par leur sens textuel
    emoji_r = convert_emojis_and_emoticons_to_word(expanded_r)
    # tokenization
    tokenized_r = tokenization(emoji_r)
    # suppression des mots d'arret
    removed_stop_w_r = remove_stop_words(tokenized_r)
    # lemmatization du texte
    lemmatized_r = lemmatize_text(removed_stop_w_r)
    return lemmatized_r


if __name__ == "__main__":
    print(preprocessTweet("J'ai vraiment ❤️ ce film, c'était génial !"))
