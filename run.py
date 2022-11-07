from pipelines import pipeline

nlp = pipeline("e2e-qg")
output = nlp("Python is a programming language. Created by Guido van Rossum and first released in 1991.")
print(output)
