'''
Created on Jun 13, 2017

@author: taurus
'''

if __name__ == '__main__':
    path = '/home/taurus/Datasets/ieee_zhihu_cup'
    fpLabel = open(path + 'question_topic_train_set.txt', 'r')
    fpQuestion = open(path + 'question_train_set.txt', 'r')
    
    fpLabel