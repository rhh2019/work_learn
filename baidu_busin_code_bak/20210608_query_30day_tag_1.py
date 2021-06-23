# coding=utf-8
"""
29372876 query数据
2021-04-09
renhuihui
"""
import codecs
import datetime
import time
import json
from multiprocessing import Pool
import random
import sys
sys.path.append('/home/work/renhuihui/code/baidu/ebiz/fcapp-lemon-data/')

from lemon_data.tp_wenda_tag_v2.tp_tag.predict_project_tag import predict_notClf3  


def load_data(data_path, out_path):
    with codecs.open(data_path, 'r', 'utf-8') as fin, \
        codecs.open(out_path, 'w', 'utf-8') as fout:
        idx = 0
        for line in fin:
            idx += 1
            error_lines = []
            tags = []
            try:
                arr = line.strip("\n").split("\t")
                if len(arr) != 4: continue
                nid = arr[1]
                day = arr[0]                
                texts = arr[2].split("-")
                
                for text in texts:
                    level, tag, mark = predict_notClf3.predict_main(text)
                    tags.append([level, tag])
                fout.write(nid + "\t" + arr[2] + "\t" + day + "\t" + json.dumps(tags, ensure_ascii=False) + "\n")
            except:
                error_lines.append(idx)
            # if idx > 10:
            #     break
    print data_path, "error_lines: ", error_lines
            


def get_past_days(base_date_str, num):
    """[获取过去N天的日期字符串]

    Arguments:
        num {[int]} -- [过去num天]

    Returns:
        [list] -- [日期列表]
    """
    past_30_days = []
    base_date = datetime.datetime.strptime(base_date_str, "%Y%m%d")
    for i in range(0, num):
        past_ith_day = base_date - datetime.timedelta(days=i)
        past_ith_day =  past_ith_day.strftime('%Y%m%d')
        # print past_ith_day
        past_30_days.append(past_ith_day)
    return past_30_days


def multiple_process_predict(current_day):
    past_30_days = get_past_days(current_day, 20)
    p = Pool(10)
    for idx in past_30_days:
        in_path = base_path + "daily_query/app_user_query_day_{}.txt".format(idx)
        out_path = base_path + "h5_app_all_tag/app_user_query_day_{}.tag.txt".format(idx)
        p.apply_async(load_data, args=(in_path, out_path,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()


def res_check():
    tag_res = {}
    error_cnt = 0
    for idx in ["00", "05", "09"]:
        out_path = base_path + "20210425_user_item_query.tag.txt{}".format(idx)
        with codecs.open(out_path, 'r', 'utf-8') as fin:
            for line in fin:
                arr = line.strip().split("\t")
                text_list = u"".join(arr[1:-2]).split("-")
                tags = json.loads(arr[-1])
                if len(text_list) == len(tags):
                    for text, tag in zip(text_list, tags):
                        tag = u"{}-{}".format(tag[0], tag[1])
                        tag_res.setdefault(tag, [])
                        tag_res[tag].append(text)
                else:
                    error_cnt += 1
                # if len(tag_res) > 2: break
        # if len(tag_res) > 2: break
    sorted_tag_res = sorted(tag_res.items(), key=lambda x: len(x[1]), reverse=True)
    with codecs.open(base_path + "res_check.txt", 'w', 'utf-8') as fout:
        for tag, text_list in sorted_tag_res:
            # level_tag = u"_".join(tag)
            random.shuffle(text_list)
            for text in text_list[:10]:
                fout.write(tag + u"\001" + text + "\n")
            
        
if __name__ == "__main__":
    current_day = "20210528"
    past_30_days = get_past_days(current_day, 30)
    print len(past_30_days), past_30_days
    exit()
    base_path = u"/home/work/renhuihui/project_data/query_tag/"
    multiple_process_predict(current_day)
    # idx = "00"
    # in_path = base_path + "20210425_user_items_query.txt{}".format(idx)
    # out_path = base_path + "20210425_user_items_query.tag.txt{}".format(idx)
    # start_time = time.time()
    # load_data(in_path, out_path)
    # end_time = time.time()
    # total_seconds = end_time - start_time
    # total_hour = total_seconds * 1. / 3600
    # print total_seconds, total_hour
    
    # res_check()
    
    # 3550 nohup python tag.py > tmp.log 2>&1 &
    
    
    
    
    
    