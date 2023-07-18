import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(tag):
    """
    Map POS tag to WordNet POS tag
    """
    if tag.startswith('J'):
        return 'a'  # adjective
    elif tag.startswith('V'):
        return 'v'  # verb
    elif tag.startswith('N'):
        return 'n'  # noun
    elif tag.startswith('R'):
        return 'r'  # adverb
    else:
        return 'n'  # noun (default)

def text_process(mess):
    # remove punctuations
    # remove stopwords
    # lemmatization
    # return clean message

    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    nostop = [word.lower() for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    pos_tags = pos_tag(nostop)
    clean_mess = [lemmatizer.lemmatize(word, pos=get_wordnet_pos(tag)) for word, tag in pos_tags]

    return clean_mess