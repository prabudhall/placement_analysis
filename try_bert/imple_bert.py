import nltk
# nltk.download('stopwords')
# nltk.download('omw-1.4')
# nltk.download('wordnet')
wn = nltk.WordNetLemmatizer()
from bertopic import BERTopic
from umap import UMAP
import os
from ext_all_ques import get_ques_list

os.chdir("../theory")
folder_list = os.listdir()
ques_list = get_ques_list("networking")
print(ques_list)
# def use_bert:

amz_review = ques_list
stopwords = nltk.corpus.stopwords.words('english')
# amz_review_without_stopwords = amz_review.apply(lambda x: ' '.join([w for w in x.split() if w.lower() not in stopwords]))
# amz_review_lemmatized = amz_review_without_stopwords.apply(lambda x: ' '.join([wn.lemmatize(w) for w in x.split() if w not in stopwords]))
# print(amz_review_without_stopwords)

umap_model = UMAP(n_neighbors=15,
                  n_components=5,
                  min_dist=0.0,
                  metric='cosine',
                  random_state=100)

topic_model = BERTopic(umap_model=umap_model, language="english", calculate_probabilities=True)

topics, probabilities = topic_model.fit_transform(amz_review)
print(topics)
print(topic_model.get_topic_info())
print(topic_model.get_topic(0))


# if __name__ == "__main__":
#     os.chdir("../theory")
#     folder_list = os.listdir()
#     ques_list = get_ques_list("networking")
    # print(ques_list)
    # use_bert(ques_list)
