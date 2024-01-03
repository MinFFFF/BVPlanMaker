# 获取观看计划
# epi_name为视频名称列表，string类型
# epi_time为视频长度列表,int类型,单位为秒
# start为开始集数，最小为1
# end为结束集数，-1默认为最后一集
# days为计划完成天数
# speed为倍速
def getPlan(epi_name,epi_time,days,start=1,end=-1,speed=1):
    if(end == -1):#end = -1,默认到最后一集
        end = len(epi_time)
    total_sec = 0
    for i in range(start-1,end):
        total_sec = total_sec + epi_time[i]
    sec_per_day = total_sec / days
    #print(sec_per_day/60)

    now = start - 1
    plan = []
    now_sec = 0
    for i in range(days):
        temp = 0
        d = []
        days_sec = []
        while(temp < sec_per_day and now < end):
            temp = temp + epi_time[now]
            d.append(epi_name[now])
            now = now + 1
        days_sec.append(temp)
        now_sec = now_sec + temp
        print("--------------------第{}天--------------------".format(i+1))
        for j in range(len(d)):
            print("({}) {}".format(j+1,d[j]))
        print("总时长:{:.2f}({:.2f})分钟".format(temp/60,temp/60/speed))
        print("完成率:{:.4f}%".format((now_sec/total_sec)*100))
        plan.append(d)
    return plan

#获取时长
def getDuration(epi_name,epi_time,start,end,speed):
    if (end == -1):
        end = len(epi_time)
    d = 0
    print(start)
    for i in range(start-1,end):
        d = d + epi_time[i]
    print("{}-{}:{:.2f}({:.2f})分钟".format(epi_name[start-1],epi_name[end-1],d/60,d/60/speed))
    return d/60