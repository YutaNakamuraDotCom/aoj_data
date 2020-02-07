import requests
import json
import ast

def problem_id():
    url = 'https://judgeapi.u-aizu.ac.jp/problems?page={page}&size={size}'
    savepath = 'problem{num}.json'

    for page in list(range(0,1)):

        body = requests.get(url.format(page=page,size=2500))

        a = open(savepath.format(num=page), 'w')
        json.dump(body.json(), a)

    return body.json()

def mkidls():
    for num in (range(0,2500)):
        a = problem_id()
        b = a[num]
        print(b['id'])

mkidls()