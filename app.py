from pprint import pprint
from Questgen import main


payloadtext = "India is a great country where people speak different languages but the national language is Hindi. " \
              "India is full of different castes, creeds, religion, and cultures but they live together. That’s the " \
              "reasons India is famous for the common saying of “unity in diversity“. India is the seventh-largest" \
              "country in the whole world."

print("1-Yes-No")
print("2-Mcq")
print("3-Faq")
print("4-Predict answer")

i = input("choice")

if i == '1':
    qe = main.BoolQGen()
    payload = {
        "input_text": payloadtext,
        "max_questions": 6
    }

    output = qe.predict_boolq(payload)
    pprint(output)
elif i == '2':
    qg = main.QGen()
    payload = {
        "input_text": payloadtext
    }
    output = qg.predict_mcq(payload)
    pprint(output)
elif i == '3':
    qg = main.QGen()
    payload = {
        "input_text": payloadtext
    }
    output = qg.predict_shortq(payload)
    pprint(output)
elif i == '4':
    qg = main.AnswerPredictor()
    payload = {
        "input_text": payloadtext,
        "input_question": "which is the seventh largest country?"
    }
    output = qg.predict_answer(payload)
    pprint(output)
