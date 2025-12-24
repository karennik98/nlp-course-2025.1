import string
text = '''
    Natural Language Processing being seen (NLP) is a subfield of linguistics, computer science, and artificial
    intelligence concerned with the interactions between computers and human language. It is used to
    analyze text, allowing machines to understand, interpret, and manipulate human language. NLP has
    many real-world applications, including machine translation, sentiment analysis, and chatbots.
    '''
# step 1
tokens = text.split()
print(tokens)

# step 2 & 3
tokens_lower = [i.lower() for i in tokens]
translator = str.maketrans('', '', string.punctuation)
tokens_lower_no_punct = [t.translate(translator) for t in tokens_lower]
print(tokens_lower_no_punct)

# step 4
stop_words = ['the', 'a', 'an', 'in', 'on', 'at', 'for', 'to', 'of', 'and', 'is', 'are']
token_unstoppable = []
for i in tokens_lower_no_punct:
    if i not in stop_words:
        token_unstoppable.append(i)

print(token_unstoppable)

# step 5
all_suffixes = [
    'able', 'ible', 'ness', 'ment', 'less',
    'tion', 'sion', 'ive', 'ful', 'ity',
    'ing', 'est', 'ize', 'ise', 'ion',
    'al', 'ed', 'er', 'es', 'or', 's', 'ic'
]

def stemming(token, suffixes):
    for suffix in suffixes:
        if token.endswith(suffix):
            return token[:-len(suffix)]
    return token

tokens_stemmed = [stemming(i, all_suffixes) for i in token_unstoppable]
print(tokens_stemmed)


# bonus
lemma_dict = {
    'be': ['is', 'am', 'are', 'was', 'were', 'being', 'been'],
    'have': ['has', 'had', 'having'],
    'do': ['does', 'did', 'doing', 'done'],
    'go': ['goes', 'went', 'going', 'gone'],
    'say': ['says', 'said', 'saying'],
    'eat': ['ate', 'eaten', 'eating'],
    'see': ['saw', 'seen', 'seeing'],
    'take': ['took', 'taken', 'taking'],
    'make': ['made', 'making'],
    'know': ['knew', 'known', 'knowing'],
    'give': ['gave', 'given', 'giving'],
    'find': ['found', 'finding'],
    'think': ['thought', 'thinking'],
    'CHEKC WORD': ['it']
}
def lemmer(token, dic):
    for k, v in dic.items():
        if token in v:
            return k
    return token
tokens_lemma = [lemmer(i, lemma_dict) for i in tokens_lower_no_punct]
print(tokens_lemma)
