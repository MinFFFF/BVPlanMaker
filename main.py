import requests
import re
from  GetPlan import getPlan,getDuration



headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
}

BV = 'BV1TD4y137mP'
url = 'https://www.bilibili.com/video/' + BV
speed = 1.25#倍速

webPageSource = requests.get(url=url,headers=headers)

if(webPageSource.status_code != 200):
    print('网页源代码爬取错误')
else:
    epiNamePattern = '\"part\":\"(.*?)\"'#视频名称匹配串
    epiDurationPattern = '\"duration\":(.*?),'#视频时长匹配串
    epiNameList = re.findall(epiNamePattern, webPageSource.text)
    tempEpiDurationList = re.findall(epiDurationPattern, webPageSource.text)
    epiDurationList = []

    for i in range(2,len(tempEpiDurationList)):#将string类型转换为int类型，匹配到的前两个非视频集数时长
        if i >= len(epiNameList) + 2:
            break
        epiDurationList.append(int(tempEpiDurationList[i]))

    getPlan(epiNameList,epiDurationList,10,start=12,end=-1,speed=speed)




