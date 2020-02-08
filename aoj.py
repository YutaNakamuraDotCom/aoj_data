import requests
import json
import ast

def problem_id():
    url = 'https://judgeapi.u-aizu.ac.jp'
    para = '/problems?page={page}&size={size}'
    savepath = 'problem{num}.json'

    for page in list(range(0,1)):

        body = requests.get(url + para.format(page=page,size=2500))

        a = open(savepath.format(num=page), 'w')
        json.dump(body.json(), a)

    return body.json()

def mkidls():
    url = 'https://judgeapi.u-aizu.ac.jp'
    para = '/submission_records/problems/{id}?page={page}&size={size}'
    savepath = 'problem{num}_{page}.json'
    for num in (range(0,2500)):
        a = problem_id()
        b = a[num]
        id = b['id']
        for page in range(0,5):
            print(page)
            judgeid = requests.get(url + para.format(id=id,page=page,size=10000))
            a = open(savepath.format(num=id,page=page), 'w')
            json.dump(judgeid.json(), a)    

mkidls()