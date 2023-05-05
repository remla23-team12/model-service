import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk
import pandas as pd
import os

nltk.download('stopwords')
ps = PorterStemmer()

all_stopwords = stopwords.words('english')
all_stopwords.remove('not')


def preprocess_data(filename):
    filepath = f'training_data/{filename}'
    if not os.path.exists(filepath):
        print(filename + ' does not exist')
        return
    dataset = pd.read_csv(filepath, delimiter='\t', quoting=3)
    dataset['Review'] = dataset['Review'].map(lambda review: preprocess_review(review))
    dataset.to_csv(f'preprocessed_training_data/preprocessed_{filename}', sep='\t', quoting=3, index=False, encoding='utf-8')


def preprocess_review(review):
    review = re.sub('[^a-zA-Z]', ' ', review)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    review = ' '.join(review)
    return review


def test_preprocess():
    # r = 'I paid the bill but did not tip because I felt the server did a terrible job.'
    # preprocess_review(r)
    preprocess_data('a1_RestaurantReviews_HistoricDump.tsv')
