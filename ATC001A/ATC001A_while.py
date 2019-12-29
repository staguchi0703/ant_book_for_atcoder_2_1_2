# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\ATC001A\input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可
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
