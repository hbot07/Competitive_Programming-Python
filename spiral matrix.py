import sys

n = 4

matrix = [[0 for i in range(n)] for j in range(n)]
count = 1
for i in range(n):
    for j in range(n):
        matrix[i][j] = count
        count += 1

a = 0, 0
b = 0, n
c = n, n
d = n, 0


def go_right():
    global a, b
    for i in range(a[1], b[1]):
        print(matrix[a[0]][i])
    a = a[0] + 1, a[1]
    b = b[0] + 1, b[1]
    if a == b:
        sys.exit()
    go_down()


def go_left():
    global c, d
    for i in range(c[1] - 1, d[1] - 1, -1):
        print(matrix[c[0] - 1][i])
    c = c[0] - 1, c[1]
    d = d[0] - 1, d[1]
    if c == d:
        sys.exit()
    go_up()


def go_down():
    global b, c
    for i in range(b[0], c[0]):
        print(matrix[i][b[1] - 1])
    b = b[0], b[1] - 1
    c = c[0], c[1] - 1
    if c == b:
        sys.exit()
    go_left()


def go_up():
    global d, a
    for i in range(d[0] - 1, a[0] - 1, -1):
        print(matrix[i][d[1]])
    d = d[0], d[1] + 1
    a = a[0], a[1] + 1
    if a == d:
        sys.exit()
    go_right()


go_right()
