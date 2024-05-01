import numpy as np
import matplotlib 
import matplotlib.pyplot as plt 
import matplotlib.patches as ptc
import math as mt

def sao_paulo(ax, escala, spa_x=0, spa_y=0):
    # losango
    los_vertices = [(0.50+spa_x,0.0+spa_y), (0.14+spa_x,0.44+spa_y), 
    (0.14+spa_x,0.72+spa_y), (0.86+spa_x,0.72+spa_y), (0.86+spa_x,0.44+spa_y)]
    los = ptc.Polygon(los_vertices, 
                    closed=True,
                    facecolor='w',
                    edgecolor='k',
                    lw=1)
    los_vertices2 = [(0.44+spa_x,0.14+spa_y), (0.18+spa_x,0.45+spa_y), 
    (0.44+spa_x,0.45+spa_y)]
    los2 = ptc.Polygon(los_vertices2, 
                    closed=True,
                    facecolor='r',
                    edgecolor='r',
                    lw=1)

    los_vertices3 = [(0.56+spa_x,0.14+spa_y), (0.56+spa_x,0.45+spa_y), 
    (0.82+spa_x,0.45+spa_y)]
    los3 = ptc.Polygon(los_vertices3, 
                    closed=True,
                    facecolor='k',
                    edgecolor='k',
                    lw=1)

    los_vertices4 = [(0.18+spa_x,0.50+spa_y), (0.18+spa_x,0.68+spa_y), 
    (0.82+spa_x,0.68+spa_y), (0.82+spa_x,0.50+spa_y)]
    los4 = ptc.Polygon(los_vertices4, 
                    closed=True,
                    facecolor='k',
                    edgecolor='k',
                    lw=1)



    ax.add_patch(los)
    ax.add_patch(los2)
    ax.add_patch(los3)
    ax.add_patch(los4)

    ax.plot([0.78+spa_x , 0.78+spa_x , 0.69+spa_x, 0.69+spa_x , 0.78+spa_x , 0.78+spa_x],
    [0.55+spa_y , 0.54+spa_y , 0.54+spa_y, 0.64+spa_y , 0.64+spa_y , 0.63+spa_y],
    c='w',linewidth=5*3/escala, mec='w')

    # ffffffffffffffffffffffffffffff

    ax.plot([0.53+spa_x , 0.53+spa_x , 0.60+spa_x, 0.53+spa_x , 0.53+spa_x , 0.62+spa_x],
    [0.54+spa_y , 0.59+spa_y , 0.59+spa_y, 0.59+spa_y , 0.64+spa_y , 0.64+spa_y],
    c='w',linewidth=5*3/escala, mec='w')

    # ppppppppppppppppppppppppppppppp

    ax.plot([0.37+spa_x , 0.37+spa_x , 0.47+spa_x, 0.47+spa_x , 0.37+spa_x , 0.37+spa_x],
    [0.54+spa_y , 0.59+spa_y , 0.59+spa_y, 0.64+spa_y , 0.64+spa_y, 0.59+spa_y ],
    c='w',linewidth=5*3/escala, mec='w')

    # ssssssssssssssssssssssssssssss

    ax.plot([0.22+spa_x , 0.31+spa_x , 0.31+spa_x, 0.22+spa_x , 0.22+spa_x , 0.31+spa_x],
    [0.54+spa_y , 0.54+spa_y , 0.59+spa_y , 0.59+spa_y, 0.64+spa_y , 0.64+spa_y],
    c='w',linewidth=5*3/escala, mec='w')


    #[(0.25+spa_x,0.43+spa_y), (0.55+spa_x,0,43+spa_y)]

    #ax.plot([0.25+spa_x , 0.4+spa_x , 0.55+spa_x],[0.43+spa_y , 0.43+spa_y , 0.43+spa_y],'*',
    #c='y',markersize=20, mec='k')

    ax.plot([0.24+spa_x , 0.76+spa_x ],[0.79+spa_y , 0.79+spa_y],'*',
    c='y',markersize=20*3/escala, mec='k')

    ax.plot([0.41+spa_x , 0.59+spa_x , 0.50+spa_x],[0.79+spa_y , 0.79+spa_y , 0.91+spa_y],'*',
    c='r',markersize=20*3/escala, mec='k')

    
    

