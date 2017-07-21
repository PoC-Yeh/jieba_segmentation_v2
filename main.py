import pickle
import jieba
import progressbar
import csv
import math
from jieba_cut_v2 import *


jieba_1("Japan_Travel", "textpickle")
#jieba_1(boardname, filename)
#/home/ptt/ptt_Japan_Travel_textpickle.txt
#first arg -> board name
#second arg -> "textpickle" or "text_pickle"

jieba_from2("Japan_Travel", 10000, 20000)
#jieba_from2(boardname, start, end)
