# やっつけ仕事

[aoj](http://judge.u-aizu.ac.jp/onlinejudge/)のAPIから問題ID、ジャッジID、ソースコードを取得する。
APIから、すべてのソースコードを取得できるが、言語、ステータスの情報がないのでjson形式で取得してみた。
以下データ構造
```
[
    {
        "judgeId": int,
        "judgeType": int,
        "userId": str,
        "problemId": str,
        "submissionDate": int,
        "language": str{"C++"},
        "status": int{1 or 4},
        "cpuTime": int,
        "memory": int,
        "codeSize": int,
        "accuracy": str,
        "judgeDate": int,
        "score": int,
        "problemTitle": null,
        "token": null
        "source": str{}
    },
    {
        ...
    },
]
```