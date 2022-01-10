import pandas as pd
import stanza
import csv

stanza.download('en')

nlp = stanza.Pipeline(lang='en', processors='tokenize')


num = 600
train_df = pd.read_csv("train.csv", header=None)
test_df = pd.read_csv("test.csv", header=None)
dev_df = pd.read_csv("dev.csv", header=None)

train_sentences = list(train_df[1].unique())
test_sentences = list(test_df[1].unique())
dev_sentences = list(dev_df[1].unique())

print(len(train_sentences), len(test_sentences))

import re
sentences = []
count_excluded = 0
csv.register_dialect('mydialect', delimiter=',', quoting=csv.QUOTE_ALL, doublequote=True)
df = pd.read_csv("unlabeled_original.csv", dialect='mydialect', header=None)

df = df.sample(num)
for i,sentence in enumerate(list(df[0])):
	print(f"{i}/{len(list(df[0]))}")
	doc = nlp(sentence)
	for sentence in doc.sentences:
		if sentence not in train_sentences and sentence not in test_sentences and sentence not in dev_sentences:
			sentences.append(sentence.text)
		else:
			count_excluded+=1
			print(f"Sentences excluded: {count_excluded}")
		break

# create csv of unlabelled data with train, test or dev without data in tra


with open("unlabeled.csv","w") as f:
	wr = csv.writer(f, delimiter=",")
	for sentence in sentences:
		wr.writerow(["",sentence])

