[abc399](https://atcoder.jp/contests/abc399)

## C - Make it Forest

グラフで閉路を判断する問題  

連結成分の数を数えることにより解決  
答え = M辺 - ( N頂点 - 連結成分の個数K )

素集合データ構造(Union-Find)を用いることで高速に個数を求められる

