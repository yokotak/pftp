def search_matrix(A, key):
    h = len(A)
    w = len(A[0])

    i, j = 0, w - 1  # 右上からスタート

    while i < w and j >= 0:  # 行列の範囲から出てしまうまで続ける
        if A[i][j] < key:
            i += 1
        elif A[i][j] == key:
            return (i, j)
        else:
            j -= 1

    return (-1, -1)  # 発見できなかった場合

key = int(input("enter num (1~30):"))

T = [[1, 4, 7, 11, 15],
     [2, 5, 8, 12, 19],
     [3, 6, 9, 16, 22],
     [10, 13, 14, 17, 24],
     [18, 21, 23, 26, 30]]

print(search_matrix(T, key))