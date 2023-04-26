import string
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import defaultdict, OrderedDict
from sense2vec import sense2vec as s2v
import numpy
#for distractors
import random
from nltk.corpus import wordnet

from Questgen.mcq.mcq import edits

# download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# read in the text to generate questions from
text = "Dozens of mental illnesses have been identified and defined. They include depression, generalized anxiety disorder, bipolar disorder, obsessive-compulsive disorder, post-traumatic stress disorder, schizophrenia, and many more."

# preprocess the text
sentences = sent_tokenize(text)
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# define a dictionary to store words and their frequencies
word_freq = defaultdict(int)
for sentence in sentences:
    words = word_tokenize(sentence.lower())
    for word in words:
        if word not in stop_words:
            word = lemmatizer.lemmatize(word)
            word_freq[word] += 1

# sort the words by frequency
sorted_words = sorted(word_freq, key=word_freq.get, reverse=True)

# select the top 5 most frequent words to generate questions from
top_words = sorted_words[:5]

# define a function to generate questions from a sentence
def generate_distractors(word):
    output = []
    distractors = []

    word_preprocessed =  word.translate(word.maketrans("","", string.punctuation))
    word_preprocessed = word_preprocessed.lower()

    word_edits = edits(word_preprocessed)

    word = word.replace(" ", "_")

    sense = sense2vec   (word)
    most_similar = s2v.most_similar(sense, n=15)

    compare_list = [word_preprocessed]
    for each_word in most_similar:
        append_word = each_word[0].split("|")[0].replace("_", " ")
        append_word = append_word.strip()
        append_word_processed = append_word.lower()
        append_word_processed = append_word_processed.translate(append_word_processed.maketrans("","", string.punctuation))
        if append_word_processed not in compare_list and word_preprocessed not in append_word_processed and append_word_processed not in word_edits:
            output.append(append_word.title())
            compare_list.append(append_word_processed)


    distractors= list(OrderedDict.fromkeys(output))
    distractors = random.sample(distractors, min(3, len(distractors)))
    return distractors

def generate_questions(sentence):
    questions = []
    answers= []
    distt= []
    for word in top_words:
        if word in sentence.lower():
            question = sentence.replace(word, "______")
            dist=generate_distractors(word)
            distt.append(dist)
            answers.append(word)
            questions.append(question)
    return questions, answers, distt

# generate questions for each sentence in the text
for sentence in sentences:
    questions, answers, distt = generate_questions(sentence)
    if questions:
        print("Original Sentence:", sentence)
        for question,answer,dist in zip(questions,answers,distt):
            print("Question:", question)
            print("Answer", answer)
            print("distractors", dist)


