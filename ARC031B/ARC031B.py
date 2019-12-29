# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\ARC031B\input.txt', 'r', encoding="utf-8")
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
import copy
map_grid = [[ i for i in input()] for _ in range(10)]

print(map_grid)

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
        print(temp_grid)
        print('-----------------------')



    


