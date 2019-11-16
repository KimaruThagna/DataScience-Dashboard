import plotly.plotly as py
import plotly.figure_factory as ff
import plotly.graph_objs as go
import numpy as np
# imaginary Sales data. 

data  =  [['A', 'B', 'C', 'D', 'E'],
        [16, 3, 28, 0, 18],
        [18, 0, 12, 5, 29],
        [9, 11, 17, 27, 0],
        [19, 0, 31, 11, 12],
        [23, 17, 10, 0, 34]]


matrix = np.array([[16,  3, 28,  0, 18],
                 [18,  0, 12,  5, 29],
                 [ 9, 11, 17, 27,  0],
                 [19,  0, 31, 11, 12],
                 [23, 17, 10,  0, 34]], dtype = int)
L,M =  matrix.shape
table  =  ff.create_table(data, index = True)
#table.write_html('Data-Table.html', auto_open = True)

'''
Create ideograms which are arcs defined by the column total
'''
PI = np.pi

def moduloAB(x, a, b): #maps a real number onto the unit circle identified with
                       #the interval [a,b), b-a = 2*PI
        if a>=b:
            raise ValueError('Incorrect interval ends')
        y = (x-a)%(b-a)
        return y+b if y<0 else y+a

def test_2PI(x):
    return 0<=x <2*PI

row_sum = [np.sum(matrix[k,:]) for k in range(L)]

#set the gap between two consecutive ideograms
gap = 2*PI*0.005
ideogram_length = 2*PI*np.asarray(row_sum)/sum(row_sum)-gap*np.ones(L) # length of the arcs based on row sum


# generate coordinates of the ideogram arcs
def get_ideogram_ends(ideogram_len, gap):
    ideo_ends = []
    left = 0
    for k in range(len(ideogram_len)):
        right = left+ideogram_len[k]
        ideo_ends.append([left, right])
        left = right+gap
    return ideo_ends

ideo_ends  =  get_ideogram_ends(ideogram_length, gap)
print(f'The coordinates of the ideogram ends {ideo_ends}')

# convert the output of get_ideogram_ends into complex numbers in polar form for plotting purposes by plotly
def make_ideogram_arc(R, phi, a=50):
    # R is the circle radius
    # phi is the list of ends angle coordinates of an arc
    # a is a parameter that controls the number of points to be evaluated on an arc
    if not test_2PI(phi[0]) or not test_2PI(phi[1]):
        phi=[moduloAB(t, 0, 2*PI) for t in phi]
    length=(phi[1]-phi[0])% 2*PI
    nr=5 if length<=PI/4 else int(a*length/PI)

    if phi[0] < phi[1]:
        theta=np.linspace(phi[0], phi[1], nr)
    else:
        phi=[moduloAB(t, -PI, PI) for t in phi]
        theta=np.linspace(phi[0], phi[1], nr)
    return R*np.exp(1j*theta)

# set ideogram colors

labels=['A', 'B', 'C', 'D', 'E']
ideo_colors=['rgba(244, 109, 67, 0.75)',
             'rgba(100, 174, 97, 1)',
             'rgba(254, 5, 139, 0.55)',
             'rgba(254, 239, 139, 0.75)',
             'rgba(12, 7, 106, 0.75)']#brewer colors with alpha set on 0.75

# map data from the matrix onto the ideogram
def map_data(data_matrix, row_value, ideogram_length):
    mapped = np.zeros(data_matrix.shape)
    for j  in range(L):
        mapped[:, j] = ideogram_length*data_matrix[:,j]/row_value
    return mapped

mapped_data = map_data(matrix, row_sum, ideogram_length)
print(f'Mapped data {mapped_data}')

idx_sort=np.argsort(mapped_data, axis=1)

def make_ribbon_ends(mapped_data, ideo_ends,  idx_sort):
    L=mapped_data.shape[0]
    ribbon_boundary=np.zeros((L,L+1))
    for k in range(L):
        start=ideo_ends[k][0]
        ribbon_boundary[k][0]=start
        for j in range(1,L+1):
            J=idx_sort[k][j-1]
            ribbon_boundary[k][j]=start+mapped_data[k][J]
            start=ribbon_boundary[k][j]
    return [[(ribbon_boundary[k][j],ribbon_boundary[k][j+1] ) for j in range(L)] for k in range(L)]

ribbon_ends=make_ribbon_ends(mapped_data, ideo_ends,  idx_sort)
print ('ribbon ends starting from the ideogram[2]\n', ribbon_ends[2])