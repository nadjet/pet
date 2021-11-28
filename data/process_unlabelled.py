import pandas as pd
from nltk.tokenize import sent_tokenize
from csv import writer

train_df = pd.read_csv("train.csv", header=None)
test_df = pd.read_csv("test.csv", header=None)
dev_df = pd.read_csv("dev.csv", header=None)

train_sentences = list(train_df[1].unique())
test_sentences = list(test_df[1].unique())
dev_sentences = list(dev_df[1].unique())

print(len(train_sentences), len(test_sentences))

sentences = []
count_excluded = 0
with open("unlabeled.csv") as f:
	for line in f.readlines():
		sentence = sent_tokenize(line)[0]
		if sentence not in train_sentences and sentence not in test_sentences and sentence not in dev_sentences:
			sentences.append(sentence)
		else:
			count_excluded+=1
			print(f"Sentences excluded: {count_excluded}")

# create csv of unlabelled data with train, test or dev without data in tra
with open("unlabeled0.csv","w") as f:
	wr = writer(f, delimiter=",")
	for sentence in sentences:
		wr.writerow(["",sentence])

