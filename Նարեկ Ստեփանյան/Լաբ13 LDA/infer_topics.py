from gensim.models import LdaModel
from gensim.corpora import Dictionary
from gensim.parsing.preprocessing import STOPWORDS
import re
import json

lda_model = LdaModel.load('models/lda_model.model')
dictionary = Dictionary.load('models/dictionary.dict')

with open('models/topic_labels.json') as f:
    topic_labels = json.load(f)

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = text.split()
    tokens = [t for t in tokens if t not in STOPWORDS and len(t) >= 3]
    return tokens
def classify_document(text):
    tokens = preprocess(text)
    bow = dictionary.doc2bow(tokens)
    topic_dist = lda_model[bow]
    top_topics = sorted(topic_dist, key=lambda x: x[1], reverse = True)[:3]
    return top_topics
def display_results(text, top_topics):
    print('\n' + '='*60)
    print('INPUT DOCUMENT PREVIEW:')
    print(text[:200] + '...' if len(text) >200 else text)
    print('\nTOP 3 TOPICS:')

    for topic_id, prob in top_topics:
        name = topic_labels.get(str(topic_id), f'Topic {topic_id}')
        words = [w for w,p in lda_model.show_topic(topic_id, topn=5)]
        print(f' →{name} (prob: {prob:.3f}')
        print(f'    Words: {','.join(words)}')
    print('='*60)
print('LOADED TOPICS:')
for i in range(10):
    name = topic_labels.get(str(i), f'Topic {i}')
    words = [w for w,p in lda_model.show_topic(i, topn=5)]
    print(f' Topic {i}: {name} → {', '.join(words)}')
print()

samples = [
    "The new graphics card delivers amazing performance for gaming. The GPU can handle 4K resolution easily with ray tracing enabled. Gamers will love the improved frame rates.",
    "Scientists discovered a new exoplanet orbiting a distant star in the habitable zone. The research team published their findings in Nature journal. This discovery could provide insights into planetary formation.",
    "The basketball team won the championship after an incredible final game. The players celebrated with fans in the stadium. It was the team's first title in twenty years.",
    "Congress passed a new bill regarding healthcare reform. The president is expected to sign the legislation next week. The policy will affect millions of citizens across the country.",
    "I love cooking Italian food at home. Pasta carbonara and margherita pizza are my favorite dishes to make. Fresh ingredients make all the difference in authentic recipes."
]

for i, text in enumerate(samples, 1):
    print(f'\nSAMPLE {i}')
    topics = classify_document(text)
    display_results(text, topics)