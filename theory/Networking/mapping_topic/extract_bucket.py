from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings

warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)

import os
from bertopic import BERTopic
import pandas as pd

model_merged_ngram = BERTopic.load("../model_merged_ngram_no_len")

tp = model_merged_ngram.get_topic_info()
#print(type(tp))

data = {
    'Bucket Number': tp['Topic'],
    'Bucket': tp['Name']
}

df = pd.DataFrame.from_dict(data)

df.to_csv('net_bucket.csv', index=False)
