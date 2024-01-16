def search_matrix(A, key):
    h = len(A)
    w = len(A[0])

    def search_subarea(top_row, left_col, bottom_row, right_col):  # 部分行列を探索する関数
        if top_row > bottom_row or left_col > right_col:  # 領域が存在しなければ探索しない
            return (-1, -1)

        mid_row = (top_row + bottom_row) // 2  # 真ん中の行
        left, right = left_col, right_col
        while left <= right:  # 二分探索
            mid_col = (left+right) // 2
            if A[mid_row][mid_col] < key:
                left = mid_col + 1
            elif A[mid_row][mid_col] == key:
                return (mid_row, mid_col)
            else:
                right = mid_col - 1

        # 発見できなければ2つの部分行列を探索
        upper_right = search_subarea(top_row, left, mid_row - 1, right_col)
        lower_left = search_subarea(mid_row + 1, left_col, bottom_row, right)

        if upper_right != (-1, -1):
            return upper_right
        elif lower_left != (-1, -1):
            return lower_left
        else:
            return (-1, -1)

    return search_subarea(0, 0, h-1, w-1)

key = int(input("enter num (1~30):"))

T = [[1, 4, 7, 11, 15],
     [2, 5, 8, 12, 19],
     [3, 6, 9, 16, 22],
     [10, 13, 14, 17, 24],
     [18, 21, 23, 26, 30]]

print(search_matrix(T, key))