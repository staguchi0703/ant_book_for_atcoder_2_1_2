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

for i in range(H):
    for k in range(W):
        if map_grid[i][k] == 's':
            start_point = [k, i] # x(k<<w), y(i << H)
# print(start_point)


foot_print = []
d = deque()
d.append(start_point)

def temp_sign(temp_site):
    return map_grid[temp_site[0]][temp_site[1]]


while len(d) <= 0:
    temp_site = d.pop()
    if temp_sign(temp_site) == '.':
        temp_site.append()
    
