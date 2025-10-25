[AtCoder のディレクトリ作成・サンプルケースのテスト・提出を自動化する。](https://qiita.com/takeaship/items/d0718066922612648eaa)を参考に実装  

## 前提条件

- atcoder-cli と online-judge-tools の導入が済んでいること

- 2つに対してログインが済んでいること(acc login , oj login https://beta.atcoder.jp/)

## テスト提出まで

※コマンドプロンプトにて作業する

1. acc new [コンテストNo]

1. 対象ディレクトリへ移動

1. oj t -c "python main.py"

1. acc submit main.py -- -l 5063

##  テンプレート設定

1. acc config-dir で格納場所検索

1. template.jsonとmain.pyの作成

1. acc config default-test-dirname-format test

1. acc config default-task-choice all

1. acc config default-template python

## その他

- 現在、Atcoderのセキュリティ強化の影響によりacc submitができない。  
その場合は、acc submitの手順は手動で行う必要あり。

- acc loginができないケースが発言([対処法](https://kaiyou9.com/acc_and_oj_login_failed/))

## Python 入力

- edgeの入力(木構造みたいな形)
```python
edges = [tuple(map(int, input().split())) for _ in range(M)]
```

- 迷路問題
```python
H,W=map(int, input().split())
S=[input() for i in range(H)]
```

## 参考

- 累積和  
[C - Rotate and Sum Query](https://atcoder.jp/contests/abc425/tasks/abc425_c)
[C - Equilateral Triangle](https://atcoder.jp/contests/abc409/tasks/abc409_c)


- 木問題(有向辺)  
[C - New Skill Acquired ](https://atcoder.jp/contests/abc424/tasks/abc424_c)

- 2部グラフ、bit全探索
[C - Bipartize](https://atcoder.jp/contests/abc427/tasks/abc427_c)

- 迷路問題、多始点BFS(幅優先探索)
[D - Escape Route](https://atcoder.jp/contests/abc405/tasks/abc405_d)