from ext_all_ques import get_ques_list
from bertopic import BERTopic
import numpy as np
from time import sleep
import pickle
import torch
import os
from transformers import BertConfig, BertModel

def check_for(folder):
    ques_list = get_ques_list(folder)
    os.chdir(folder)
    print(os.getcwd(), '\n Now importing model\n')
    # model = BERTopic.load(torch.load('model', map_location=torch.device('cpu')))
    # model.model.to('cpu')
    # model = torch.load('model.pkl', map_location=torch.device('cpu'))
    # model = model.to(torch.device('cpu'))
    # model = BertModel.from_pretrained('./model')

    # with open('model.pkl', 'rb') as f:
    #     model = pickle.load(torch.load(f, map_location=torch.device('cpu')))
    #     model.to('cpu')


    device = torch.device('cpu')
    model=torch.load('model_direct_pth.pth', map_location=device)
    model.eval()



    for ques in ques_list:
        print(ques)
        # for predicting the topics for any new sentence
        new_check = ques

        # Find topics
        num_of_topics = 3
        similar_topics, similarity = model.find_topics(new_check, top_n=num_of_topics)

        print(
            f'The top {num_of_topics} similar topics are {similar_topics}, and the similarities are {np.round(similarity, 2)}')

        # for printing those 3 topics
        for index, top in enumerate(similar_topics):
            keys = [t[0] for t in model.get_topic(top)]
            print(f'{keys} : with probability \n{np.round(similarity, 2)[index]}')

        print()
        print()
        print()
        sleep(1)

    os.chdir('..')


if __name__ == "__main__":
    os.chdir("../theory")
    print(os.getcwd())
    check_for("Networking")
