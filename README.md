# [やってみた]　AtCoder 版！蟻本 (初級編) [2-1-2 Lake Counting (POJ No.2386)]

## はじめに

筆者はAtCoderを取り組み始めたアラフォー・Unコーダである。

[AtCoder 版！蟻本 (初級編)](https://qiita.com/drken/items/e77685614f3c6bf86f44)に蟻本記載例題の類似問題が記載されている。

[AtCoder](https://atcoder.jp/?lang=ja)を利用してジャッジできるアルゴリズムの良問が選別されているので、初学者にうってつけである。

上記記事著者である、けんちょん (Otsuki)@drken氏に感謝。

筆者は[AtCoder 版！蟻本 (初級編)](https://qiita.com/drken/items/e77685614f3c6bf86f44)を頼りにスキルアップを図っている途中である。
* [1 いざチャレンジ！でもその前に --- 準備編に取り組んだ過去記事](https://qiita.com/tagtagtag/items/eaa0655d26cdcbd5202e)


## 目的

* 筆者の競技プログラミング成績向上を図る。
* [AtCoder 版！蟻本 (初級編)](https://qiita.com/drken/items/e77685614f3c6bf86f44)に記載の問題を解説しながら記述することで、アルゴリズムの基礎を身に着ける。
* コードと解説を掲載し、諸兄（姉）からの指摘を受けることで見落としていた課題を補完する。

## 今後

* 2-2 猪突猛進！ "貪欲法"に挑戦する。


## 解答

問題のタイトルは、けんちょん (Otsuki)@drken氏の記事を借用致します。



#### [ATC 001 A 深さ優先探索](https://atcoder.jp/contests/atc001/tasks/dfs_a)

* 方針
  * 数字の間に＋******************
  * 
 

* 実装
  * hoge***********************


```python
import math
```

#### [ARC031B 深さ優先探索](https://atcoder.jp/contests/arc031/tasks/arc031_2)

* 方針
  * deepcopyで毎回計算する盤面を新しくする
  * 
 

* 実装
  * 答えが見つかれば二重ループを一発で抜けたい
    * for文でのelseの使い方が重要
      * breakするとelse:が実行されないため、次のbreakに進む。
      * for loopが完了するとelseが実行されるので、continueが実行され外側のloopが次へ進む。
  * 答えが見つからなかった場合の実行を行う
    * for loopが全部回り切ったら答えが見つからなかったことになるため、最後のelse: が答えが見つからなかった時の処理。

```python

for i in some_list:
    for j in somesome_list:
        if some_condition:
            print('YES')
            break
    else:
        continue
    break
else:
    print('NO')
```





```python
import math
```