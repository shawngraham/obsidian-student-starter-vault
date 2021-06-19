import operator, collections, os, sys, re, string, nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.util import pr
from tabulate import tabulate

import pandas as pd
import numpy as np

# spacy for lemmatization
import spacy

# cosine similarity
import warnings
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# TFIDF
from sklearn.feature_extraction.text import TfidfVectorizer

## README
#v1.2
# Place it at the root of your notes folder. `cd` to it and run the script with:
# `python3 similarity.py path/to/your/target/file.md`

rootdir = "."
# cwd = os.getcwd()
# print(cwd)
rootdir = "/Users/shawngraham/Documents/obsidian-experiments/student-starter-vault/" #PUT THE DIRECTORY TO YOUR VAULT ROOT HERE !!!
target = sys.argv[1]

similarity_threshold = 0.1

stop_words = set(stopwords.words('english')).union(set(stopwords.words('english')))
md_regex = re.compile(r'.*md$')
tag_regex = re.compile(r'#([-_\d\w]+)')
link_regex = re.compile(r'\[\[(.*?)[|#]')

# Initialize spacy 'en' model, keeping only tagger component (for efficiency)
# python3 -m spacy download en

nlp = spacy.load("en_core_web_sm", disable=['parser', 'ner'])

#nlp = spacy.load('en', disable=['parser', 'ner'])

def read(file):
	with open(file, 'r') as f:
		content = f.read()
		f.close()
	return content.lower()

def remove_numbers(input_str):
	result = re.sub(r'\d+', '', input_str)
	return result

def remove_whitespace(input_str):
	result = re.sub(r'[\t\n\r]', '', input_str)
	return result

def remove_punctuation(input_str):
	result = input_str.translate(str.maketrans('', '', string.punctuation))
	return result

def remove_stopwords(input_str):
	tokens = word_tokenize(input_str)
	result = [i for i in tokens if not i in stop_words]
	return result

def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
	"""https://spacy.io/api/annotation"""
	texts_out = []
	# for sent in texts:
	doc = nlp(" ".join(texts))
	texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
	return texts_out[0]

## TFIDF Similarity
def get_vectors(target, other):

	# target = nlp(" ".join(target))
	other = nlp(" ".join(other))
	corpus = [str(target), str(other)]
	# print(corpus)
	vect = TfidfVectorizer(min_df=1)
	tfidf = vect.fit_transform(corpus)
	pairwise_similarity = tfidf * tfidf.T
	# print(pairwise_similarity.toarray())
	return pairwise_similarity.toarray()[0][1]

## Processing

def preprocess(file):

	out = lemmatization(remove_stopwords(remove_whitespace(remove_punctuation(remove_numbers(read(file))))))
	# print(out)
	# lemms = lemmatization(out)
	# print(lemms)
	return out

def extract_keywords(input_str):
	tags = set(re.findall(tag_regex, input_str))
	links = set(re.findall(link_regex, input_str))
	# print(tags.union(links))
	return tags.union(links)

def jaccard_similarity(list1, list2):
	intersection = set(list1).intersection(set(list2))
	union = set(list1).union(set(list2))
	if len(union)>0:
		return float(len(intersection) / len(union))
	else: return 0.0

def df_to_markdown(df, y_index=False):
	blob = tabulate(df, headers='keys', tablefmt='pipe')
	if not y_index:
		# Remove the index with some creative splicing and iteration
		return '\n'.join(['| {}'.format(row.split('|', 2)[-1]) for row in blob.split('\n')])
	return blob

raw_target = read(sys.argv[1])
# print(str(sys.argv))

preprocessed_target = preprocess(sys.argv[1])
preprocessed_target_joined = nlp(" ".join(preprocessed_target))

# exit()
table = []
tableTFIDF = []

for root, dirs, files in os.walk(rootdir):
	for other_file in files:
		if md_regex.match(other_file):
			other_file_path = os.path.join(root, other_file)

			preprocessed_other = preprocess(other_file_path)



			raw_other = read(other_file_path)
			filename = other_file

			filename = filename[:-3]
			# filename = "[["+filename+"]]"

			# print(filename)

			tfidf_score = get_vectors(preprocessed_target_joined, preprocessed_other)
			# print(tfidf_score)

			text_similarity = jaccard_similarity(preprocessed_target, preprocessed_other)

			keyword_similarity = jaccard_similarity(extract_keywords(raw_target), extract_keywords(raw_other))



			# print(extract_keywords(raw_other))
			similarity = (0.5*text_similarity) + (0.5*keyword_similarity)
			tfidf_similarity = (0.5*tfidf_score) + (0.5*keyword_similarity)
			#print(similarity)
			if similarity > similarity_threshold:
				# print(other_file)
				# print(text_similarity)
				# print(preprocessed_other)

				row = [filename, round(similarity,3), text_similarity, tfidf_score, tfidf_similarity]
				table.append(row)

			if tfidf_similarity > similarity_threshold:
				# print(other_file)
				# print(text_similarity)
				# print(preprocessed_other)

				row = [filename, round(similarity,3), text_similarity, tfidf_score, tfidf_similarity]
				tableTFIDF.append(row)


data = np.array(table)
df = pd.DataFrame(data, columns=['filename', 'score', 'text_similarity', 'tfidf', 'tfidf_similarity'])
df = df.sort_values(by=['score'], ascending = False)
df = df.drop_duplicates()
# print(df)

tableOutput = "## Similar Notes \n"
tableOutput += df_to_markdown(df)
print(tableOutput)
sys.stdout.flush()


data = np.array(tableTFIDF)
df = pd.DataFrame(data, columns=['filename', 'score', 'text_similarity', 'tfidf', 'tfidf_similarity'])
df = df.sort_values(by=['tfidf_similarity'], ascending = False)
df = df.drop_duplicates()
# print(df)

tableOutput = "## Similar Notes TFIDF \n"
tableOutput += df_to_markdown(df)
print(tableOutput)
sys.stdout.flush()

# print(tabulate(table, headers=['File', 'Score']))
