from transformers import AutoTokenizer, AutoModelForQuestionAnswering

tokenizer = AutoTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")

model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")

# Define a function to generate context questions
# Tokenize the context
context ="Artificial intelligence (AI) is intelligence—perceiving, synthesizing, and inferring information—demonstrated by machines, as opposed to intelligence displayed by non-human animals and humans. Example tasks in which this is done include speech recognition, computer vision, translation between (natural) languages, as well as other mappings of inputs."
inputs = tokenizer(context, return_tensors="pt")

# Generate question(s) from the context using the model
outputs = model.generate(**inputs, max_length=32, num_beams=4)
questions = tokenizer.batch_decode(outputs, skip_special_tokens=True)
print(questions)

