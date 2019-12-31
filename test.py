import json
path = 'data_files/test1.json'
records = [json.loads(line) for line in open(path,'r', encoding='UTF-8')]

SendRegisterVerificationCodejson_txt = """
[{
  "header":{
    "funcNo": "IF010002",
    "opStation": "11.11.1.1",
    "appId": "aaaaaa",
    "deviceId": "kk",
    "ver":"wx-1.0",
    "channel": "4"
  },
  "payload": {
    "mobileTel": "13817120001"
  }
},
{
  "header":{
    "funcNo": "IHBH123",
    "appId": "avva",
    "ver":"wx-1.1",
    "channel": "3"
  },
  "payload": {
    "mobileTel": "13900109001"
  }
}]
"""
flat = json.loads(SendRegisterVerificationCodejson_txt)

# 获取records第一条数据
print(records[0])
print(records[0]['code'])
print(records[0]['Flag']['score'])
# 可能不是所有记录都有code字段，需要增加一个if判断
#code=[rec['tz'] for rec in records] 可能会报错
code=[rec['code'] for rec in records if 'code' in rec]


# dic = {}
# def json_txt(dic_json):
#     if isinstance(dic_json, dict):  # 判断是否是字典类型isinstance 返回True false
#         for key in dic_json:
#             print(key)
#             if isinstance(dic_json[key], dict):  # 如果dic_json[key]依旧是字典类型
#                 print("key：%s value: %s" % (key, dic_json[key]))
#                 json_txt(dic_json[key])
#                 dic[key] = dic_json[key]
#             else:
#                 print("key：%s value: %s" % (key, dic_json[key]))
#                 dic[key] = dic_json[key]
#
# json_txt(flat)
# print(str(dic))

# 获取统计个数
def get_counts(sequence):
    counts={}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

from collections import defaultdict
def get_counts2(sequence):
    counts= defaultdict(int)#所有的值均会被初始化为0
    for x in sequence:
        counts[x] += 1
    return counts


def top_counts(count_dict,n=10):
    # 因为用到了排序，所以需要将code和统计次数倒置
    values=[(count,code) for code,count in count_dict.items()]
    # 降序排列，默认reverse=Flase，升序
    values.sort()
    # 切片,取最后n个元素，因为是升序，所以取的是top n
    return values[-n:]

counts = get_counts(code)
print("counts:",counts)
print("get_counts2(code):",get_counts2(code))
print("top_counts(counts):",top_counts(counts))

# 用标准库计数，取出top10
from collections import Counter
counts=Counter(code)
print("counts",counts)
print("top10",counts.most_common(10))


from pandas import DataFrame,Series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

frame=DataFrame(records)
# print("frame",frame)
# print(frame['Flag'][:10])
# 也可以写成.的形式获取Flag里的内容
# print(frame.Flag)
# print(frame['Flag'].value_counts())

# fillna 替换缺失值

clean_code = frame['code'].fillna('Missing')
print("空的索引",clean_code[clean_code == ''])

# 通过布尔型数组索引替换值是空字符串的为Unknown
clean_code[clean_code == ''] = 'Unknown'
code_counts = clean_code.value_counts()
print(code_counts[:10])
code_counts[:10].plot(kind='barh',rot=0)
plt.show()

# frame.code.notnull() 判断是否非空，属于布尔型索引
cframe=frame[frame.code.notnull()]
# dropna删除空项
dframe=frame.code.dropna()

