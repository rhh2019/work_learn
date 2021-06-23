
def get_past_days(base_date, num):
    """[获取过去N天的日期字符串]

    Arguments:
        num {[int]} -- [过去num天]

    Returns:
        [list] -- [日期列表]
    """
    base_date = datetime.datetime.strptime(base_date, "%Y%m%d")
    past_30_days = []
    for i in range(0, num):
        past_ith_day = base_date - datetime.timedelta(days=i)
        past_ith_day =  past_ith_day.strftime('%Y%m%d')
        # print past_ith_day
        past_30_days.append(past_ith_day)
    return past_30_days


# 多进程同时对多天的
# multiple_process_predict(day, tag_by_day_path, merged_res_path)
def multiple_process_predict(current_day, in_path, out_path):
    """[summary]

    Arguments:
        current_day {[type]} -- [description]
        in_path {[type]} -- [description]
        out_path {[type]} -- [description]
    """
    past_30_days = get_past_days(current_day, 30)
    print len(past_30_days), past_30_days
    p = multiprocessing.Pool(5)
    for idx in past_30_days:
        fulled_in_path = in_path.format(day=idx)
        fulled_out_path = out_path.format(day=idx)
        p.apply_async(merge_cuid_latest_tag, args=(fulled_in_path, fulled_out_path,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    
    