import nltk
from nltk.probability import FreqDist
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string
import pandas as pd
import regex as re
#from wordcloud import WordCloud
#cloud = WordCloud(max_font_size=80,colormap="hsv").generate_from_frequencies(dictionary)

def cut_lines(lines, file):
    with open(file, 'r') as f:
        lines = f.readlines()[lines:]
    with open(file, 'w') as f:
        f.writelines(lines)

#cut_lines(5, 'Pharmaceutical+general+notes.csv')
        
        # CHANGE FILE NAME HERE
df = pd.read_csv('all+general+notes.csv')
#("Pharmaceutical+general+notes.csv")

def plot_words(corpus, stopwords):
    chars = re.escape(string.punctuation)

    corpus = re.sub('['+chars+']', '', corpus)
    print(type(corpus))

    #corpus = corpus.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(corpus)

    stopwords = list(stopwords.words('english'))
    with open('stopwords.txt', 'r') as f:
        other_stopwords = [word.strip('\n').lower() for word in f.readlines()]
        print(other_stopwords)
    #other_stopwords = ['dr', 'susanna', 'christopher', 'need', 'would', 'okay', 'notes', "'", 'may', 'like', 'us', 'also', 'email', ',', "search", "`", "looking", "attorney", "share", "spoke","please", ]
    filtered_text = [t for t in tokens if t not in stopwords and t not in other_stopwords]
    counter = Counter(filtered_text)
    with open('output.txt', 'w+') as f:
        f.write('\n'.join([str(i) for i in counter.most_common()]))

    fdist_filtered = FreqDist(filtered_text)
    fdist_filtered.plot(50,title='Frequency distribution for 50 most common tokens in our text collection (excluding stopwords and punctuation)')
plot_words(' '.join(df['General Search Notes']).lower(), stopwords)

