import pickle
import jieba
import progressbar
import csv
import math

def jieba_1(boardname, filename):
    bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
    with open("/home/ptt/ptt_{}_{}.txt".format(boardname, filename), "rb") as f:
        ptt = pickle.load(f)
    jieba.load_userdict("for_jieba_seasoning.txt")


    total_page = len(ptt)
    start = 0
    end = 10000

    page_count = 0

    
    if end > total_page:
        end = total_page
        print("Last run! All " + total_page + " pages will soon be finished.")
    else:
        print("This is the first run, you still have to run " + str(math.ceil(total_page/10000)) + " times.")

    for content in ptt[start:end]:
        seg_list = list(jieba.cut(content[-1], cut_all=False))
        content.append(seg_list)
        page_count += 1
        bar.update(page_count)
    
    with open("ptt_{}_text_jieba_pickle.txt".format(boardname), "wb") as c:
        pickle.dump(ptt, c)
    

    f = open('ptt_{}_text_jieba.csv'.format(boardname), 'w')
    w = csv.writer(f)
    w.writerows(ptt)
    f.close()

            

def jieba_from2(boardname, start, end):
    bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
    with open("ptt_{}_text_jieba_pickle.txt".format(boardname), "rb") as f:
        ptt = pickle.load(f)
    jieba.load_userdict("for_jieba_seasoning.txt")


    total_page = len(ptt)
    #start = 10000
    #end = 20000

    page_count = 0


    if end > total_page:
        end = total_page
        print("Last run! All " + total_page + " pages will soon be finished.")
    else:
        print("This is the " + str(end/10000) + " run!" + "you still have to run " + str(math.ceil((total_page-10000)/10000)) + " times.")
    for content in ptt[start:end]:
        seg_list = list(jieba.cut(content[-1], cut_all=False))
        content.append(seg_list)
        page_count += 1
        bar.update(page_count)

    with open("ptt_{}_text_jieba_pickle.txt".format(boardname), "wb") as c:
        pickle.dump(ptt, c)

    f = open('ptt_{}_text_jieba.csv'.format(boardname), 'w')
    w = csv.writer(f)
    w.writerows(ptt)
    f.close()
