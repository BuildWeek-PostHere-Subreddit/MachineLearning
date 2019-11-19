import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors


df= pd.read_csv('token_data.csv').drop(['Unnamed: 0','Unnamed: 0.1'], axis=1)

def vectorizer():
    # Instantiate vectorizer object
    tfidf = TfidfVectorizer(stop_words='english', min_df=0.025, max_df=.98, ngram_range=(1,2))
    
    # Create a vocabulary and get word counts per comment
    dtm = tfidf.fit_transform(df['tokens']) # Similiar to fit_predict

    # Get feature names to use as dataframe column headers
    dtm = pd.DataFrame(dtm.todense(), columns=tfidf.get_feature_names())

    return dtm,tfidf

def neighbors(dtm, tfidf, text):
    # Fit on TF-IDF Vectors
    nn  = NearestNeighbors(n_neighbors=5, algorithm='kd_tree')
    nn.fit(dtm)
    new = tfidf.transform(text)
    return nn.kneighbors(new.todense())[1][0]
