# やっつけ仕事

[aojのAPI](http://judge.u-aizu.ac.jp/onlinejudge/)から問題ID、ジャッジID、ソースコードを取得する。
APIから、すべてのソースコードを取得できるが、言語、ステータスの情報がないのでjson形式で取得してみた。

また、サーバに高負荷をかけないように適宜time.sleep()を挿入してください。


以下データ構造
```
[
    {
        "judgeId": int,
        "userId": str,
        "problemId": str,
        "submissionDate": int,
        "language": str{"C++"},
        "status": int{0-8},
        "sourceCode": str{}
    },
    {
        ...
    },
]
```