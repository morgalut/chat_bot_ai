import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

# Ensure the necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def tokenize_and_tag(text):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    return tagged

def identify_named_entities(tagged_tokens):
    entities = ne_chunk(tagged_tokens)
    return entities
