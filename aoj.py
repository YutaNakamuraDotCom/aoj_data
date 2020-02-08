import requests
import json
import ast
import re

# 問題情報を取得する（問題文は含まれない）


def problem_id(url):
    para = '/problems?page={page}&size={size}'
    savepath = 'problem{num}.json'

    for page in list(range(0, 1)):

        body = requests.get(url + para.format(page=page, size=2500))

        a = open(savepath.format(num=page), 'w')
        json.dump(body.json(), a)

    return body.json()

# 各問題のユーザの全回答id,ステータスを取得しjson形式で保存


def mk_id_ls(url):
    para = '/submission_records/problems/{id}?&size={size}'
    savepath = 'problem{num}.json'
    b = pro_id_ls()
    prolen = len(b)
    for num in (range(0, prolen)):
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
        for num in range(0000, prolen):
            c = b[num]
            id = c['id']
            pro_id_ls.append(id)
    return pro_id_ls

# mk_id_lsで保存したjsonからｃ、ｃ＋＋のみを抽出し上書きする。


def c_filter():
    ls = pro_id_ls()
    leng = len(ls)
    path = 'problem{pro_id}.json'
    for a in range(0, leng):
        result = {}
        li = []
        pro_id = ls[a]
        print(pro_id)
        with open(path.format(pro_id=pro_id), 'r') as f:
            judge = json.load(f)
            judge_leng = len(judge)
            for b in range(0, judge_leng):
                judge_temp = judge[b]
                judge_lang = judge_temp['language']
                print(b)
                if judge_lang in ['C', 'C++', 'c++14']:
                    result.update(judge_temp)
                    li.append(result)
                    print(judge_lang)
                    # print(result)
        savepath = '{pro_id}.json'
        a = open(savepath.format(pro_id=pro_id,), 'w')
        json.dump(li, a)
        print('ok')


def main():
    url = 'https://judgeapi.u-aizu.ac.jp'
    # problem_id(url)
    # mk_id_ls(url)
    c_filter()


if __name__ == "__main__":
    main()