def flamengo(ax,escala,spa_x=0,spa_y=0):

    '''# losango
    los_vertices = [(0.50+spa_x,0.0+spa_y), (0.58+spa_x,0.04+spa_y),(0.60+spa_x,0.06+spa_y), 
    (0.64+spa_x,0.08+spa_y), (0.68+spa_x,0.11+spa_y), (0.75+spa_x,0.18+spa_y),
    (0.80+spa_x,0.26+spa_y), (0.83+spa_x,0.31+spa_y), (0.86+spa_x,0.39+spa_y),
    (0.88+spa_x,0.50+spa_y), (0.89+spa_x,0.57+spa_y), (0.89+spa_x,0.99+spa_y),
    (1-0.89+spa_x,0.99+spa_y), (1-0.89+spa_x,0.57+spa_y), (1-0.88+spa_x,0.50+spa_y),
    (1-0.86+spa_x,0.39+spa_y), (1-0.83+spa_x,0.31+spa_y), (1-0.80+spa_x,0.26+spa_y),
    (1-0.75+spa_x,0.18+spa_y), (1-0.68+spa_x,0.11+spa_y), (1-0.64+spa_x,0.08+spa_y),
    (1-0.60+spa_x,0.06+spa_y), (1-0.58+spa_x,0.04+spa_y),
    ]
    los = ptc.Polygon(los_vertices, 
                    closed=True,
                    facecolor='r',
                    edgecolor='k',
                    lw=4)'''



    rec_vertices = [(0.15+spa_x,0.66+spa_y), (0.15+spa_x,0.95+spa_y),(0.48+spa_x,0.95+spa_y), 
    (0.48+spa_x,0.66+spa_y)]

    rec = ptc.Polygon(rec_vertices, 
                    closed=True,
                    facecolor='r',
                    edgecolor='k',
                    lw=4)

    # losango
    los_vertices = [(0.50+spa_x,0.02+spa_y), (-0.02+0.58+spa_x,0.02+0.04+spa_y),
    (-0.02+0.60+spa_x,0.02+0.06+spa_y), (-0.02+0.64+spa_x,0.02+0.08+spa_y), 
    (-0.02+0.68+spa_x,0.02+0.11+spa_y), (-0.02+0.75+spa_x,0.02+0.18+spa_y),
    (-0.02+0.80+spa_x,0.02+0.26+spa_y), (-0.02+0.83+spa_x,0.02+0.31+spa_y), 
    (-0.02+0.86+spa_x,0.02+0.39+spa_y), (-0.02+0.88+spa_x,0.50+spa_y), 
    (-0.02+0.89+spa_x,-0.02+0.57+spa_y), (-0.02+0.89+spa_x,-0.02+0.99+spa_y),
    (0.02+1-0.89+spa_x,-0.02+0.99+spa_y), (0.02+1-0.89+spa_x,-0.02+0.57+spa_y), 
    (0.02+1-0.88+spa_x,0.50+spa_y), (0.02+1-0.86+spa_x,0.02+0.39+spa_y), 
    (0.02+1-0.83+spa_x,0.02+0.31+spa_y), (0.02+1-0.80+spa_x,0.02+0.26+spa_y),
    (0.02+1-0.75+spa_x,0.02+0.18+spa_y), (0.02+1-0.68+spa_x,0.02+0.11+spa_y), 
    (0.02+1-0.64+spa_x,0.02+0.08+spa_y),
    (0.02+1-0.60+spa_x,0.02+0.06+spa_y), (0.02+1-0.58+spa_x,0.02+0.04+spa_y),
    ]
    los = ptc.Polygon(los_vertices, 
                    closed=True,
                    facecolor='r',
                    edgecolor='k',
                    lw=6,)

    rec_vertices2 = [(0.87+spa_x,0.88+spa_y), (0.87+spa_x,0.98+spa_y),(0.13+spa_x,0.98+spa_y), 
    (0.13+spa_x,0.75+spa_y), (0.23+spa_x,0.75+spa_y) ,(0.23+spa_x,0.88+spa_y)]

    rec2 = ptc.Polygon(rec_vertices2, 
                    closed=True,
                    facecolor='k',
                    edgecolor='k',
                    lw=0)

    rec_vertices3 = [(0.13+spa_x,0.63+spa_y), (0.13+spa_x,0.75+spa_y),(0.87+spa_x,0.75+spa_y), 
    (0.87+spa_x,0.63+spa_y)]

    rec3 = ptc.Polygon(rec_vertices3, 
                    closed=True,
                    facecolor='k',
                    edgecolor='k',
                    lw=0)

    rec_vertices4 = [(0.13+spa_x,0.50+spa_y), (0.16+spa_x,0.39+spa_y),(0.83+spa_x,0.39+spa_y), 
    (0.86+spa_x,0.50+spa_y)]

    rec4 = ptc.Polygon(rec_vertices4, 
                    closed=True,
                    facecolor='k',
                    edgecolor='k',
                    lw=0)

    rec_vertices5 = [(0.31+spa_x,0.14+spa_y), (0.69+spa_x,0.14+spa_y),(0.78+spa_x,0.26+spa_y), 
    (0.22+spa_x,0.26+spa_y)]

    rec5 = ptc.Polygon(rec_vertices5, 
                    closed=True,
                    facecolor='k',
                    edgecolor='k',
                    lw=0)



    ax.add_patch(los)
    ax.add_patch(rec2)
    ax.add_patch(rec3)
    ax.add_patch(rec4)
    ax.add_patch(rec5)

    ax.add_patch(rec)

    ax.plot([0.34+spa_x, 0.34+spa_x, 0.41+spa_x  , 0.41+spa_x , 
    0.41+spa_x ,0.41+spa_x, 0.34+spa_x, 0.34+spa_x, 0.44+spa_x, 0.44+spa_x ],
    [0.69+spa_y, 0.79+spa_y, 0.78+spa_y  , 0.77+spa_y ,  
    0.79+spa_y, 0.78+spa_y, 0.79+spa_y, 0.88+spa_y, 0.88+spa_y, 0.86+spa_y],
    c='w',linewidth=4*3/escala, mec='k')

    ax.plot([0.43+spa_x, 0.40+spa_x, 0.33+spa_x  , 0.27+spa_x , 
    0.27+spa_x ,0.27+spa_x, 0.35+spa_x, 0.39+spa_x, 0.33+spa_x],
    [0.70+spa_y, 0.69+spa_y, 0.78+spa_y  , 0.78+spa_y ,  
    0.69+spa_y, 0.92+spa_y, 0.92+spa_y, 0.87+spa_y, 0.78+spa_y],
    c='w',linewidth=4*3/escala, mec='k')

    ax.plot([0.29+spa_x, 0.22+spa_x, 0.20+spa_x  , 0.22+spa_x , 0.30+spa_x],
    [0.73+spa_y, 0.75+spa_y, 0.81+spa_y  , 0.87+spa_y , 0.90+spa_y],
    c='w',linewidth=4*3/escala, mec='k')

   
# flamengo(ax,3)

# sao_paulo(ax,3)