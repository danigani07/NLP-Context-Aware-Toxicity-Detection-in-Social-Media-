import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from transformers import pipeline

df = pd.read_csv('toxic_comments.csv')
comments = df['comment'].tolist()
labels = df['label'].tolist()

X_train, X_test, y_train, y_test = train_test_split(comments, labels, test_size=0.2, random_state=42)
classifier = pipeline("text-classification", model="bert-base-uncased", tokenizer="bert-base-uncased")

predictions = [classifier(text)[0]['label'] for text in X_test]
predictions = [1 if pred == 'LABEL_1' else 0 for pred in predictions]

accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

def classify_comment(text):
    result = classifier(text)[0]  
    label = result['label']
    return "Toxic" if label == 'LABEL_1' else "Non-toxic"

input_text = "Oh brilliant, just what we needed more nonsense."
print("Example:", classify_comment(input_text))
