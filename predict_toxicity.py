import pandas as pd

df_keywords = pd.read_csv("toxic_keywords.csv")
toxic_keywords = df_keywords["keyword"].tolist()
comments = [
    "You're such an idiot!",  
    "Have a nice day!"        
]
for comment in comments:
    print(f"Checking comment: {comment}")
    text = comment.replace("http", "")
    cleaned = ""
    for char in text:
        if char.isalnum() or char in " ?!":
            cleaned += char
        elif char.isspace():
            cleaned += " "
    cleaned = " ".join(cleaned.strip().lower().split())
    is_toxic = False
    for word in toxic_keywords:
        if word in cleaned:
            is_toxic = True
            print(f"Toxic (The word used is: '{word}')")
            break
    if not is_toxic:
        print("Non-toxic")
      print()

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")
