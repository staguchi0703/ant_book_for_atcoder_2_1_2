# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\ARC037B\input.txt', 'r', encoding="utf-8")
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