import csv
import os
import joblib
import pickle
from ext_ques_csv import get_ques
import pandas

def pred(filename):
    # ques_list = get_ques(filename)
    ques_list = ['given string binary example lkadnf sdfjsn rgrth hgvgvh gvhgv hgvghv hbghvghv jghvjvg gvhgv jbhbvhjj jgjyg yftc ftyyt dfrdrtd', '4tguy3gy 3ugy3tg 3rg3gf3']
    # cur_folder = os.getcwd().split('\\').pop()
    # os.chdir('..')

    vectorizer = ''
    with open('../code_vector.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    model = joblib.load('../code_model.joblib')

    # os.chdir(cur_folder)

    # for each_ques in ques_list:
    #     list_for_vector = []
    #     list_for_vector.append(each_ques)
    #     test = vectorizer.transform(list_for_vector)
    #
    #     print("Question : ", each_ques)
    #     for category, mdl in model.items():
    #         prediction = mdl.predict(test)
    #         if prediction[0] == 1:
    #             print(category, end=', ')
    #     print()
    vectorizer.fit(ques_list)
    test = vectorizer.transform(ques_list)
    for category, mdl in model.items():
        prediction = mdl.predict(test)
        print(prediction)
 

if __name__ == "__main__":
    os.chdir("../coding/with_ques")
    pred("Amazon.csv")
