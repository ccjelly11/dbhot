'''
        2048游戏核心算法
'''
list_merge = None


# 1.练习1：零元素移至末尾
def zero_to_end():
    '''
        0元素移动到末尾
    :param list_merge:
    :return:
    '''
    for i in range(-1, -len(list_merge) - 1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


# 列表删除，从后往前！复习！
# 测试代码
# zero_to_end()
# print(list_merge)


# 1.练习2：将相同数字合并
def merge():
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] = list_merge[i] * 2
            del list_merge[i + 1]
            # list_merge.remove(list_merge[i+1])这里不能用！[4,8,4,0]删的是第一个！！
            # remove() 一次删除一个元素; 如果列表内有重复元素则删除第一个
            list_merge.append(0)


# merge()
# print(list_merge)

# 1.练习3：地图向左移动
map = [
    [2, 0, 0, 2],
    [4, 4, 2, 2],
    [2, 4, 0, 4],
    [0, 0, 2, 2]
]


def move_left():
    '''
        向左移动
    :return:
    '''
    # 思想：将二维列表中每行交给merge
    for line in map:
        global list_merge
        list_merge = line
        merge()
        # 加global的原因是此时进入 merge函数，
        # 开辟新的函数空间，这个新空间里面是没有这个函数中自己创建的list_merge的，
        # 那么在merge中只能调用全局变量merge，此时为None，会出问题

move_left()
print(map)

def move_right():
    '''
        向右移动
    :return:
    '''
    for line in map:
        global list_merge
        # 从右向左取出数据，形成新列表
        list_merge = line[::-1]
        merge()
        # 从右向左接受 合并后的数据
        line[::-1] = list_merge


# move_right()
# print(map)

def square_matrix_transpose(square_matrix):
    for r in range(len(square_matrix) - 1):
        for c in range(r + 1, len(square_matrix[0])):
            square_matrix[r][c], square_matrix[c][r] = square_matrix[c][r], square_matrix[r][c]


# 1.练习4：地图向上移动
def move_up():
    square_matrix_transpose(map)
    move_left()
    square_matrix_transpose(map)


# move_up()
# print(map)

# 1.练习4：地图向下移动
def move_down():
    square_matrix_transpose(map)
    move_right()
    square_matrix_transpose(map)
# move_down()
# print(map)


'''
    # 总结：写程序过程中犯得几个错误:
    ①删除从前往后删除！！
    ②list用remove删除导致与①弄巧成拙写出来的练习1反而没问题，但是后续
    利用该函数时，陆续出现问题！！
    ③remove删除的是匹配的第一个
'''







#自己写的
list_merge = None


def zero_to_end():
    for i in range(len(list_merge) - 1,-1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


def merge():
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] *= 2
            del list_merge[i + 1]
            list_merge.append(0)


map = [
    [2, 4, 0, 0],
    [2, 0, 0, 2],
    [0, 2, 0, 2],
    [4, 2, 2, 4]
]


def move_left():
    for line in map:
        global list_merge
        list_merge = line
        merge()


def move_right():
    for line in map:
        global list_merge
        list_merge = line[::-1]
        merge()
        line[::-1] = list_merge


def square_matrix_transpose(square_matrix):
    for r in range(len(square_matrix) - 1):
        for c in range(r + 1, len(square_matrix)):
            square_matrix[r][c], square_matrix[c][r] = square_matrix[c][r], square_matrix[r][c]


def move_up():
    square_matrix_transpose(map)
    move_left()
    square_matrix_transpose(map)


def move_down():
    square_matrix_transpose(map)
    move_right()
    square_matrix_transpose(map)

move_up()
print(map)