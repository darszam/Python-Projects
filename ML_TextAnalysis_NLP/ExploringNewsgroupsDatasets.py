from nltk.corpus import names
print (names.words()[:10])

print(len(names.words()))
from sklearn.datasets import fetch_20newsgroups
import numpy as np
groups = fetch_20newsgroups()
print(groups.keys())

print(groups['target_names'])

print(groups.target)

import seaborn as sns
sns.distplot(groups.target)

import matplotlib.pyplot as plt
plt.show()

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(stop_words="english", max_features=500)
transformed = cv.fit_transform(groups.data)
print(cv.get_feature_names())

sns.distplot(np.log(transformed.toarray().sum(axis=0)))
plt.xlabel('Log Count')
plt.ylabel('Frequency')
plt.title('Distribution plot of 500 word counts')
plt.show()