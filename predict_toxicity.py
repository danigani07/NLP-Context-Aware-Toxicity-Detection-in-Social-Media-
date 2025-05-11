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
