import requests
import json
import ast

#問題情報を取得する（問題文は含まれない）
def problem_id():
    url = 'https://judgeapi.u-aizu.ac.jp'
    para = '/problems?page={page}&size={size}'
    savepath = 'problem{num}.json'

    for page in list(range(0,1)):

        body = requests.get(url + para.format(page=page,size=2500))

        a = open(savepath.format(num=page), 'w')
        json.dump(body.json(), a)

    return body.json()

#各問題のユーザの全回答id,ステータスを取得しjson形式で保存
def mk_id_ls():
    url = 'https://judgeapi.u-aizu.ac.jp'
    para = '/submission_records/problems/{id}?&size={size}'
    savepath = 'problem{num}.json'
    b=pro_id_ls()
    prolen = len(b)
    for num in (range(0,prolen)):
        id=b[num]
        judgeid = requests.get(url + para.format(id=id,size=50000))
        a = open(savepath.format(num=id,), 'w')
        json.dump(judgeid.json(), a)


#問題IDをlistで返す関数
def pro_id_ls():
    pro_id_ls = []
    with open('problem0.json', 'r') as f:
        b=json.load(f)
        prolen = len(b)
        for num in range(0000,prolen):
            c = b[num]
            id = c['id']
            pro_id_ls.append(id)
    return pro_id_ls

    

if __name__ == "__main__":
