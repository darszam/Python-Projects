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