from jaygen.answer_long import generate_answer, generate_question

sentence="Mental illness, also called mental health disorders, refers to a wide range of mental health conditions — disorders that affect your mood, thinking and behavior. Examples of mental illness include depression, anxiety disorders, schizophrenia, eating disorders and addictive behaviors."
questions=[]
answers=[]
questions=generate_question(sentence)
for question in questions:
 #   answer=generate_answer(question, sentence)
  #  answers.append(answer)
   print("Question:", question)
    #print("Answer:", answer)
