from transformers import pipeline

nlp = pipeline("question-answering")

context = "Natural Language Processing (NLP) is a subfield of linguistics, computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human languages."

questions = nlp(context)

for question in questions:
    print(question["question"])
