import requests
import json
import ast
import re
import time

# 問題情報を取得する（問題文は含まれない）


def problem_id(url):
    para = '/problems?page={page}&size={size}'
    savepath = 'problem{num}.json'

    for page in list(range(0, 1)):

        # body = requests.get(url + para.format(page=page, size=2500))
        body = requests.get(url + para.format(page=page, size=3))

        a = open(savepath.format(num=page), 'w')
        json.dump(body.json(), a)

    return body.json()

# 各問題のユーザの全回答id,ステータスを取得しjson形式で保存


def mk_id_ls(url):
    para = '/submission_records/problems/{id}?&size={size}'
    savepath = 'problem{num}.json'
    b = pro_id_ls()
    prolen = len(b)
    # for num in (range(0, prolen)):
    for num in (range(0, 3)):
        id = b[num]
        judgeid = requests.get(url + para.format(id=id, size=100000))
        a = open(savepath.format(num=id,), 'w')
        json.dump(judgeid.json(), a)
        print(str(num)+'ファイル出力')


# problem_idで保存したjsonから問題IDを取得し、listを返す関数
def pro_id_ls():
    pro_id_ls = []
    with open('problem0.json', 'r') as f:
        b = json.load(f)
        prolen = len(b)
        # for num in range(0000, prolen):
        for num in range(0000, 3):
            c = b[num]
            id = c['id']
            pro_id_ls.append(id)
    return pro_id_ls

# mk_id_lsで保存したjsonからｃ、ｃ＋＋のみを抽出し上書きする。


def c_filter():
    ls = pro_id_ls()
    leng = len(ls)
    path = 'problem{pro_id}.json'
    # for a in range(0, leng):
    for a in range(0, 3):
        result = {}
        li = []
        pro_id = ls[a]
        judge_id = []
        print(pro_id)
        with open(path.format(pro_id=pro_id), 'r') as f:
            judge = json.load(f)
            judge_leng = len(judge)
            for b in range(0, judge_leng):
                judge_temp = judge[b]
                judge_lang = judge_temp['language']
                print(judge_temp)
                if judge_lang in ['C', 'C++', 'c++14']:
                    result.update(judge_temp)
                    judge_id.append(result)

                    # print(judge_lang)

        savepath = 'lang{pro_id}.json'
        a = open(savepath.format(pro_id=pro_id,), 'w')
        json.dump(judge_id, a)
        # print('ok')
    return judge_id


def mk_result(url, judge_id):
    para = '/reviews/{judge}'
    savepath = 'result{pro_id}.json'
    path = 'lang{lang_id}.json'
    pro_id = pro_id_ls()
    result = []
    for a in pro_id:
        a = int(a)
        with open(path.format(lang_id=pro_id[a]), 'r') as f:
            filter_json = json.load(f)
            length = len(filter_json)
        for num in range(length):
            # time.sleep(5)
            print("                                                                                                                                                                                ")
            print(num)
            te = list(filter_json)
            d = te[num]
            ta = dict(d)
            judgeis_ls = ta['judgeId']
            print('あｓｆじゃいｊふぁｐ')
            print(judgeis_ls)

            judgeid = requests.get(url + para.format(judge=judgeis_ls))
            w = judgeid.json()
            print(w)
            z = w["sourceCode"]
            print(z)
            if not z == 'You are not allowed to see this code.':
                d.update(sourceCode=z)
                result.append(d)
                print(d)
        a = open(savepath.format(pro_id=num), 'a')
        json.dump(result, a)


def main():
    url = 'https://judgeapi.u-aizu.ac.jp'
    problem_id(url)
    mk_id_ls(url)
    judge_id = c_filter()
    mk_result(url, judge_id)


if __name__ == "__main__":
    main()
