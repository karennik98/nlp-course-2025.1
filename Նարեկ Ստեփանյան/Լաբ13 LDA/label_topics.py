import json
from gensim.models import LdaModel
from gensim.corpora import Dictionary

lda_model = LdaModel.load('models/lda_model.model')
dictionary = Dictionary.load('models/dictionary.dict')

topic_labels = {}
print('\n=== TOPIC LABELING ===')
for i in range(10):
    words = lda_model.show_topic(i, topn=20)
    print(f'\n--- Topic {i} ---')
    for word, prob in words:
        print(f' {word}: {prob:.4f}')
    label = input(f'\nEnter name for Topic {i} (or press Enter to skip): ').strip()
    topic_labels[i] = label if label else f'Topic {i}'

with open('models/topic_labels.json', 'w') as f:
    json.dump(topic_labels, f, indent=2)
print('\n=== FINAL TOPIC NAMES ===')
for idx, name in topic_labels.items():
    print(f'Topic {idx} → {name}')