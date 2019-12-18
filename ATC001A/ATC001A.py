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
# import pprint
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
