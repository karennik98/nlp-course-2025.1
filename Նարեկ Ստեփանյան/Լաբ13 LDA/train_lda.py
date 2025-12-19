from sklearn.datasets import fetch_20newsgroups
from gensim.parsing.preprocessing import STOPWORDS
from gensim.corpora import Dictionary
import re
import os
from gensim.models import LdaModel

newsgroups = fetch_20newsgroups(subset='train', remove=('headers', 'footers', 'quotes'))
docs = newsgroups.data[:1000]

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = text.split()
    tokens = [t for t in tokens if t not in STOPWORDS and len(t) >= 3]
    return tokens

processed_docs = [preprocess(doc) for doc in docs]

dictionary = Dictionary(processed_docs)
dictionary.filter_extremes(no_below=5, no_above=0.5)
corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

lda_model = LdaModel(
    corpus=corpus,
    id2word=dictionary,
    num_topics=10,
    passes=15,
    alpha='auto',
    eta='auto',
    random_state=42
)

os.makedirs("models", exist_ok=True)
lda_model.save("models/lda_model.model")
dictionary.save("models/dictionary.dict")

print('Discovered Topics:')
for idx, topic in lda_model.print_topics(num_words=15):
    print(f'Topic {idx}: {topic}')