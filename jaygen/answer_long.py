import nltk
from nltk.stem import PorterStemmer
from nltk.text import Text
from nltk.chunk import ne_chunk
from nltk.parse import DependencyGraph
from rake_nltk import Rake
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import sent_tokenize


def generate_question(text):
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize
    from nltk.probability import FreqDist
    from nltk.tag import pos_tag
    from nltk.chunk import ne_chunk

    # Load the text you want to analyze
    text = "The quick brown fox jumps over the lazy dog. John Smith is a software engineer at Google. He loves to travel to new places and try new foods."

    # Tokenize the text into sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    # Remove stop words and punctuation
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words and word.isalpha()]

    # Perform part-of-speech tagging and named entity recognition
    pos_tags = pos_tag(words)
    ne_chunks = ne_chunk(pos_tags)

    # Identify the most frequent words and phrases
    fdist = FreqDist(words)
    top_words = fdist.most_common(5)

    # Identify the named entities and their types
    named_entities = []
    for chunk in ne_chunks:
        if hasattr(chunk, 'label') and chunk.label() == 'NE':
            named_entities.append(' '.join(c[0] for c in chunk))

    # Generate open-ended questions based on the identified salient parts
    questions = []
    for named_entity in named_entities:
        questions.append(f"What is {named_entity}?")
    for top_word in top_words:
        questions.append(f"What is the significance of {top_word[0]} in the text?")

    return questions


# Define a corpus(text) to search for answers
def generate_answer(question, corpus):
    # Define a list of stop words to remove from the corpus
    stop_words = set(stopwords.words('english'))

    # Tokenize the corpus
    corpus_tokens = word_tokenize(corpus)

    # Remove stop words and stem the remaining words
    ps = PorterStemmer()
    filtered_tokens = [ps.stem(token.lower()) for token in corpus_tokens if token.lower() not in stop_words]

    # Calculate the frequency distribution of the filtered tokens
    freq_dist = FreqDist(filtered_tokens)

    # Get the most common words from the frequency distribution
    most_common_words = freq_dist.most_common(10)

    # Convert the corpus to a Text object for easier analysis
    corpus_text = Text(corpus_tokens)

    # Get the sentences from the corpus that contain the most common words
    relevant_sentences = []
    for word, freq in most_common_words:
        sentences = [sent for sent in sent_tokenize(corpus) if word in word_tokenize(sent)]
        relevant_sentences.extend(sentences)

    # Generate a summary of the relevant sentences
    summary = ' '.join(relevant_sentences)

    # Print the summary as the answer to the question
    #print(summary)
    return summary

