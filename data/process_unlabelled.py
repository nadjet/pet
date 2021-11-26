import pandas as pd
from nltk.tokenize import sent_tokenize

train_df = pd.read_csv("train_winery.csv", header=None)
test_df = pd.read_csv("test_winery.csv", header=None)

train_sentences = list(train_df[1].unique())
test_sentences = list(test_df[1].unique())

print(len(train_sentences), len(test_sentences))

sentences = []
count_excluded = 0
with open("unlabelled_winery.csv") as f:
	for line in f.readlines():
		sentence = sent_tokenize(line)[0]
		if sentence not in train_sentences and sentence not in test_sentences:
			sentences.append(sentence)
		else:
			count_excluded+=1
			print(f"Sentences excluded: {count_excluded}")

with open("unlabelled_winery0.csv","w") as f:
	for sentence in sentences:
		f.write(f"{sentence}\n")

