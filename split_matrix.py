
import io
import numpy as np
import itertools as it

# with io.open(r'e:/rastert_l7113001.txt') as fin:
#     [fin.readline() for _ in range(6)]
#     m = np.loadtxt(fin, dtype=int)

m = np.loadtxt(r'e:/rastert_l7113001.txt', dtype=int, skiprows=6)

print('data loaded')

print(m.shape)

def split(matrix, width, height):
    result = []
    x_size, y_size = matrix.shape
    slices = it.product(range(0, x_size, width), range(0, y_size, height))
    for idx, (x, y) in enumerate(slices):
        if idx%500 == 0: print(idx)
        result.append((x, y, matrix[x:x+width, y:y+height]))
    return result

def get_head(x, y, width, height):
    return [
        "col: 234",
        "kkdkd",
        "nodeata" 
    ]

matrixs = split(m, 100, 100)

matrixs = [(x,y,m) for x, y, m in matrixs if not (m==0).any()]

matrixs.sort(key=lambda item: item[2].var(), reverse=True)

matrixs = matrixs[0:10]

for matrix in matrixs:
    x, y, m = matrix
    fname = "{0}_{1}.txt".format(x, y)
    c = io.BytesIO()
    #np.savetxt(c, m, fmt="%d")
    header = '\r\n'.join(get_head(x, y, 100, 100))
    np.savetxt(fname, m, fmt="%d", newline='\r\n', header=header, comments='')
    # with io.open(fname, 'w') as fout:
    #     # writehead
    #     fout.write("helle\n")
    #     # m.tofile("h.txt", sep=" ", format="%d")
    #     fout.write(str(c.getvalue(), 'utf-8'))
