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
