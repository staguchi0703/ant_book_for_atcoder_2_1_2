# [やってみたが力尽きた]　AtCoder 版！蟻本 (初級編) [2-1-2 Lake Counting (POJ No.2386)]

## はじめに

筆者はAtCoderを取り組み始めたアラフォー・Unコーダである(非ソフトウェア職)。

[AtCoder 版！蟻本 (初級編)](https://qiita.com/drken/items/e77685614f3c6bf86f44)に蟻本記載例題の類似問題が記載されている。

[AtCoder](https://atcoder.jp/?lang=ja)を利用してジャッジできるアルゴリズムの良問が選別されているので、初学者にうってつけであるらしい。

上記記事著者である、けんちょん (Otsuki)@drken氏に感謝。

筆者は[AtCoder 版！蟻本 (初級編)](https://qiita.com/drken/items/e77685614f3c6bf86f44)を頼りにスキルアップを図っている途中である。
* [1 いざチャレンジ！でもその前に --- 準備編に取り組んだ過去記事](https://qiita.com/tagtagtag/items/eaa0655d26cdcbd5202e)

正直筆者には難しすぎて辛い。。。

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
  * 再帰
    * 壁と欄外に言ったらreturn
    * gを見つけるまで再帰関数で見つける
  * whileでqueかstackを使う方法
    * queかstackがなくなるまでwhileを回す
    * 答えが見つかったらflagを返す


```python

H, W = [int(item) for item in input().split()]
map_grid = [input() for _ in range(H)]

# pprint.pprint(map_grid, width=W)

for i in range(H):
    for k in range(W):
        if map_grid[i][k] == 's':
            start_point = [k, i] # x(k<<w), y(i << H)
# print(start_point)


def search_g(x, y, foot_print):
    if x >= W or x < 0 or y >= H or y < 0:
        return
    else:
        # print(x, y)
        if [x, y] in foot_print:
            return
        else:
            foot_print.append([x, y])

        temp_sign = map_grid[y][x]
        if temp_sign == '#':
            return
        elif temp_sign == 'g':
            print('yes')
            return

        search_g(x+1, y, foot_print)
        search_g(x, y+1, foot_print)
        search_g(x-1, y, foot_print)
        search_g(x, y-1, foot_print)

search_g(start_point[0], start_point[1], [])
```


``` python

from collections import deque
H, W = [int(item) for item in input().split()]
map_grid = [input() for _ in range(H)]

# pprint.pprint(map_grid, width=W)

# 開始地点の座標を探す
for i in range(H):
    for k in range(W):
        if map_grid[i][k] == 's':
            start_point = [k, i] # x(k<<w), y(i << H)
# print(start_point)

# dfsもしくはbfsするキュー(スタック)を生成
d = deque()
d.append(start_point)
#訪れた履歴を管理するスタックを生成
f = deque()

#とある座標の値を表示する関数（座標が定義外に飛んだ時にエラーとならないようにtry-exceptで無視できるようにするのがコツ）
def temp_sign(temp_site):
    try:
        res = map_grid[temp_site[0]][temp_site[1]]
        return res
    except:
        pass

next_direction_list = [[1, 0], [0,1], [-1, 0], [0, -1]]
is_found = False

while len(d) > 0:
    temp_site = d.pop()
    # print(temp_sign(temp_site))
    if temp_sign(temp_site) == 'g':
        is_found = True
        break
    
    for next_dir in next_direction_list:

        new_site = [x+y for (x, y) in zip(temp_site, next_dir) if x+y >= 0]
        # print(new_site)

        if temp_sign(new_site) in ['.', 'g'] and new_site not in f:
            # print(new_site)
            d.append(new_site)
            f.append(new_site)

if is_found:
    print('Yes')
else:
    print('No')
```

#### [ARC031B 埋め立て](https://atcoder.jp/contests/arc031/tasks/arc031_2)

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

* この構文を覚えておくと便利だと思った

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

* 解答

```python
from collections import deque
import copy
map_grid = [[ i for i in input()] for _ in range(10)]

# print(map_grid)

def dfs(site, temp_grid):
    y, x = site
    if 0 <= y <= 9 and 0 <= x <= 9 and temp_grid[y][x] == 'o':
        temp_grid[y][x] = 1
    else:
        return

    dfs([y+1, x], temp_grid)
    dfs([y, x+1], temp_grid)
    dfs([y-1, x], temp_grid)
    dfs([y, x-1], temp_grid)

for i in range(10):
    for j in range(10):
        temp_grid = copy.deepcopy(map_grid)
        temp_grid[i][j] = 'o'
        dfs([i, j], temp_grid)
        # print(temp_grid)
        # print('-----------------------')

        is_temp_o_found = False

        for k in temp_grid:
            if 'o' in k:
                is_temp_o_found = True

        if not is_temp_o_found:
            print('YES')
            # print(temp_grid)
            # print('-----------------------')
            break
    else:
        continue
    break
else:
    print('NO')

```


#### 「解答できず」[ARC037B バウムテスト](https://atcoder.jp/contests/arc031/tasks/arc037_b)

* 方針
  * 出来なかった
  * 木である事を判定する方法が分からなかった。
  * 「リンクする先があるなら辿る」を行ってみるものの木である状態の終了条件が考えつかなかった。
 

* 実装
  * listのあるindexに値を追加したい。
    * listはlistで値を持っている（ネストされている）
    * `some_list[index] += value`と書くと`some_list[index]`にsome_listが入ってしまってハマった
    * `some_list[index] = some_list[index] + value`と書くと思い通りに扱えた。

```python


N, M = [int(i) for i in input().split()]
tree = [[int(i) for i in input().split()] for _ in range(M)]

# print(tree)

link_list = [[]] * (N + 1)
# print(link_list)

for node, j in tree:
    # print(node, j)
    temp = link_list[node] + [j]
    link_list[node] = temp

visited = [0]*(N+1)

def search(k):

    if visited[k] == 1:
        return False
    else:
        que = [k, link_list[k]]

    print(que)
    is_search = True
    while is_search:
        x, y = que
        visited[x] = 1
        if y == []:
            is_search = False
        else:
            for i in y:
                if visited[i] == 1:
                    is_search = False
                    return False
                else:
                    visited[i] = 1
                    que = [i, link_list[i]]
    return True

cnt = -1
for k in range(N):
    if search(k):
        cnt += 1

print(cnt)

```

