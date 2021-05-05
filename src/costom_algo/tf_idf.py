# -*- coding: utf-8 -*- #
# ------------------------------------------------------------------
# Author:           wangkun
# Created:          2021/5/5
# Description:      this file contains tf_idf algorithm
# ------------------------------------------------------------------
import math

import jieba
from src.logger import mylogger

class TfIdf(object):
    """
    This class implement the origin tf_idf algo.
    tf_idf algo tends to give weight to each word by considering 
    both term frequency and inverse document frequecy.
    tf_idf(word) = tf(word) * idf(word)
    Args:
        doc -> list: a list of strings or word list
    """
    def __init__(self, doc):
        self.word_list = []
        self.size = len(doc)
        if isinstance(doc, list) and self.size != 0:
            if isinstance(doc[0], str):
                mylogger.info("catch string like input for tf_idf, use jieba to cut.")
                for sentence in doc:
                    self.word_list.append(list(jieba.cut(sentence)))
            elif isinstance(doc[0], list):
                mylogger.info("catch word lsit like input for tf_idf.")
                self.word_list = doc
            else:
                mylogger.error("{} type illegal".format(type(doc[0])))
        else:
             mylogger.error("doc is empty or is not a list")

    def cal_tf(self, sentence):
        """
        Args:
            sentence -> Union(string, list)
        """
        total = 0
        vocab = {}
        sentence = sentence if isinstance(sentence, list) else list(jieba.cut(sentence))
        for word in sentence:
            total += 1
            if word in vocab.keys():
                vocab[word] += 1
            else:
                vocab[word] = 1
        for key, times in vocab.items():
             vocab[key] /= total
        return vocab

    def cal_idf(self, sentence):
        """
        Args:
            sentence -> Union(string, list)
        """
        vocab = {}
        sentence = sentence if isinstance(sentence, list) else list(jieba.cut(sentence))
        for word in sentence:
            vocab[word] = 0
            for item in self.word_list:
                if word in item:
                    vocab[word] += 1
        for key, times in vocab.items():
            vocab[key] = math.log(self.size / (1 + times))
        return vocab
        
    def cal_tf_idf(self, sentence):
        """
        Args:
            sentence -> Union(string, list)
        """
        vocab = {}
        sentence = sentence if isinstance(sentence, list) else list(jieba.cut(sentence))
        tf_vocab = self.cal_tf(sentence)
        idf_vocab = self.cal_idf(sentence)
        for key, value in tf_vocab.items():
            vocab[key] = tf_vocab[key] * idf_vocab[key]
        return vocab