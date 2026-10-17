
import pandas as pd
import re
import string
import math

# Load dataset
df = pd.read_csv("Week7\\IMDB Dataset.csv")

# Punctuation and stop words
table = str.maketrans("", "", string.punctuation)

stop = {"the","is","a","an","and","of","to","in","this","was","it","i","very","are","on"}

# 1. Lowercasing
# 2. Remove HTML
# 3. Remove URLs
# 4. Remove punctuation
# 5. Stop words removal
# 6. Tokenization

def preprocess(text):
    text = text.lower()
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    text = text.translate(table)
    return [w for w in re.findall(r"\w+", text) if w not in stop]

tok = df["review"].apply(preprocess).tolist()

print(tok[0])

# 7. Term Frequency (TF)
# 8. TF-IDF

tf  = lambda t, d: d.count(t) / len(d)
idf = lambda t: math.log(len(tok) / sum(t in d for d in tok))

for t in ["movie", "film", "good", "bad"]:
    print(t, "tf =", round(tf(t, tok[1]), 2), "idf =", round(idf(t), 2),
          "tf-idf =", round(tf(t, tok[1]) * idf(t), 2))
