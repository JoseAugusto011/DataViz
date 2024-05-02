import matplotlib 
import matplotlib.pyplot as plt 
import matplotlib.patches as ptc

def estrela(ax, escala, spa_x=0, spa_y=0, facecor ="k", esgecor = "k", lwesge = 0):

    escala_x = escala

    escala_y = escala
    
    est_vertices = [(0.0*escala_x+spa_x,0.49*escala_y+spa_y), (-0.12*escala_x+spa_x,0.11*escala_y+spa_y), 
                    (-0.5*escala_x+spa_x,0.10*escala_y+spa_y), (-0.20*escala_x+spa_x,-0.12*escala_y+spa_y),
                    (-0.31*escala_x+spa_x,-0.5*escala_y+spa_y), (0.0*escala_x+spa_x,-0.28*escala_y+spa_y),
                    (0.30*escala_x+spa_x,-0.5*escala_y+spa_y), (0.19*escala_x+spa_x,-0.12*escala_y+spa_y),
                    (0.49*escala_x+spa_x,0.10*escala_y+spa_y), (0.11*escala_x+spa_x,0.11*escala_y+spa_y),
                    ]
    est = ptc.Polygon(est_vertices, 
                    closed=True,
                    facecolor=facecor,
                    edgecolor=esgecor,
                    lw=lwesge*escala*5)
    
    ax.add_patch(est)

def criciuma(ax, escala,  spa_x=0, spa_y=0 ,  neg=False):

    escala_x = escala
    if neg:
        escala_y = -escala
    else:
        escala_y = escala
    

    los_vertices = [(0.45*escala_x+spa_x,0.0*escala_y+spa_y), (0.23*escala_x+spa_x,0.0*escala_y+spa_y), 
                    (0.1*escala_x+spa_x,0.13*escala_y+spa_y), (0.21*escala_x+spa_x,0.24*escala_y+spa_y)]
    los = ptc.Polygon(los_vertices, 
                    closed=True,
                    facecolor='y',
                    edgecolor='k',
                    lw=2-0**((escala+0.5)//1))
    los_vertices2 = [(0.48*escala_x+spa_x,0.03*escala_y+spa_y), (0.48*escala_x+spa_x,0.25*escala_y+spa_y), 
                     (0.35*escala_x+spa_x,0.38*escala_y+spa_y), (0.24*escala_x+spa_x,0.27*escala_y+spa_y)]
    los2 = ptc.Polygon(los_vertices2, 
                    closed=True,
                    facecolor='y',
                    edgecolor='k',
                    lw=2-0**((escala+0.5)//1))
    los_vertices3 = [(0.55*escala_x+spa_x,0.0*escala_y+spa_y), (0.77*escala_x+spa_x,0.0*escala_y+spa_y), 
                     (0.90*escala_x+spa_x,0.13*escala_y+spa_y), (0.79*escala_x+spa_x,0.24*escala_y+spa_y)]
    los3 = ptc.Polygon(los_vertices3, 
                    closed=True,
                    facecolor='y',
                    edgecolor='k',
                    lw=2-0**((escala+0.5)//1))
    los_vertices4 = [(0.52*escala_x+spa_x,0.03*escala_y+spa_y), (0.52*escala_x+spa_x,0.25*escala_y+spa_y), 
                     (0.65*escala_x+spa_x,0.38*escala_y+spa_y), (0.76*escala_x+spa_x,0.27*escala_y+spa_y)]
    los4 = ptc.Polygon(los_vertices4, 
                    closed=True,
                    facecolor='y',
                    edgecolor='k',
                    lw=2-0**((escala+0.5)//1))




    ax.add_patch(los)
    ax.add_patch(los2)
    ax.add_patch(los3)
    ax.add_patch(los4)

    estrela(ax,10/100*escala, spa_x=0.34*escala_x+spa_x, spa_y=0.51*escala_y+spa_y, facecor ="y", esgecor = "k", lwesge = 2-0**((escala+0.5)//1))
    estrela(ax,10/100*escala, spa_x=0.50*escala_x+spa_x, spa_y=0.51*escala_y+spa_y, facecor ="y", esgecor = "k", lwesge = 2-0**((escala+0.5)//1))
    estrela(ax,10/100*escala, spa_x=0.66*escala_x+spa_x, spa_y=0.51*escala_y+spa_y, facecor ="y", esgecor = "k", lwesge = 2-0**((escala+0.5)//1))

def goias(ax, escala,  spa_x=0, spa_y=0 ,  neg=False):

    escala_x = escala
    if neg:
        escala_y = -escala
    else:
        escala_y = escala

    cir = ptc.Circle(xy=(0.49*escala_x+spa_x,0.49*escala_y+spa_y), 
                    radius = 0.49*escala,
                    facecolor='darkgreen',
                    edgecolor='w',
                    lw=0)

    cir2 = ptc.Circle(xy=(0.49*escala_x+spa_x,0.49*escala_y+spa_y), 
                    radius = 0.4*escala,
                    facecolor='w',
                    edgecolor='w',
                    lw=0)

    cir3 = ptc.Circle(xy=(0.49*escala_x+spa_x,0.49*escala_y+spa_y), 
                    radius = 0.33*escala,
                    facecolor='darkgreen',
                    edgecolor='w',
                    lw=0)  
    cir4 = ptc.Circle(xy=(0.49*escala_x+spa_x,0.49*escala_y+spa_y), 
                    radius = 0.24*escala,
                    facecolor='w',
                    edgecolor='w',
                    lw=0)


    los_vertices = [(0.66*escala_x+spa_x,0.51*escala_y+spa_y), (0.86*escala_x+spa_x,0.51*escala_y+spa_y),
    (0.86*escala_x+spa_x,0.60*escala_y+spa_y), (0.66*escala_x+spa_x,0.60*escala_y+spa_y),
    ]

    los = ptc.Polygon(los_vertices, 
                    closed=True,
                    facecolor='w',
                    edgecolor='k',
                    lw=0)

    los_vertices2 = [(0.50*escala_x+spa_x,0.42*escala_y+spa_y), (0.50*escala_x+spa_x,0.51*escala_y+spa_y),
    (0.81*escala_x+spa_x,0.51*escala_y+spa_y), (0.81*escala_x+spa_x,0.42*escala_y+spa_y),
    ]

    los2 = ptc.Polygon(los_vertices2, 
                    closed=True,
                    facecolor='darkgreen',
                    edgecolor='k',
                    lw=0)
            

    ax.add_patch(cir)
    ax.add_patch(cir2)
    ax.add_patch(cir3)
    ax.add_patch(cir4)
    ax.add_patch(los)
    ax.add_patch(los2)

def atletico_goianiense(ax, escala,  spa_x=0, spa_y=0 ,  neg=False):

    escala_x = escala
    if neg:
        escala_y = -escala
    else:
        escala_y = escala
    los_vertices = [(0.50*escala_x+spa_x,0.75*escala_y+spa_y), (0.79*escala_x+spa_x,0.83*escala_y+spa_y), 
                    (0.79*escala_x+spa_x,0.63*escala_y+spa_y), (0.50*escala_x+spa_x,0.41*escala_y+spa_y), 
                    (0.21*escala_x+spa_x,0.63*escala_y+spa_y), (0.21*escala_x+spa_x,0.83*escala_y+spa_y),
                    ]
    los = ptc.Polygon(los_vertices, 
                    closed=True,
                    facecolor='r',
                    edgecolor='r', 
                    lw=1)


    los_vertices2 = [(0.50*escala_x+spa_x,0.01*escala_y+spa_y), (0.79*escala_x+spa_x,0.36*escala_y+spa_y), (0.79*escala_x+spa_x,0.63*escala_y+spa_y), 
    (0.5*escala_x+spa_x,0.41*escala_y+spa_y), (0.21*escala_x+spa_x,0.63*escala_y+spa_y), (0.21*escala_x+spa_x,0.36*escala_y+spa_y),
    ]
    los2 = ptc.Polygon(los_vertices2, 
                    closed=True,
                    facecolor='k',
                    edgecolor='k',
                    lw=0)

    los_vertices3 = [(0.28*escala_x+spa_x,0.31*escala_y+spa_y), (0.23*escala_x+spa_x,0.38*escala_y+spa_y), 
    (0.23*escala_x+spa_x,0.80*escala_y+spa_y), (0.39*escala_x+spa_x,0.75*escala_y+spa_y), 
    (0.39*escala_x+spa_x,0.17*escala_y+spa_y), (0.34*escala_x+spa_x,0.24*escala_y+spa_y),

    (0.34*escala_x+spa_x,0.53*escala_y+spa_y), (0.28*escala_x+spa_x,0.57*escala_y+spa_y), 
    (0.28*escala_x+spa_x,0.62*escala_y+spa_y), (0.34*escala_x+spa_x,0.58*escala_y+spa_y), 
    (0.34*escala_x+spa_x,0.74*escala_y+spa_y), (0.28*escala_x+spa_x,0.76*escala_y+spa_y),
    ]

    los3 = ptc.Polygon(los_vertices3, 
                    closed=True,
                    facecolor='w',
                    edgecolor='k',
                    lw=0)

    los_vertices4 = [(0.58*escala_x+spa_x,0.41*escala_y+spa_y), (0.58*escala_x+spa_x,0.13*escala_y+spa_y), 
    (0.50*escala_x+spa_x,0.03*escala_y+spa_y), (0.42*escala_x+spa_x,0.13*escala_y+spa_y), 
    (0.42*escala_x+spa_x,0.74*escala_y+spa_y), (0.50*escala_x+spa_x,0.72*escala_y+spa_y),

    (0.58*escala_x+spa_x,0.74*escala_y+spa_y), (0.58*escala_x+spa_x,0.59*escala_y+spa_y), 
    (0.53*escala_x+spa_x,0.56*escala_y+spa_y), (0.53*escala_x+spa_x,0.69*escala_y+spa_y), 
    (0.5*escala_x+spa_x,0.68*escala_y+spa_y), (0.47*escala_x+spa_x,0.69*escala_y+spa_y),

    (0.47*escala_x+spa_x,0.11*escala_y+spa_y), (0.5*escala_x+spa_x,0.07*escala_y+spa_y), 
    (0.53*escala_x+spa_x,0.11*escala_y+spa_y), (0.53*escala_x+spa_x,0.37*escala_y+spa_y),
    ]

    los4 = ptc.Polygon(los_vertices4, 
                    closed=True,
                    facecolor='w',
                    edgecolor='k',
                    lw=0)

    los_vertices5 = [(0.77*escala_x+spa_x,0.65*escala_y+spa_y), (0.77*escala_x+spa_x,0.38*escala_y+spa_y), 
    (0.61*escala_x+spa_x,0.17*escala_y+spa_y), (0.61*escala_x+spa_x,0.75*escala_y+spa_y), 
    (0.77*escala_x+spa_x,0.80*escala_y+spa_y), (0.77*escala_x+spa_x,0.70*escala_y+spa_y),

    (0.72*escala_x+spa_x,0.67*escala_y+spa_y), (0.72*escala_x+spa_x,0.76*escala_y+spa_y), 
    (0.66*escala_x+spa_x,0.73*escala_y+spa_y), (0.66*escala_x+spa_x,0.27*escala_y+spa_y), 
    (0.72*escala_x+spa_x,0.33*escala_y+spa_y), (0.72*escala_x+spa_x,0.57*escala_y+spa_y),

    (0.69*escala_x+spa_x,0.55*escala_y+spa_y), (0.69*escala_x+spa_x,0.59*escala_y+spa_y), 

    ]

    los5 = ptc.Polygon(los_vertices5, 
                    closed=True,
                    facecolor='w',
                    edgecolor='k',
                    lw=0)

    ax.add_patch(los)
    ax.add_patch(los2)
    ax.add_patch(los3)
    ax.add_patch(los4)
    ax.add_patch(los5)

    bronze_color = (186/255,136/255,67/255)
    estrela(ax, 10/100*escala, spa_x=0.68*escala_x+spa_x, spa_y=0.91*escala_y+spa_y, facecor =bronze_color)
    estrela(ax, 10/100*escala, spa_x=0.32*escala_x+spa_x, spa_y=0.91*escala_y+spa_y, facecor =bronze_color)


    estrela(ax, 15/100*escala, spa_x=0.50*escala_x+spa_x, spa_y=0.90*escala_y+spa_y, facecor ="silver")

def athetico_paranaense(ax, escala,  spa_x=0, spa_y=0 ,  neg=False):

    escala_x = escala
    if neg:
        escala_y = -escala
    else:
        escala_y = escala

    # losango
    los_vertices = [(0.86*escala_x+spa_x,1*escala_y+spa_y), (0.14*escala_x+spa_x,0.41*escala_y+spa_y)
    ,(0.14*escala_x+spa_x,0.27*escala_y+spa_y),(0.86*escala_x+spa_x,0.87*escala_y+spa_y)]
    los = ptc.Polygon(los_vertices, 
                    closed=True,
                    facecolor='r',
                    edgecolor='w',
                    lw=0)

    # losango
    los_vertices2 = [(0.86*escala_x+spa_x,0.83*escala_y+spa_y), (0.15*escala_x+spa_x,0.24*escala_y+spa_y)
    ,(0.23*escala_x+spa_x,0.18*escala_y+spa_y),(0.86*escala_x+spa_x,0.70*escala_y+spa_y)]
    los2 = ptc.Polygon(los_vertices2, 
                    closed=True,
                    facecolor='k',
                    edgecolor='k',
                    lw=0)

    # losango
    los_vertices3 = [(0.78*escala_x+spa_x,0.60*escala_y+spa_y), (0.25*escala_x+spa_x,0.16*escala_y+spa_y)
    ,(0.33*escala_x+spa_x,0.10*escala_y+spa_y),(0.78*escala_x+spa_x,0.47*escala_y+spa_y)]
    los3 = ptc.Polygon(los_vertices3, 
                    closed=True,
                    facecolor='r',
                    edgecolor='w',
                    lw=0)

    # losango
    los_vertices4 = [(0.71*escala_x+spa_x,0.38*escala_y+spa_y), (0.35*escala_x+spa_x,0.08*escala_y+spa_y)
    ,(0.43*escala_x+spa_x,0.01*escala_y+spa_y),(0.71*escala_x+spa_x,0.24*escala_y+spa_y)]
    los4 = ptc.Polygon(los_vertices4, 
                    closed=True,
                    facecolor='k',
                    edgecolor='k',
                    lw=0)
    
    # losango
    letr = [(0.37*escala_x+spa_x,0.63*escala_y+spa_y), (0.37*escala_x+spa_x,0.82*escala_y+spa_y)
    ,(0.42*escala_x+spa_x,0.86*escala_y+spa_y),(0.45*escala_x+spa_x,0.86*escala_y+spa_y)
    ,(0.47*escala_x+spa_x,0.84*escala_y+spa_y),(0.47*escala_x+spa_x,0.76*escala_y+spa_y)
    ,(0.31*escala_x+spa_x,0.63*escala_y+spa_y),(0.31*escala_x+spa_x,0.73*escala_y+spa_y)
    ,(0.27*escala_x+spa_x,0.69*escala_y+spa_y),(0.27*escala_x+spa_x,0.65*escala_y+spa_y)
    ,(0.24*escala_x+spa_x,0.62*escala_y+spa_y),(0.24*escala_x+spa_x,0.67*escala_y+spa_y)
    ,(0.19*escala_x+spa_x,0.63*escala_y+spa_y),(0.17*escala_x+spa_x,0.63*escala_y+spa_y)
    ,(0.14*escala_x+spa_x,0.66*escala_y+spa_y),(0.14*escala_x+spa_x,0.82*escala_y+spa_y)
    ,(0.19*escala_x+spa_x,0.86*escala_y+spa_y),(0.21*escala_x+spa_x,0.87*escala_y+spa_y)
    ,(0.24*escala_x+spa_x,0.84*escala_y+spa_y),(0.21*escala_x+spa_x,0.82*escala_y+spa_y)
    ,(0.18*escala_x+spa_x,0.82*escala_y+spa_y),(0.18*escala_x+spa_x,0.67*escala_y+spa_y)
    ,(0.24*escala_x+spa_x,0.71*escala_y+spa_y),(0.24*escala_x+spa_x,0.82*escala_y+spa_y)
    ,(0.27*escala_x+spa_x,0.84*escala_y+spa_y),(0.27*escala_x+spa_x,0.73*escala_y+spa_y)
    ,(0.31*escala_x+spa_x,0.77*escala_y+spa_y),(0.31*escala_x+spa_x,0.81*escala_y+spa_y)
    ,(0.28*escala_x+spa_x,0.84*escala_y+spa_y),(0.30*escala_x+spa_x,0.87*escala_y+spa_y)
    ,(0.33*escala_x+spa_x,0.85*escala_y+spa_y),(0.33*escala_x+spa_x,0.67*escala_y+spa_y)
    ,(0.44*escala_x+spa_x,0.77*escala_y+spa_y),(0.44*escala_x+spa_x,0.82*escala_y+spa_y)
    ,(0.40*escala_x+spa_x,0.84*escala_y+spa_y),(0.40*escala_x+spa_x,0.65*escala_y+spa_y)
    ]
    tra = ptc.Polygon(letr, 
                    closed=True,
                    facecolor='k',
                    edgecolor='k',
                    lw=0)




    ax.add_patch(los)
    ax.add_patch(los2)
    ax.add_patch(los3)
    ax.add_patch(los4)
    ax.add_patch(tra)

def sao_paulo(ax, escala,  spa_x=0, spa_y=0 ,  neg=False):

    escala_x = escala
    if neg:
        escala_y = -escala
    else:
        escala_y = escala
    # losango
    los_vertices = [(0.50*escala_x+spa_x,0.0*escala_y+spa_y), (0.14*escala_x+spa_x,0.44*escala_y+spa_y), 
    (0.14*escala_x+spa_x,0.72*escala_y+spa_y), (0.86*escala_x+spa_x,0.72*escala_y+spa_y), (0.86*escala_x+spa_x,0.44*escala_y+spa_y)]
    los = ptc.Polygon(los_vertices, 
                    closed=True,
                    facecolor='w',
                    edgecolor='k',
                    lw=1)
    los_vertices2 = [(0.44*escala_x+spa_x,0.14*escala_y+spa_y), (0.18*escala_x+spa_x,0.45*escala_y+spa_y), 
    (0.44*escala_x+spa_x,0.45*escala_y+spa_y)]
    los2 = ptc.Polygon(los_vertices2, 
                    closed=True,
                    facecolor='r',
                    edgecolor='r',
                    lw=0)

    los_vertices3 = [(0.56*escala_x+spa_x,0.14*escala_y+spa_y), (0.56*escala_x+spa_x,0.45*escala_y+spa_y), 
    (0.82*escala_x+spa_x,0.45*escala_y+spa_y)]
    los3 = ptc.Polygon(los_vertices3, 
                    closed=True,
                    facecolor='k',
                    edgecolor='k',
                    lw=0)

    los_vertices4 = [(0.18*escala_x+spa_x,0.50*escala_y+spa_y), (0.18*escala_x+spa_x,0.68*escala_y+spa_y), 
    (0.82*escala_x+spa_x,0.68*escala_y+spa_y), (0.82*escala_x+spa_x,0.50*escala_y+spa_y)]
    los4 = ptc.Polygon(los_vertices4, 
                    closed=True,
                    facecolor='k',
                    edgecolor='k',
                    lw=0)



    ax.add_patch(los)
    ax.add_patch(los2)
    ax.add_patch(los3)
    ax.add_patch(los4)


    c_vertices = [(0.77*escala_x+spa_x,0.58*escala_y+spa_y), (0.79*escala_x+spa_x,0.58*escala_y+spa_y), 
    (0.79*escala_x+spa_x,0.54*escala_y+spa_y), (0.68*escala_x+spa_x,0.54*escala_y+spa_y),
    (0.68*escala_x+spa_x,0.66*escala_y+spa_y), (0.79*escala_x+spa_x,0.66*escala_y+spa_y),
    (0.79*escala_x+spa_x,0.62*escala_y+spa_y), (0.77*escala_x+spa_x,0.62*escala_y+spa_y),
    (0.77*escala_x+spa_x,0.64*escala_y+spa_y), (0.70*escala_x+spa_x,0.64*escala_y+spa_y),
    (0.70*escala_x+spa_x,0.56*escala_y+spa_y), (0.77*escala_x+spa_x,0.56*escala_y+spa_y),
    ]
    ccccc = ptc.Polygon(c_vertices, 
                    closed=True,
                    facecolor='w',
                    edgecolor='k',
                    lw=0)
    
    f_vertices = [(0.61*escala_x+spa_x,0.61*escala_y+spa_y), (0.61*escala_x+spa_x,0.59*escala_y+spa_y), 
    (0.54*escala_x+spa_x,0.59*escala_y+spa_y), (0.54*escala_x+spa_x,0.54*escala_y+spa_y),
    (0.52*escala_x+spa_x,0.54*escala_y+spa_y), (0.52*escala_x+spa_x,0.66*escala_y+spa_y),
    (0.64*escala_x+spa_x,0.66*escala_y+spa_y), (0.64*escala_x+spa_x,0.64*escala_y+spa_y),
    (0.54*escala_x+spa_x,0.64*escala_y+spa_y), (0.54*escala_x+spa_x,0.61*escala_y+spa_y),
    ]
    fffff = ptc.Polygon(f_vertices, 
                    closed=True,
                    facecolor='w',
                    edgecolor='k',
                    lw=0)
    
    p_vertices = [(0.38*escala_x+spa_x,0.61*escala_y+spa_y), (0.38*escala_x+spa_x,0.59*escala_y+spa_y), 
    (0.48*escala_x+spa_x,0.59*escala_y+spa_y), (0.48*escala_x+spa_x,0.66*escala_y+spa_y),
    (0.36*escala_x+spa_x,0.66*escala_y+spa_y), (0.36*escala_x+spa_x,0.54*escala_y+spa_y),
    (0.38*escala_x+spa_x,0.54*escala_y+spa_y), (0.38*escala_x+spa_x,0.64*escala_y+spa_y),
    (0.46*escala_x+spa_x,0.64*escala_y+spa_y), (0.46*escala_x+spa_x,0.61*escala_y+spa_y),
    ]
    ppppp = ptc.Polygon(p_vertices, 
                    closed=True,
                    facecolor='w',
                    edgecolor='k',
                    lw=0)
    
    s_vertices = [(0.21*escala_x+spa_x,0.56*escala_y+spa_y), (0.21*escala_x+spa_x,0.54*escala_y+spa_y), 
    (0.32*escala_x+spa_x,0.54*escala_y+spa_y), (0.32*escala_x+spa_x,0.61*escala_y+spa_y),
    (0.23*escala_x+spa_x,0.61*escala_y+spa_y), (0.23*escala_x+spa_x,0.64*escala_y+spa_y),
    (0.32*escala_x+spa_x,0.64*escala_y+spa_y), (0.32*escala_x+spa_x,0.66*escala_y+spa_y),
    (0.21*escala_x+spa_x,0.66*escala_y+spa_y), (0.21*escala_x+spa_x,0.59*escala_y+spa_y),
    (0.30*escala_x+spa_x,0.59*escala_y+spa_y), (0.30*escala_x+spa_x,0.56*escala_y+spa_y),
    ]
    sssss = ptc.Polygon(s_vertices, 
                    closed=True,
                    facecolor='w',
                    edgecolor='k',
                    lw=0)

    ax.add_patch(ccccc)
    ax.add_patch(fffff)
    ax.add_patch(ppppp)
    ax.add_patch(sssss)

    estrela(ax,10/100*escala, spa_x=0.24*escala_x+spa_x, spa_y=0.81*escala_y+spa_y, facecor ="y")

    estrela(ax,10/100*escala, spa_x=0.76*escala_x+spa_x, spa_y=0.81*escala_y+spa_y, facecor ="y")
 
    estrela(ax,10/100*escala, spa_x=0.41*escala_x+spa_x, spa_y=0.81*escala_y+spa_y, facecor ="r")

    estrela(ax,10/100*escala, spa_x=0.59*escala_x+spa_x, spa_y=0.81*escala_y+spa_y, facecor ="r")

    estrela(ax,10/100*escala, spa_x=0.50*escala_x+spa_x, spa_y=0.93*escala_y+spa_y, facecor ="r")

def fortaleza(ax, escala,  spa_x=0, spa_y=0 ,  neg=False):

    escala_x = escala
    if neg:
        escala_y = -escala
    else:
        escala_y = escala

    vermelho_color = (209/255,47/255,20/255)
    azul_color = (40/255,97/255,166/255)

    # losango
    los_vertices = [(0.49*escala_x+spa_x,0.0*escala_y+spa_y), (0.86*escala_x+spa_x,0.56*escala_y+spa_y), 
    (0.86*escala_x+spa_x,0.79*escala_y+spa_y), (0.12*escala_x+spa_x,0.79*escala_y+spa_y), 
    (0.12*escala_x+spa_x,0.56*escala_y+spa_y)]
    los = ptc.Polygon(los_vertices, 
                    closed=True,
                    facecolor=azul_color,
                    edgecolor=azul_color,
                    lw=1)

    los_vertices5 = [(0.49*escala_x+spa_x,0.04*escala_y+spa_y), (0.84*escala_x+spa_x,0.57*escala_y+spa_y), 
    (0.14*escala_x+spa_x,0.57*escala_y+spa_y)]
    los5 = ptc.Polygon(los_vertices5, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=1)

    los_vertices2 = [(0.48*escala_x+spa_x,0.10*escala_y+spa_y), (0.48*escala_x+spa_x,0.55*escala_y+spa_y), 
    (0.18*escala_x+spa_x,0.55*escala_y+spa_y)]
    los2 = ptc.Polygon(los_vertices2, 
                    closed=True,
                    facecolor=azul_color,
                    edgecolor=azul_color,
                    lw=1)

    los_vertices3 = [(0.50*escala_x+spa_x,0.10*escala_y+spa_y), (0.80*escala_x+spa_x,0.55*escala_y+spa_y), 
    (0.50*escala_x+spa_x,0.55*escala_y+spa_y)]
    los3 = ptc.Polygon(los_vertices3, 
                    closed=True,
                    facecolor=vermelho_color,
                    edgecolor=vermelho_color,
                    lw=1)

    los_vertices4 = [(0.14*escala_x+spa_x,0.59*escala_y+spa_y), (0.14*escala_x+spa_x,0.76*escala_y+spa_y), 
    (0.84*escala_x+spa_x,0.76*escala_y+spa_y), (0.84*escala_x+spa_x,0.59*escala_y+spa_y)]
    los4 = ptc.Polygon(los_vertices4, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=1)


    ax.add_patch(los)
    ax.add_patch(los5)
    ax.add_patch(los2)
    ax.add_patch(los3)
    ax.add_patch(los4)


    fff_vertices = [(0.16*escala_x+spa_x,0.62*escala_y+spa_y), (0.18*escala_x+spa_x,0.62*escala_y+spa_y), 
    (0.18*escala_x+spa_x,0.66*escala_y+spa_y), (0.21*escala_x+spa_x,0.66*escala_y+spa_y),
    (0.21*escala_x+spa_x,0.68*escala_y+spa_y), (0.18*escala_x+spa_x,0.68*escala_y+spa_y),
    (0.18*escala_x+spa_x,0.70*escala_y+spa_y), (0.21*escala_x+spa_x,0.70*escala_y+spa_y),
    (0.21*escala_x+spa_x,0.72*escala_y+spa_y), (0.16*escala_x+spa_x,0.72*escala_y+spa_y),
    ]
    ffffff = ptc.Polygon(fff_vertices, 
                    closed=True,
                    facecolor=azul_color,
                    edgecolor=azul_color,
                    lw=0)
    
    ooo_vertices = [(0.28*escala_x+spa_x,0.67*escala_y+spa_y), (0.3*escala_x+spa_x,0.67*escala_y+spa_y), 
    (0.30*escala_x+spa_x,0.70*escala_y+spa_y), (0.28*escala_x+spa_x,0.72*escala_y+spa_y),
    (0.25*escala_x+spa_x,0.72*escala_y+spa_y), (0.23*escala_x+spa_x,0.70*escala_y+spa_y),
    (0.23*escala_x+spa_x,0.64*escala_y+spa_y), (0.25*escala_x+spa_x,0.62*escala_y+spa_y),
    (0.28*escala_x+spa_x,0.62*escala_y+spa_y), (0.30*escala_x+spa_x,0.64*escala_y+spa_y),
    (0.30*escala_x+spa_x,0.68*escala_y+spa_y), (0.28*escala_x+spa_x,0.68*escala_y+spa_y), 
    (0.28*escala_x+spa_x,0.64*escala_y+spa_y), (0.25*escala_x+spa_x,0.64*escala_y+spa_y), 
    (0.25*escala_x+spa_x,0.70*escala_y+spa_y), (0.28*escala_x+spa_x,0.70*escala_y+spa_y), 
    ]
    oooooo = ptc.Polygon(ooo_vertices, 
                    closed=True,
                    facecolor=azul_color,
                    edgecolor=azul_color,
                    lw=0)
    
    rrr_vertices = [(0.34*escala_x+spa_x,0.62*escala_y+spa_y), (0.32*escala_x+spa_x,0.62*escala_y+spa_y), 
    (0.32*escala_x+spa_x,0.72*escala_y+spa_y), (0.36*escala_x+spa_x,0.72*escala_y+spa_y),
    (0.38*escala_x+spa_x,0.70*escala_y+spa_y), (0.38*escala_x+spa_x,0.69*escala_y+spa_y),
    (0.36*escala_x+spa_x,0.67*escala_y+spa_y), (0.38*escala_x+spa_x,0.65*escala_y+spa_y),
    (0.38*escala_x+spa_x,0.62*escala_y+spa_y), (0.36*escala_x+spa_x,0.62*escala_y+spa_y),
    (0.36*escala_x+spa_x,0.65*escala_y+spa_y), (0.35*escala_x+spa_x,0.66*escala_y+spa_y), 
    (0.34*escala_x+spa_x,0.66*escala_y+spa_y), (0.34*escala_x+spa_x,0.69*escala_y+spa_y), 
    (0.36*escala_x+spa_x,0.69*escala_y+spa_y), (0.36*escala_x+spa_x,0.70*escala_y+spa_y),
    (0.34*escala_x+spa_x,0.70*escala_y+spa_y), (0.34*escala_x+spa_x,0.69*escala_y+spa_y),
    (0.35*escala_x+spa_x,0.69*escala_y+spa_y), (0.35*escala_x+spa_x,0.66*escala_y+spa_y),
    (0.34*escala_x+spa_x,0.66*escala_y+spa_y),
    ]
    rrrrrr = ptc.Polygon(rrr_vertices, 
                    closed=True,
                    facecolor=azul_color,
                    edgecolor=azul_color,
                    lw=0)
    
    ttt_vertices = [(0.44*escala_x+spa_x,0.62*escala_y+spa_y), (0.44*escala_x+spa_x,0.70*escala_y+spa_y), 
    (0.47*escala_x+spa_x,0.70*escala_y+spa_y), (0.47*escala_x+spa_x,0.72*escala_y+spa_y),
    (0.39*escala_x+spa_x,0.72*escala_y+spa_y), (0.39*escala_x+spa_x,0.70*escala_y+spa_y),
    (0.42*escala_x+spa_x,0.70*escala_y+spa_y), (0.42*escala_x+spa_x,0.62*escala_y+spa_y),
    ]
    tttttt = ptc.Polygon(ttt_vertices, 
                    closed=True,
                    facecolor=azul_color,
                    edgecolor=azul_color,
                    lw=0)
    
    aaa_vertices = [(0.48*escala_x+spa_x,0.62*escala_y+spa_y), (0.46*escala_x+spa_x,0.62*escala_y+spa_y), 
    (0.49*escala_x+spa_x,0.72*escala_y+spa_y), (0.50*escala_x+spa_x,0.72*escala_y+spa_y),
    (0.53*escala_x+spa_x,0.62*escala_y+spa_y), (0.51*escala_x+spa_x,0.62*escala_y+spa_y),
    (0.51*escala_x+spa_x,0.64*escala_y+spa_y), (0.49*escala_x+spa_x,0.64*escala_y+spa_y),
    (0.49*escala_x+spa_x,0.66*escala_y+spa_y), (0.51*escala_x+spa_x,0.66*escala_y+spa_y),
    (0.50*escala_x+spa_x,0.69*escala_y+spa_y), (0.49*escala_x+spa_x,0.69*escala_y+spa_y), 
    (0.48*escala_x+spa_x,0.66*escala_y+spa_y), (0.50*escala_x+spa_x,0.66*escala_y+spa_y), 
    (0.50*escala_x+spa_x,0.64*escala_y+spa_y), (0.48*escala_x+spa_x,0.64*escala_y+spa_y),
    ]
    aaaaaa = ptc.Polygon(aaa_vertices, 
                    closed=True,
                    facecolor=azul_color,
                    edgecolor=azul_color,
                    lw=0)
    
    lll_vertices = [(0.55*escala_x+spa_x,0.62*escala_y+spa_y), (0.60*escala_x+spa_x,0.62*escala_y+spa_y), 
    (0.60*escala_x+spa_x,0.64*escala_y+spa_y), (0.57*escala_x+spa_x,0.64*escala_y+spa_y),
    (0.57*escala_x+spa_x,0.72*escala_y+spa_y), (0.55*escala_x+spa_x,0.72*escala_y+spa_y),
    ]
    llllll = ptc.Polygon(lll_vertices, 
                    closed=True,
                    facecolor=azul_color,
                    edgecolor=azul_color,
                    lw=0)
    
    eee_vertices = [(0.62*escala_x+spa_x,0.62*escala_y+spa_y), (0.67*escala_x+spa_x,0.62*escala_y+spa_y), 
    (0.67*escala_x+spa_x,0.64*escala_y+spa_y), (0.64*escala_x+spa_x,0.64*escala_y+spa_y),
    (0.64*escala_x+spa_x,0.66*escala_y+spa_y), (0.67*escala_x+spa_x,0.66*escala_y+spa_y),
    (0.67*escala_x+spa_x,0.68*escala_y+spa_y), (0.64*escala_x+spa_x,0.68*escala_y+spa_y),
    (0.64*escala_x+spa_x,0.70*escala_y+spa_y), (0.67*escala_x+spa_x,0.70*escala_y+spa_y),
    (0.67*escala_x+spa_x,0.72*escala_y+spa_y), (0.62*escala_x+spa_x,0.72*escala_y+spa_y), 
    ]
    eeeeee = ptc.Polygon(eee_vertices, 
                    closed=True,
                    facecolor=azul_color,
                    edgecolor=azul_color,
                    lw=0)
    
    zzz_vertices = [(0.68*escala_x+spa_x,0.62*escala_y+spa_y), (0.73*escala_x+spa_x,0.62*escala_y+spa_y), 
    (0.73*escala_x+spa_x,0.64*escala_y+spa_y), (0.70*escala_x+spa_x,0.64*escala_y+spa_y),
    (0.73*escala_x+spa_x,0.69*escala_y+spa_y), (0.73*escala_x+spa_x,0.72*escala_y+spa_y),
    (0.68*escala_x+spa_x,0.72*escala_y+spa_y), (0.68*escala_x+spa_x,0.70*escala_y+spa_y),
    (0.71*escala_x+spa_x,0.70*escala_y+spa_y), (0.68*escala_x+spa_x,0.65*escala_y+spa_y),
    ]
    zzzzzz = ptc.Polygon(zzz_vertices, 
                    closed=True,
                    facecolor=azul_color,
                    edgecolor=azul_color,
                    lw=0)
    
    aaa_vertices2 = [(0.77*escala_x+spa_x,0.62*escala_y+spa_y), (0.75*escala_x+spa_x,0.62*escala_y+spa_y), 
    (0.78*escala_x+spa_x,0.72*escala_y+spa_y), (0.79*escala_x+spa_x,0.72*escala_y+spa_y),
    (0.82*escala_x+spa_x,0.62*escala_y+spa_y), (0.80*escala_x+spa_x,0.62*escala_y+spa_y),
    (0.80*escala_x+spa_x,0.64*escala_y+spa_y), (0.78*escala_x+spa_x,0.64*escala_y+spa_y),
    (0.78*escala_x+spa_x,0.66*escala_y+spa_y), (0.80*escala_x+spa_x,0.66*escala_y+spa_y),
    (0.79*escala_x+spa_x,0.69*escala_y+spa_y), (0.78*escala_x+spa_x,0.69*escala_y+spa_y), 
    (0.77*escala_x+spa_x,0.66*escala_y+spa_y), (0.79*escala_x+spa_x,0.66*escala_y+spa_y), 
    (0.79*escala_x+spa_x,0.64*escala_y+spa_y), (0.77*escala_x+spa_x,0.64*escala_y+spa_y),
    ]
    aaaaaa2 = ptc.Polygon(aaa_vertices2, 
                    closed=True,
                    facecolor=azul_color,
                    edgecolor=azul_color,
                    lw=0)
    
    ax.add_patch(ffffff)
    ax.add_patch(oooooo)
    ax.add_patch(rrrrrr)
    ax.add_patch(tttttt)
    ax.add_patch(aaaaaa)
    ax.add_patch(llllll)
    ax.add_patch(eeeeee)
    ax.add_patch(zzzzzz)
    ax.add_patch(aaaaaa2)

    bronze_color = (186/255,136/255,67/255)

    estrela(ax, 18/100*escala, spa_x=0.49*escala_x+spa_x, spa_y=0.91*escala_y+spa_y, facecor =bronze_color)

def botafogo(ax, escala,  spa_x=0, spa_y=0 ,  neg=False):

    escala_x = escala
    if neg:
        escala_y = -escala
    else:
        escala_y = escala
    # losango
    los_vertices = [(0.50*escala_x+spa_x,0.05*escala_y+spa_y), (0.52*escala_x+spa_x,0.06*escala_y+spa_y),(0.55*escala_x+spa_x,0.08*escala_y+spa_y), 
    (0.60*escala_x+spa_x,0.12*escala_y+spa_y), (0.63*escala_x+spa_x,0.14*escala_y+spa_y), (0.69*escala_x+spa_x,0.19*escala_y+spa_y),
    (0.73*escala_x+spa_x,0.24*escala_y+spa_y), (0.77*escala_x+spa_x,0.29*escala_y+spa_y), (0.79*escala_x+spa_x,0.32*escala_y+spa_y),
    (0.82*escala_x+spa_x,0.39*escala_y+spa_y), (0.86*escala_x+spa_x,0.50*escala_y+spa_y), (0.87*escala_x+spa_x,0.59*escala_y+spa_y),
    (0.88*escala_x+spa_x,0.61*escala_y+spa_y), (0.88*escala_x+spa_x,0.83*escala_y+spa_y), (0.83*escala_x+spa_x,0.84*escala_y+spa_y),
    (0.72*escala_x+spa_x,0.87*escala_y+spa_y), (0.65*escala_x+spa_x,0.91*escala_y+spa_y), (0.58*escala_x+spa_x,0.93*escala_y+spa_y),
    (0.50*escala_x+spa_x,0.95*escala_y+spa_y),  ((1-0.58)*escala_x+spa_x,0.93*escala_y+spa_y),((1-0.65)*escala_x+spa_x,0.91*escala_y+spa_y),
    ((1-0.72)*escala_x+spa_x,0.87*escala_y+spa_y), ((1-0.83)*escala_x+spa_x,0.84*escala_y+spa_y), ((1-0.88)*escala_x+spa_x,0.83*escala_y+spa_y),
    ((1-0.88)*escala_x+spa_x,0.61*escala_y+spa_y), ((1-0.87)*escala_x+spa_x,0.59*escala_y+spa_y), ((1-0.86)*escala_x+spa_x,0.50*escala_y+spa_y),
    ((1-0.82)*escala_x+spa_x,0.39*escala_y+spa_y), ((1-0.79)*escala_x+spa_x,0.32*escala_y+spa_y), ((1-0.77)*escala_x+spa_x,0.29*escala_y+spa_y),
    ((1-0.73)*escala_x+spa_x,0.24*escala_y+spa_y), ((1-0.69)*escala_x+spa_x,0.19*escala_y+spa_y), ((1-0.63)*escala_x+spa_x,0.14*escala_y+spa_y),
    ((1-0.60)*escala_x+spa_x,0.12*escala_y+spa_y), ((1-0.55)*escala_x+spa_x,0.08*escala_y+spa_y), ((1-0.52)*escala_x+spa_x,0.06*escala_y+spa_y)]
    los = ptc.Polygon(los_vertices, 
                    closed=True,
                    facecolor='w',
                    edgecolor='k',
                    lw=2)

    # losango
    los_vertices2 = [(0.50*escala_x+spa_x,0.15*escala_y+spa_y), 
    (0.55*escala_x+spa_x,0.17*escala_y+spa_y), (0.58*escala_x+spa_x,0.19*escala_y+spa_y), 
    (0.64*escala_x+spa_x,0.24*escala_y+spa_y), ((-0.05+0.73)*escala_x+spa_x,(0.05+0.24)*escala_y+spa_y), 
    ((-0.05+0.77)*escala_x+spa_x,(0.05+0.29)*escala_y+spa_y), ((-0.05+0.79)*escala_x+spa_x,(0.05+0.32)*escala_y+spa_y),
    ((-0.05+0.82)*escala_x+spa_x,(0.05+0.39)*escala_y+spa_y), ((-0.05+0.86)*escala_x+spa_x,0.50*escala_y+spa_y), 
    ((-0.05+0.87)*escala_x+spa_x,(-0.05+0.59)*escala_y+spa_y), ((-0.05+0.88)*escala_x+spa_x,(-0.05+0.61)*escala_y+spa_y), 
    ((-0.05+0.88)*escala_x+spa_x,(-0.05+0.83)*escala_y+spa_y), ((-0.05+0.83)*escala_x+spa_x,(-0.05+0.84)*escala_y+spa_y),
    ((-0.05+0.72)*escala_x+spa_x,(-0.05+0.87)*escala_y+spa_y), ((-0.05+0.65)*escala_x+spa_x,(-0.05+0.91)*escala_y+spa_y), 
    ((-0.05+0.58)*escala_x+spa_x,(-0.05+0.93)*escala_y+spa_y), (0.50*escala_x+spa_x,(-0.07+0.95)*escala_y+spa_y),  
    ((0.05+1-0.58)*escala_x+spa_x,(-0.05+0.93)*escala_y+spa_y),((0.05+1-0.65)*escala_x+spa_x,(-0.05+0.91)*escala_y+spa_y),
    ((0.05+1-0.72)*escala_x+spa_x,(-0.05+0.87)*escala_y+spa_y), ((0.05+1-0.83)*escala_x+spa_x,(-0.05+0.84)*escala_y+spa_y), 
    ((0.05+1-0.88)*escala_x+spa_x,(-0.05+0.83)*escala_y+spa_y), ((0.05+1-0.88)*escala_x+spa_x,(-0.05+0.61)*escala_y+spa_y),
    ((0.05+1-0.87)*escala_x+spa_x,(-0.05+0.59)*escala_y+spa_y), ((0.05+1-0.86)*escala_x+spa_x,0.50*escala_y+spa_y),
    ((0.05+1-0.82)*escala_x+spa_x,(0.05+0.39)*escala_y+spa_y), ((0.05+1-0.79)*escala_x+spa_x,(0.05+0.32)*escala_y+spa_y), 
    ((0.05+1-0.77)*escala_x+spa_x,(0.05+0.29)*escala_y+spa_y), ((0.05+1-0.73)*escala_x+spa_x,(0.05+0.24)*escala_y+spa_y), 
    ((0.05+1-0.69)*escala_x+spa_x,(0.05+0.19)*escala_y+spa_y), ((0.05+1-0.63)*escala_x+spa_x,(0.05+0.14)*escala_y+spa_y),
    ((0.05+1-0.60)*escala_x+spa_x,(0.05+0.12)*escala_y+spa_y),]

    los2 = ptc.Polygon(los_vertices2, 
                    closed=True,
                    facecolor='k',
                    edgecolor='k',
                    lw=1)


    ax.add_patch(los)
    ax.add_patch(los2)

    estrela(ax, 45/100*escala, spa_x=0.50*escala_x+spa_x, spa_y=0.54*escala_y+spa_y, facecor ="w")

    """ax.plot([0.50*escala_x+spa_x],[0.54*escala_y+spa_y],'*',
    c='w',markersize=80*3/escala, mec='w')"""

def flamengo(ax, escala,  spa_x=0, spa_y=0 ,  neg=False):

    escala_x = escala
    if neg:
        escala_y = -escala
    else:
        escala_y = escala

    vermelho_color = (197/255,38/255,19/255)


    # losango
    los_vertices = [(0.50*escala_x+spa_x,0*escala_y+spa_y), (0.58*escala_x+spa_x,0.04*escala_y+spa_y),
    (0.60*escala_x+spa_x,0.06*escala_y+spa_y), (0.64*escala_x+spa_x,0.08*escala_y+spa_y), 
    (0.68*escala_x+spa_x,0.11*escala_y+spa_y), (0.75*escala_x+spa_x,0.18*escala_y+spa_y),
    (0.80*escala_x+spa_x,0.26*escala_y+spa_y), (0.83*escala_x+spa_x,0.31*escala_y+spa_y), 
    (0.86*escala_x+spa_x,0.39*escala_y+spa_y), (0.88*escala_x+spa_x,0.50*escala_y+spa_y), 
    (0.89*escala_x+spa_x,0.57*escala_y+spa_y), (0.89*escala_x+spa_x,0.99*escala_y+spa_y),
    ((1-0.89)*escala_x+spa_x,0.99*escala_y+spa_y), ((1-0.89)*escala_x+spa_x,0.57*escala_y+spa_y), 
    ((1-0.88)*escala_x+spa_x,0.50*escala_y+spa_y), ((1-0.86)*escala_x+spa_x,0.39*escala_y+spa_y), 
    ((1-0.83)*escala_x+spa_x,0.31*escala_y+spa_y), ((1-0.80)*escala_x+spa_x,0.26*escala_y+spa_y),
    ((1-0.75)*escala_x+spa_x,0.18*escala_y+spa_y), ((1-0.68)*escala_x+spa_x,0.11*escala_y+spa_y), 
    ((1-0.64)*escala_x+spa_x,0.08*escala_y+spa_y), ((1-0.60)*escala_x+spa_x,0.06*escala_y+spa_y), 
    ((1-0.58)*escala_x+spa_x,0.04*escala_y+spa_y)
    ]
    los = ptc.Polygon(los_vertices, 
                    closed=True,
                    facecolor='k',
                    edgecolor='k',
                    lw=0,)

    rec_vertices2 = [(0.35*escala_x+spa_x,0.13*escala_y+spa_y), (0.46*escala_x+spa_x,0.05*escala_y+spa_y),
    (0.49*escala_x+spa_x,0.04*escala_y+spa_y), (0.51*escala_x+spa_x,0.04*escala_y+spa_y), 
    (0.54*escala_x+spa_x,0.05*escala_y+spa_y) ,(0.65*escala_x+spa_x,0.13*escala_y+spa_y)
    ]

    rec2 = ptc.Polygon(rec_vertices2, 
                    closed=True,
                    facecolor=vermelho_color,
                    edgecolor=vermelho_color,
                    lw=0)

    rec_vertices3 = [(0.18*escala_x+spa_x,0.38*escala_y+spa_y), (0.18*escala_x+spa_x,0.37*escala_y+spa_y),
    (0.22*escala_x+spa_x,0.28*escala_y+spa_y), (0.23*escala_x+spa_x,0.27*escala_y+spa_y),
    (0.77*escala_x+spa_x,0.27*escala_y+spa_y), (0.78*escala_x+spa_x,0.28*escala_y+spa_y),
    (0.82*escala_x+spa_x,0.37*escala_y+spa_y), (0.82*escala_x+spa_x,0.38*escala_y+spa_y)
    ]

    rec3 = ptc.Polygon(rec_vertices3, 
                    closed=True,
                    facecolor=vermelho_color,
                    edgecolor=vermelho_color,
                    lw=0)

    rec_vertices4 = [(0.14*escala_x+spa_x,0.62*escala_y+spa_y), (0.14*escala_x+spa_x,0.52*escala_y+spa_y),
    (0.86*escala_x+spa_x,0.52*escala_y+spa_y), (0.86*escala_x+spa_x,0.62*escala_y+spa_y)
    ]

    rec4 = ptc.Polygon(rec_vertices4, 
                    closed=True,
                    facecolor=vermelho_color,
                    edgecolor=vermelho_color,
                    lw=0)

    rec_vertices5 = [(0.52*escala_x+spa_x,0.87*escala_y+spa_y), (0.52*escala_x+spa_x,0.76*escala_y+spa_y),
    (0.86*escala_x+spa_x,0.76*escala_y+spa_y), (0.86*escala_x+spa_x,0.87*escala_y+spa_y)
    ]

    rec5 = ptc.Polygon(rec_vertices5, 
                    closed=True,
                    facecolor=vermelho_color,
                    edgecolor=vermelho_color,
                    lw=0)
    
    rec_vertices = [(0.14*escala_x+spa_x,0.95*escala_y+spa_y), (0.14*escala_x+spa_x,0.66*escala_y+spa_y),
    (0.47*escala_x+spa_x,0.66*escala_y+spa_y), (0.47*escala_x+spa_x,0.95*escala_y+spa_y)
    ]

    rec = ptc.Polygon(rec_vertices, 
                    closed=True,
                    facecolor=vermelho_color,
                    edgecolor=vermelho_color,
                    lw=0)



    ax.add_patch(los)
    ax.add_patch(rec2)
    ax.add_patch(rec3)
    ax.add_patch(rec4)
    ax.add_patch(rec5)

    ax.add_patch(rec)

    letra_vertices = [(0.24*escala_x+spa_x,0.68*escala_y+spa_y), (0.25*escala_x+spa_x,0.69*escala_y+spa_y),
    (0.25*escala_x+spa_x,0.71*escala_y+spa_y), (0.26*escala_x+spa_x,0.72*escala_y+spa_y), 
    (0.23*escala_x+spa_x,0.73*escala_y+spa_y), (0.18*escala_x+spa_x,0.78*escala_y+spa_y),
    (0.17*escala_x+spa_x,0.81*escala_y+spa_y), (0.21*escala_x+spa_x,0.88*escala_y+spa_y), 
    (0.24*escala_x+spa_x,0.90*escala_y+spa_y), (0.27*escala_x+spa_x,0.91*escala_y+spa_y), 
    (0.30*escala_x+spa_x,0.91*escala_y+spa_y), (0.30*escala_x+spa_x,0.87*escala_y+spa_y),
    (0.28*escala_x+spa_x,0.89*escala_y+spa_y), (0.26*escala_x+spa_x,0.89*escala_y+spa_y), 
    (0.22*escala_x+spa_x,0.87*escala_y+spa_y), (0.20*escala_x+spa_x,0.84*escala_y+spa_y), 
    (0.20*escala_x+spa_x,0.79*escala_y+spa_y), (0.24*escala_x+spa_x,0.74*escala_y+spa_y),
    (0.29*escala_x+spa_x,0.73*escala_y+spa_y), (0.32*escala_x+spa_x,0.75*escala_y+spa_y), 
    (0.34*escala_x+spa_x,0.73*escala_y+spa_y), (0.34*escala_x+spa_x,0.69*escala_y+spa_y), 
    (0.35*escala_x+spa_x,0.68*escala_y+spa_y), (0.31*escala_x+spa_x,0.68*escala_y+spa_y), 
    (0.32*escala_x+spa_x,0.69*escala_y+spa_y), (0.32*escala_x+spa_x,0.73*escala_y+spa_y),
    (0.27*escala_x+spa_x,0.72*escala_y+spa_y), (0.27*escala_x+spa_x,0.69*escala_y+spa_y), 
    (0.28*escala_x+spa_x,0.68*escala_y+spa_y)
    ]
    let = ptc.Polygon(letra_vertices, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0,)
    
    letra_vertices2 = [
    (0.39*escala_x+spa_x,0.68*escala_y+spa_y), (0.36*escala_x+spa_x,0.73*escala_y+spa_y),
    (0.31*escala_x+spa_x,0.78*escala_y+spa_y), (0.27*escala_x+spa_x,0.78*escala_y+spa_y), 
    (0.27*escala_x+spa_x,0.74*escala_y+spa_y), (0.25*escala_x+spa_x,0.74*escala_y+spa_y),
    (0.25*escala_x+spa_x,0.87*escala_y+spa_y), (0.27*escala_x+spa_x,0.87*escala_y+spa_y), 
    (0.27*escala_x+spa_x,0.81*escala_y+spa_y), (0.29*escala_x+spa_x,0.79*escala_y+spa_y), 
    (0.32*escala_x+spa_x,0.79*escala_y+spa_y), (0.37*escala_x+spa_x,0.74*escala_y+spa_y),
    (0.37*escala_x+spa_x,0.73*escala_y+spa_y), (0.39*escala_x+spa_x,0.71*escala_y+spa_y), 
    (0.43*escala_x+spa_x,0.71*escala_y+spa_y), (0.43*escala_x+spa_x,0.70*escala_y+spa_y), 
    (0.41*escala_x+spa_x,0.68*escala_y+spa_y)
    ]
    let2 = ptc.Polygon(letra_vertices2, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0,)
    
    letra_vertices3 = [
    (0.40*escala_x+spa_x,0.76*escala_y+spa_y), (0.40*escala_x+spa_x,0.78*escala_y+spa_y),
    (0.35*escala_x+spa_x,0.78*escala_y+spa_y), (0.32*escala_x+spa_x,0.81*escala_y+spa_y), 
    (0.32*escala_x+spa_x,0.89*escala_y+spa_y), (0.36*escala_x+spa_x,0.89*escala_y+spa_y),
    (0.33*escala_x+spa_x,0.92*escala_y+spa_y), (0.30*escala_x+spa_x,0.93*escala_y+spa_y), 
    (0.25*escala_x+spa_x,0.92*escala_y+spa_y), (0.24*escala_x+spa_x,0.94*escala_y+spa_y), 
    (0.27*escala_x+spa_x,0.93*escala_y+spa_y), (0.35*escala_x+spa_x,0.93*escala_y+spa_y),
    (0.39*escala_x+spa_x,0.89*escala_y+spa_y), (0.44*escala_x+spa_x,0.89*escala_y+spa_y), 
    (0.44*escala_x+spa_x,0.86*escala_y+spa_y), (0.43*escala_x+spa_x,0.86*escala_y+spa_y), 
    (0.40*escala_x+spa_x,0.89*escala_y+spa_y), (0.39*escala_x+spa_x,0.88*escala_y+spa_y), 
    (0.40*escala_x+spa_x,0.87*escala_y+spa_y), (0.37*escala_x+spa_x,0.81*escala_y+spa_y),
    (0.37*escala_x+spa_x,0.89*escala_y+spa_y), (0.34*escala_x+spa_x,0.86*escala_y+spa_y), 
    (0.34*escala_x+spa_x,0.80*escala_y+spa_y), (0.35*escala_x+spa_x,0.79*escala_y+spa_y), 
    (0.39*escala_x+spa_x,0.79*escala_y+spa_y), (0.40*escala_x+spa_x,0.80*escala_y+spa_y), 
    (0.42*escala_x+spa_x,0.80*escala_y+spa_y), (0.42*escala_x+spa_x,0.78*escala_y+spa_y), 
    
    ]
    let3 = ptc.Polygon(letra_vertices3, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0,)
    

    ax.add_patch(let)
    ax.add_patch(let2)
    ax.add_patch(let3)

def fluminense(ax, escala,  spa_x=0, spa_y=0 ,  neg=False):

    escala_x = escala
    if neg:
        escala_y = -escala
    else:
        escala_y = escala
    grenar_color = (135/255,10/255,40/255)  # RGB values for a shade of red
    verde_color = (0/255,96/255,57/255)

    # losango
    los_vertices = [(0.50*escala_x+spa_x,1*escala_y+spa_y), (0.52*escala_x+spa_x,(1-0.03)*escala_y+spa_y), (0.61*escala_x+spa_x,(1-0.11)*escala_y+spa_y), 
    (0.70*escala_x+spa_x,(1-0.15)*escala_y+spa_y), (0.73*escala_x+spa_x,(1-0.16)*escala_y+spa_y), (0.82*escala_x+spa_x,(1-0.17)*escala_y+spa_y),
    (0.92*escala_x+spa_x,(1-0.16)*escala_y+spa_y), (0.92*escala_x+spa_x,(1-0.27)*escala_y+spa_y), (0.91*escala_x+spa_x,(1-0.34)*escala_y+spa_y),
    (0.88*escala_x+spa_x,(1-0.49)*escala_y+spa_y), (0.87*escala_x+spa_x,(1-0.50)*escala_y+spa_y), (0.81*escala_x+spa_x,(1-0.65)*escala_y+spa_y),
    (0.76*escala_x+spa_x,(1-0.73)*escala_y+spa_y), (0.73*escala_x+spa_x,(1-0.77)*escala_y+spa_y), (0.57*escala_x+spa_x,(1-0.93)*escala_y+spa_y),
    (0.50*escala_x+spa_x,(1-0.98)*escala_y+spa_y), ((1-0.57)*escala_x+spa_x,(1-0.93)*escala_y+spa_y), ((1-0.73)*escala_x+spa_x,(1-0.77)*escala_y+spa_y),
    ((1-0.76)*escala_x+spa_x,(1-0.73)*escala_y+spa_y), ((1-0.81)*escala_x+spa_x,(1-0.65)*escala_y+spa_y), ((1-0.87)*escala_x+spa_x,(1-0.50)*escala_y+spa_y),
    ((1-0.88)*escala_x+spa_x,(1-0.49)*escala_y+spa_y), ((1-0.91)*escala_x+spa_x,(1-0.34)*escala_y+spa_y), ((1-0.92)*escala_x+spa_x,(1-0.27)*escala_y+spa_y),
    ((1-0.92)*escala_x+spa_x,(1-0.16)*escala_y+spa_y), ((1-0.82)*escala_x+spa_x,(1-0.17)*escala_y+spa_y), ((1-0.73)*escala_x+spa_x,(1-0.16)*escala_y+spa_y),
    ((1-0.70)*escala_x+spa_x,(1-0.15)*escala_y+spa_y), ((1-0.61)*escala_x+spa_x,(1-0.11)*escala_y+spa_y), ((1-0.52)*escala_x+spa_x,(1-0.03)*escala_y+spa_y)
    ]
    los = ptc.Polygon(los_vertices, 
                    closed=True,
                    facecolor='w',
                    edgecolor=grenar_color, # Adjusted color here
                    lw=1)


    # losango
    los_vertices2 = [(0.50*escala_x+spa_x,(1-(0.07+0.0))*escala_y+spa_y), (0.52*escala_x+spa_x,(1-(0.06+0.03))*escala_y+spa_y), 
    (0.61*escala_x+spa_x,(1-(0.05+0.11))*escala_y+spa_y), (0.70*escala_x+spa_x,(1-(0.05+0.15))*escala_y+spa_y), 
    (0.73*escala_x+spa_x,(1-(0.05+0.16))*escala_y+spa_y), (0.82*escala_x+spa_x,(1-(0.05+0.17))*escala_y+spa_y),
    ((-0.05+0.92)*escala_x+spa_x,(1-(0.05+0.16))*escala_y+spa_y), ((-0.05+0.92)*escala_x+spa_x,(1-0.27)*escala_y+spa_y), 
    ((-0.05+0.91)*escala_x+spa_x,(1-0.34)*escala_y+spa_y),

    (0.83*escala_x+spa_x,(1-0.47)*escala_y+spa_y), ((1-0.83)*escala_x+spa_x,(1-0.47)*escala_y+spa_y),

    ((0.05+1-0.91)*escala_x+spa_x,(1-0.34)*escala_y+spa_y), ((0.05+1-0.92)*escala_x+spa_x,(1-0.27)*escala_y+spa_y),
    ((0.05+1-0.92)*escala_x+spa_x,(1-(0.05+0.16))*escala_y+spa_y), ((1-0.82)*escala_x+spa_x,(1-(0.05+0.17))*escala_y+spa_y), 
    ((1-0.73)*escala_x+spa_x,(1-(0.05+0.16))*escala_y+spa_y), ((1-0.70)*escala_x+spa_x,(1-(0.05+0.15))*escala_y+spa_y), 
    ((1-0.61)*escala_x+spa_x,(1-(0.05+0.11))*escala_y+spa_y), ((1-0.52)*escala_x+spa_x,(1-(0.06+0.03))*escala_y+spa_y)]
    los2 = ptc.Polygon(los_vertices2, 
                    closed=True,
                    facecolor=grenar_color,
                    edgecolor='k',
                    lw=0)

    los_vertices3 = [(0.82*escala_x+spa_x,(1-0.51)*escala_y+spa_y), ((-0.05+0.81)*escala_x+spa_x,(1-0.65)*escala_y+spa_y),
    ((-0.05+0.76)*escala_x+spa_x,(1-0.73)*escala_y+spa_y), ((-0.05+0.73)*escala_x+spa_x,(1-0.77)*escala_y+spa_y), 
    (0.57*escala_x+spa_x,(1-(-0.06+0.93))*escala_y+spa_y), (0.50*escala_x+spa_x,(1-(-0.06+0.98))*escala_y+spa_y), 
    ((1-0.57)*escala_x+spa_x,(1-(-0.06+0.93))*escala_y+spa_y), ((0.05+1-0.73)*escala_x+spa_x,(1-0.77)*escala_y+spa_y),
    ((0.05+1-0.76)*escala_x+spa_x,(1-0.73)*escala_y+spa_y), ((0.05+1-0.81)*escala_x+spa_x,(1-0.65)*escala_y+spa_y), 
    ((1-0.82)*escala_x+spa_x,(1-0.51)*escala_y+spa_y)]
    los3 = ptc.Polygon(los_vertices3, 
                    closed=True,
                    facecolor=verde_color,
                    edgecolor='k',
                    lw=0)

    ax.add_patch(los)
    ax.add_patch(los2)
    ax.add_patch(los3)

    letra_vertices = [
    (0.40*escala_x+spa_x,0.26*escala_y+spa_y), (0.40*escala_x+spa_x,0.29*escala_y+spa_y),
    (0.36*escala_x+spa_x,0.32*escala_y+spa_y), (0.38*escala_x+spa_x,0.43*escala_y+spa_y), 
    (0.38*escala_x+spa_x,0.48*escala_y+spa_y), (0.43*escala_x+spa_x,0.49*escala_y+spa_y),
    (0.51*escala_x+spa_x,0.49*escala_y+spa_y), (0.51*escala_x+spa_x,0.47*escala_y+spa_y), 
    (0.55*escala_x+spa_x,0.43*escala_y+spa_y), (0.53*escala_x+spa_x,0.47*escala_y+spa_y), 
    (0.53*escala_x+spa_x,0.49*escala_y+spa_y), (0.57*escala_x+spa_x,0.48*escala_y+spa_y),
    (0.57*escala_x+spa_x,0.52*escala_y+spa_y), (0.54*escala_x+spa_x,0.51*escala_y+spa_y), 
    (0.55*escala_x+spa_x,0.57*escala_y+spa_y), (0.47*escala_x+spa_x,0.57*escala_y+spa_y), 
    (0.48*escala_x+spa_x,0.67*escala_y+spa_y), (0.44*escala_x+spa_x,0.67*escala_y+spa_y),
    (0.44*escala_x+spa_x,0.53*escala_y+spa_y), (0.47*escala_x+spa_x,0.53*escala_y+spa_y), 
    (0.47*escala_x+spa_x,0.55*escala_y+spa_y), (0.52*escala_x+spa_x,0.55*escala_y+spa_y), 
    (0.52*escala_x+spa_x,0.52*escala_y+spa_y), (0.39*escala_x+spa_x,0.51*escala_y+spa_y), 
    (0.39*escala_x+spa_x,0.60*escala_y+spa_y), (0.35*escala_x+spa_x,0.58*escala_y+spa_y),
    (0.35*escala_x+spa_x,0.41*escala_y+spa_y), (0.34*escala_x+spa_x,0.40*escala_y+spa_y), 
    (0.33*escala_x+spa_x,0.37*escala_y+spa_y), (0.33*escala_x+spa_x,0.29*escala_y+spa_y), 
    (0.37*escala_x+spa_x,0.29*escala_y+spa_y)
    ]
    let = ptc.Polygon(letra_vertices, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0,)
    
    letra_vertices2 = [
    (0.32*escala_x+spa_x,0.37*escala_y+spa_y), (0.33*escala_x+spa_x,0.40*escala_y+spa_y),
    (0.28*escala_x+spa_x,0.44*escala_y+spa_y), (0.26*escala_x+spa_x,0.49*escala_y+spa_y), 
    (0.28*escala_x+spa_x,0.53*escala_y+spa_y), (0.33*escala_x+spa_x,0.58*escala_y+spa_y),
    (0.43*escala_x+spa_x,0.62*escala_y+spa_y), (0.43*escala_x+spa_x,0.64*escala_y+spa_y), 
    (0.35*escala_x+spa_x,0.62*escala_y+spa_y), (0.27*escala_x+spa_x,0.56*escala_y+spa_y), 
    (0.25*escala_x+spa_x,0.53*escala_y+spa_y), (0.21*escala_x+spa_x,0.49*escala_y+spa_y),
    (0.25*escala_x+spa_x,0.43*escala_y+spa_y), (0.30*escala_x+spa_x,0.38*escala_y+spa_y), 
    ]
    let2 = ptc.Polygon(letra_vertices2, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0,)
    
    letra_vertices3 = [
    (0.35*escala_x+spa_x,0.63*escala_y+spa_y), (0.34*escala_x+spa_x,0.69*escala_y+spa_y),
    (0.38*escala_x+spa_x,0.69*escala_y+spa_y), (0.49*escala_x+spa_x,0.71*escala_y+spa_y), 
    (0.54*escala_x+spa_x,0.71*escala_y+spa_y), (0.54*escala_x+spa_x,0.69*escala_y+spa_y),
    (0.49*escala_x+spa_x,0.69*escala_y+spa_y), (0.42*escala_x+spa_x,0.68*escala_y+spa_y), 
    (0.39*escala_x+spa_x,0.65*escala_y+spa_y)
    ]
    let3 = ptc.Polygon(letra_vertices3, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0,)
    
    letra_vertices4 = [
    (0.44*escala_x+spa_x,0.72*escala_y+spa_y), (0.40*escala_x+spa_x,0.76*escala_y+spa_y),
    (0.42*escala_x+spa_x,0.78*escala_y+spa_y), (0.49*escala_x+spa_x,0.78*escala_y+spa_y), 
    (0.57*escala_x+spa_x,0.80*escala_y+spa_y), (0.65*escala_x+spa_x,0.75*escala_y+spa_y),
    (0.62*escala_x+spa_x,0.74*escala_y+spa_y), (0.59*escala_x+spa_x,0.71*escala_y+spa_y), 
    (0.57*escala_x+spa_x,0.65*escala_y+spa_y), (0.56*escala_x+spa_x,0.66*escala_y+spa_y),
    (0.56*escala_x+spa_x,0.71*escala_y+spa_y), (0.60*escala_x+spa_x,0.75*escala_y+spa_y), 
    (0.56*escala_x+spa_x,0.78*escala_y+spa_y), (0.53*escala_x+spa_x,0.76*escala_y+spa_y),
    (0.47*escala_x+spa_x,0.75*escala_y+spa_y), (0.47*escala_x+spa_x,0.72*escala_y+spa_y), 
    
    ]
    let4 = ptc.Polygon(letra_vertices4, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0,)
    
    letra_vertices5 = [
    (0.69*escala_x+spa_x,0.53*escala_y+spa_y), (0.66*escala_x+spa_x,0.55*escala_y+spa_y),
    (0.66*escala_x+spa_x,0.57*escala_y+spa_y), (0.61*escala_x+spa_x,0.62*escala_y+spa_y), 
    (0.61*escala_x+spa_x,0.63*escala_y+spa_y), (0.68*escala_x+spa_x,0.62*escala_y+spa_y),
    (0.70*escala_x+spa_x,0.61*escala_y+spa_y), (0.67*escala_x+spa_x,0.58*escala_y+spa_y), 
    (0.67*escala_x+spa_x,0.57*escala_y+spa_y), (0.70*escala_x+spa_x,0.54*escala_y+spa_y),
    (0.73*escala_x+spa_x,0.55*escala_y+spa_y), (0.73*escala_x+spa_x,0.53*escala_y+spa_y), 
    ]
    let5 = ptc.Polygon(letra_vertices5, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0,)
    
    letra_vertices6 = [
    (0.37*escala_x+spa_x,0.35*escala_y+spa_y), (0.38*escala_x+spa_x,0.38*escala_y+spa_y),
    (0.47*escala_x+spa_x,0.37*escala_y+spa_y), (0.54*escala_x+spa_x,0.38*escala_y+spa_y), 
    (0.59*escala_x+spa_x,0.39*escala_y+spa_y), (0.66*escala_x+spa_x,0.42*escala_y+spa_y),
    (0.71*escala_x+spa_x,0.46*escala_y+spa_y), (0.76*escala_x+spa_x,0.46*escala_y+spa_y), 
    (0.77*escala_x+spa_x,0.45*escala_y+spa_y), (0.77*escala_x+spa_x,0.42*escala_y+spa_y),
    (0.73*escala_x+spa_x,0.44*escala_y+spa_y), (0.69*escala_x+spa_x,0.40*escala_y+spa_y), 
    (0.69*escala_x+spa_x,0.38*escala_y+spa_y), (0.63*escala_x+spa_x,0.38*escala_y+spa_y), 
    (0.52*escala_x+spa_x,0.35*escala_y+spa_y), (0.47*escala_x+spa_x,0.34*escala_y+spa_y),
    ]
    let6 = ptc.Polygon(letra_vertices6, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0,)
    
    letra_vertices7 = [
    (0.41*escala_x+spa_x,0.25*escala_y+spa_y), (0.43*escala_x+spa_x,0.33*escala_y+spa_y),
    (0.47*escala_x+spa_x,0.33*escala_y+spa_y), (0.49*escala_x+spa_x,0.27*escala_y+spa_y), 
    (0.53*escala_x+spa_x,0.24*escala_y+spa_y), (0.58*escala_x+spa_x,0.22*escala_y+spa_y),
    (0.55*escala_x+spa_x,0.22*escala_y+spa_y), (0.44*escala_x+spa_x,0.25*escala_y+spa_y), 
    ]
    let7 = ptc.Polygon(letra_vertices7, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0,)
    
    letra_vertices8 = [
    (0.43*escala_x+spa_x,0.21*escala_y+spa_y), (0.40*escala_x+spa_x,0.24*escala_y+spa_y),
    (0.42*escala_x+spa_x,0.24*escala_y+spa_y), (0.43*escala_x+spa_x,0.23*escala_y+spa_y), 
    (0.44*escala_x+spa_x,0.21*escala_y+spa_y)
    ]
    let8 = ptc.Polygon(letra_vertices8, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0,)
    
    letra_vertices9 = [
    (0.58*escala_x+spa_x,0.58*escala_y+spa_y), (0.60*escala_x+spa_x,0.69*escala_y+spa_y),
    (0.66*escala_x+spa_x,0.70*escala_y+spa_y), (0.66*escala_x+spa_x,0.68*escala_y+spa_y), 
    (0.60*escala_x+spa_x,0.63*escala_y+spa_y), (0.61*escala_x+spa_x,0.55*escala_y+spa_y), 
    ]
    let9 = ptc.Polygon(letra_vertices9, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0,)
    
    letra_vertices10 = [
    (0.49*escala_x+spa_x,0.63*escala_y+spa_y), (0.49*escala_x+spa_x,0.65*escala_y+spa_y),
    (0.53*escala_x+spa_x,0.65*escala_y+spa_y), (0.58*escala_x+spa_x,0.64*escala_y+spa_y), 
    (0.58*escala_x+spa_x,0.62*escala_y+spa_y)
    ]
    let10 = ptc.Polygon(letra_vertices10, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0,)
    
    letra_vertices11 = [
    (0.44*escala_x+spa_x,0.39*escala_y+spa_y), (0.47*escala_x+spa_x,0.39*escala_y+spa_y),
    (0.47*escala_x+spa_x,0.48*escala_y+spa_y), (0.44*escala_x+spa_x,0.48*escala_y+spa_y), 
    ]
    let11 = ptc.Polygon(letra_vertices11, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0,)
    
    ax.add_patch(let)
    ax.add_patch(let2)
    ax.add_patch(let3)
    ax.add_patch(let4)
    ax.add_patch(let5)
    ax.add_patch(let6)
    ax.add_patch(let7)
    ax.add_patch(let8)
    ax.add_patch(let9)
    ax.add_patch(let10)
    ax.add_patch(let11)

def vasco(ax, escala,  spa_x=0, spa_y=0 ,  neg=False):

    escala_x = escala
    if neg:
        escala_y = -escala
    else:
        escala_y = escala

    barco_color = (255/255,164/255,0/255)

    # losango
    los_vertices = [(0.50*escala_x+spa_x,0.01*escala_y+spa_y), (0.58*escala_x+spa_x,0.04*escala_y+spa_y),(0.64*escala_x+spa_x,0.08*escala_y+spa_y),  
    (0.76*escala_x+spa_x,0.20*escala_y+spa_y), (0.81*escala_x+spa_x,0.27*escala_y+spa_y), (0.82*escala_x+spa_x,0.30*escala_y+spa_y), 
    (0.86*escala_x+spa_x,0.39*escala_y+spa_y), (0.88*escala_x+spa_x,0.50*escala_y+spa_y), (0.88*escala_x+spa_x,0.75*escala_y+spa_y), 
    (0.75*escala_x+spa_x,0.75*escala_y+spa_y), (0.70*escala_x+spa_x,0.80*escala_y+spa_y), (0.69*escala_x+spa_x,0.86*escala_y+spa_y), 
    (0.70*escala_x+spa_x,0.95*escala_y+spa_y), (0.62*escala_x+spa_x,0.97*escala_y+spa_y), (0.56*escala_x+spa_x,0.98*escala_y+spa_y), 
    (0.50*escala_x+spa_x,0.98*escala_y+spa_y),
    ((1-0.56)*escala_x+spa_x,0.98*escala_y+spa_y), ((1-0.62)*escala_x+spa_x,0.97*escala_y+spa_y), ((1-0.70)*escala_x+spa_x,0.95*escala_y+spa_y),
    ((1-0.69)*escala_x+spa_x,0.86*escala_y+spa_y), ((1-0.70)*escala_x+spa_x,0.80*escala_y+spa_y), ((1-0.75)*escala_x+spa_x,0.75*escala_y+spa_y),
    ((1-0.88)*escala_x+spa_x,0.75*escala_y+spa_y), ((1-0.88)*escala_x+spa_x,0.50*escala_y+spa_y), ((1-0.86)*escala_x+spa_x,0.39*escala_y+spa_y),
    ((1-0.82)*escala_x+spa_x,0.30*escala_y+spa_y), ((1-0.81)*escala_x+spa_x,0.27*escala_y+spa_y), ((1-0.76)*escala_x+spa_x,0.20*escala_y+spa_y),
    ((1-0.64)*escala_x+spa_x,0.08*escala_y+spa_y), ((1-0.58)*escala_x+spa_x,0.04*escala_y+spa_y)
    ]
    los = ptc.Polygon(los_vertices, 
                    closed=True,
                    facecolor='w',
                    edgecolor='k',
                    lw=2)

    # losango
    los_vertices2 = [(0.50*escala_x+spa_x,0.05*escala_y+spa_y), (0.58*escala_x+spa_x,0.08*escala_y+spa_y),
    (0.64*escala_x+spa_x,+0.13*escala_y+spa_y), (0.72*escala_x+spa_x,0.20*escala_y+spa_y), 
    (0.77*escala_x+spa_x,0.27*escala_y+spa_y), (0.78*escala_x+spa_x,0.30*escala_y+spa_y), 
    (0.82*escala_x+spa_x,0.39*escala_y+spa_y), (0.84*escala_x+spa_x,0.50*escala_y+spa_y), 
    (0.85*escala_x+spa_x,0.71*escala_y+spa_y), (0.31*escala_x+spa_x,0.17*escala_y+spa_y),
    (0.36*escala_x+spa_x,0.13*escala_y+spa_y), (0.42*escala_x+spa_x,0.08*escala_y+spa_y)]
    los2 = ptc.Polygon(los_vertices2, 
                    closed=True,
                    facecolor='k',
                    edgecolor='k',
                    lw=0)

    # losango
    los_vertices3 = [(0.66*escala_x+spa_x,0.82*escala_y+spa_y), (0.66*escala_x+spa_x,0.93*escala_y+spa_y), 
    (0.62*escala_x+spa_x,0.93*escala_y+spa_y), (0.56*escala_x+spa_x,0.94*escala_y+spa_y), 
    (0.50*escala_x+spa_x,0.94*escala_y+spa_y), (0.44*escala_x+spa_x,0.94*escala_y+spa_y), 
    (0.38*escala_x+spa_x,0.93*escala_y+spa_y), (0.34*escala_x+spa_x, 0.93*escala_y+spa_y),
    ((0.04 +1-0.69)*escala_x+spa_x,0.86*escala_y+spa_y), ((0.04 +1-0.70)*escala_x+spa_x,0.80*escala_y+spa_y), 
    (0.25*escala_x+spa_x,0.71*escala_y+spa_y), (0.15*escala_x+spa_x,0.71*escala_y+spa_y), 
    ((0.04 + 1 -0.88)*escala_x+spa_x,0.50*escala_y+spa_y), (0.19*escala_x+spa_x,0.35*escala_y+spa_y),
    ]
    los3 = ptc.Polygon(los_vertices3, 
                    closed=True,
                    facecolor='k',
                    edgecolor='k',
                    lw=0)

    los_vertices4 = [(0.40*escala_x+spa_x,0.67*escala_y+spa_y), (0.43*escala_x+spa_x,0.70*escala_y+spa_y), (0.44*escala_x+spa_x,0.72*escala_y+spa_y), 
    (0.40*escala_x+spa_x,0.72*escala_y+spa_y),

    ]
    los4 = ptc.Polygon(los_vertices4, 
                    closed=True,
                    facecolor='w',
                    edgecolor='k',
                    lw=1)

    los_vertices5 = [(0.36*escala_x+spa_x,0.40*escala_y+spa_y), (0.38*escala_x+spa_x,0.43*escala_y+spa_y), 
    (0.39*escala_x+spa_x,0.46*escala_y+spa_y), (0.41*escala_x+spa_x,0.51*escala_y+spa_y), 
    (0.41*escala_x+spa_x,0.57*escala_y+spa_y), (0.39*escala_x+spa_x,0.62*escala_y+spa_y),
    (0.40*escala_x+spa_x,0.55*escala_y+spa_y), (0.39*escala_x+spa_x,0.46*escala_y+spa_y),
    (0.37*escala_x+spa_x,0.44*escala_y+spa_y), (0.32*escala_x+spa_x,0.42*escala_y+spa_y), 
    (0.34*escala_x+spa_x,0.45*escala_y+spa_y), (0.35*escala_x+spa_x,0.50*escala_y+spa_y), 
    (0.36*escala_x+spa_x,0.55*escala_y+spa_y), (0.35*escala_x+spa_x,0.62*escala_y+spa_y),
    (0.33*escala_x+spa_x,0.67*escala_y+spa_y), (0.45*escala_x+spa_x,0.67*escala_y+spa_y),
    (0.45*escala_x+spa_x,0.64*escala_y+spa_y), (0.46*escala_x+spa_x,0.66*escala_y+spa_y), 
    (0.46*escala_x+spa_x,0.73*escala_y+spa_y), (0.45*escala_x+spa_x,0.74*escala_y+spa_y), 
    (0.47*escala_x+spa_x,0.76*escala_y+spa_y), (0.52*escala_x+spa_x,0.77*escala_y+spa_y),
    (0.55*escala_x+spa_x,0.78*escala_y+spa_y), (0.57*escala_x+spa_x,0.78*escala_y+spa_y),
    
    (0.56*escala_x+spa_x,0.79*escala_y+spa_y), (0.48*escala_x+spa_x,0.78*escala_y+spa_y), 
    (0.45*escala_x+spa_x,0.75*escala_y+spa_y), (0.42*escala_x+spa_x,0.74*escala_y+spa_y), 
    (0.41*escala_x+spa_x,0.75*escala_y+spa_y), (0.42*escala_x+spa_x,0.76*escala_y+spa_y),
    (0.42*escala_x+spa_x,0.80*escala_y+spa_y), (0.41*escala_x+spa_x,0.81*escala_y+spa_y),
    (0.43*escala_x+spa_x,0.83*escala_y+spa_y), (0.46*escala_x+spa_x,0.84*escala_y+spa_y), 
    (0.50*escala_x+spa_x,0.85*escala_y+spa_y), (0.50*escala_x+spa_x,0.92*escala_y+spa_y), 
    (0.52*escala_x+spa_x,0.92*escala_y+spa_y), (0.52*escala_x+spa_x,0.85*escala_y+spa_y),
    (0.54*escala_x+spa_x,0.84*escala_y+spa_y), (0.56*escala_x+spa_x,0.84*escala_y+spa_y),
    (0.60*escala_x+spa_x,0.80*escala_y+spa_y), (0.60*escala_x+spa_x,0.78*escala_y+spa_y), 
    (0.64*escala_x+spa_x,0.77*escala_y+spa_y), (0.67*escala_x+spa_x,0.74*escala_y+spa_y), 
    (0.68*escala_x+spa_x,0.71*escala_y+spa_y), (0.67*escala_x+spa_x,0.66*escala_y+spa_y),
    (0.66*escala_x+spa_x,0.64*escala_y+spa_y), (0.71*escala_x+spa_x,0.64*escala_y+spa_y),

    (0.71*escala_x+spa_x,0.59*escala_y+spa_y), (0.72*escala_x+spa_x,0.58*escala_y+spa_y), 
    (0.71*escala_x+spa_x,0.51*escala_y+spa_y), (0.68*escala_x+spa_x,0.44*escala_y+spa_y), 
    (0.65*escala_x+spa_x,0.41*escala_y+spa_y), (0.64*escala_x+spa_x,0.43*escala_y+spa_y),
    (0.61*escala_x+spa_x,0.45*escala_y+spa_y), (0.54*escala_x+spa_x,0.45*escala_y+spa_y),
    (0.47*escala_x+spa_x,0.44*escala_y+spa_y), (0.44*escala_x+spa_x,0.43*escala_y+spa_y), 
    (0.41*escala_x+spa_x,0.42*escala_y+spa_y)
    ]
    los5 = ptc.Polygon(los_vertices5, 
                    closed=True,
                    facecolor='w',
                    edgecolor='k',
                    lw=1)
    
    los_vertices6 = [(0.48*escala_x+spa_x,0.64*escala_y+spa_y), 
    (0.51*escala_x+spa_x,0.65*escala_y+spa_y), (0.56*escala_x+spa_x,0.66*escala_y+spa_y), 
    (0.61*escala_x+spa_x,0.66*escala_y+spa_y), (0.63*escala_x+spa_x,0.64*escala_y+spa_y)
    ]
    los6 = ptc.Polygon(los_vertices6, 
                    closed=True,
                    facecolor='k',
                    edgecolor='k',
                    lw=1)
    
    los_vertices7 = [(0.39*escala_x+spa_x,0.62*escala_y+spa_y), 
    (0.39*escala_x+spa_x,0.46*escala_y+spa_y), (0.40*escala_x+spa_x,0.41*escala_y+spa_y), 
    (0.46*escala_x+spa_x,0.36*escala_y+spa_y), (0.58*escala_x+spa_x,0.45*escala_y+spa_y)
    ]
    los7 = ptc.Polygon(los_vertices7, 
                    closed=True,
                    facecolor='k',
                    edgecolor='k',
                    lw=1)


    los_vertices8 = [
    (0.42*escala_x+spa_x,0.83*escala_y+spa_y), (0.41*escala_x+spa_x,0.84*escala_y+spa_y),
    (0.44*escala_x+spa_x,0.87*escala_y+spa_y), (0.47*escala_x+spa_x,0.90*escala_y+spa_y),
    (0.50*escala_x+spa_x,0.90*escala_y+spa_y), (0.50*escala_x+spa_x,0.86*escala_y+spa_y),
    (0.48*escala_x+spa_x,0.86*escala_y+spa_y), (0.43*escala_x+spa_x,0.84*escala_y+spa_y)
    ]
    los8 = ptc.Polygon(los_vertices8, 
                    closed=True,
                    facecolor='w',
                    edgecolor='k',
                    lw=1)

    los_vertices9 = [(0.55*escala_x+spa_x,0.55*escala_y+spa_y), (0.50*escala_x+spa_x,0.52*escala_y+spa_y), (0.50*escala_x+spa_x,0.59*escala_y+spa_y), 
    (0.55*escala_x+spa_x,0.56*escala_y+spa_y), (0.52*escala_x+spa_x,0.61*escala_y+spa_y), (0.59*escala_x+spa_x,0.61*escala_y+spa_y),
    (0.56*escala_x+spa_x,0.56*escala_y+spa_y), (0.61*escala_x+spa_x,0.59*escala_y+spa_y), (0.61*escala_x+spa_x,0.52*escala_y+spa_y),
    (0.56*escala_x+spa_x,0.55*escala_y+spa_y), (0.59*escala_x+spa_x,0.50*escala_y+spa_y), (0.52*escala_x+spa_x,0.50*escala_y+spa_y),
    ]
    los9 = ptc.Polygon(los_vertices9, 
                    closed=True,
                    facecolor='r',
                    edgecolor='k',
                    lw=0)

    los_vertices10 = [
    (0.47*escala_x+spa_x,0.32*escala_y+spa_y), (0.46*escala_x+spa_x,0.33*escala_y+spa_y), 
    (0.49*escala_x+spa_x,0.35*escala_y+spa_y), (0.58*escala_x+spa_x,0.37*escala_y+spa_y), 
    (0.60*escala_x+spa_x,0.35*escala_y+spa_y), (0.60*escala_x+spa_x,0.33*escala_y+spa_y),
    (0.57*escala_x+spa_x,0.32*escala_y+spa_y), (0.56*escala_x+spa_x,0.33*escala_y+spa_y), 
    (0.53*escala_x+spa_x,0.34*escala_y+spa_y), (0.52*escala_x+spa_x,0.33*escala_y+spa_y), 
    ]
    los10 = ptc.Polygon(los_vertices10, 
                    closed=True,
                    facecolor=barco_color,
                    edgecolor='k',
                    lw=1)
    
    los_vertices11 = [
    (0.46*escala_x+spa_x,0.33*escala_y+spa_y), (0.49*escala_x+spa_x,0.35*escala_y+spa_y), 
    (0.58*escala_x+spa_x,0.37*escala_y+spa_y), (0.60*escala_x+spa_x,0.35*escala_y+spa_y), 
    (0.62*escala_x+spa_x,0.39*escala_y+spa_y), (0.61*escala_x+spa_x,0.40*escala_y+spa_y),
    (0.58*escala_x+spa_x,0.40*escala_y+spa_y), (0.49*escala_x+spa_x,0.38*escala_y+spa_y), 
    (0.46*escala_x+spa_x,0.36*escala_y+spa_y), (0.43*escala_x+spa_x,0.34*escala_y+spa_y), 
    ]
    los11 = ptc.Polygon(los_vertices11, 
                    closed=True,
                    facecolor=barco_color,
                    edgecolor='k',
                    lw=1)
    
    los_vertices12 = [
    (0.62*escala_x+spa_x,0.39*escala_y+spa_y), (0.61*escala_x+spa_x,0.40*escala_y+spa_y),
    (0.58*escala_x+spa_x,0.40*escala_y+spa_y), (0.49*escala_x+spa_x,0.38*escala_y+spa_y), 
    (0.46*escala_x+spa_x,0.36*escala_y+spa_y), (0.43*escala_x+spa_x,0.34*escala_y+spa_y), 
    
    (0.41*escala_x+spa_x,0.36*escala_y+spa_y), (0.40*escala_x+spa_x,0.41*escala_y+spa_y),
    (0.42*escala_x+spa_x,0.41*escala_y+spa_y), (0.44*escala_x+spa_x,0.39*escala_y+spa_y), 
    (0.45*escala_x+spa_x,0.39*escala_y+spa_y), (0.49*escala_x+spa_x,0.43*escala_y+spa_y), 
    
    (0.56*escala_x+spa_x,0.45*escala_y+spa_y), (0.60*escala_x+spa_x,0.45*escala_y+spa_y), 
    (0.63*escala_x+spa_x,0.42*escala_y+spa_y)
    ]

    los12 = ptc.Polygon(los_vertices12, 
                    closed=True,
                    facecolor=barco_color,
                    edgecolor='k',
                    lw=1)
    
    los_vertices13 = [
    (0.57*escala_x+spa_x,0.32*escala_y+spa_y), (0.58*escala_x+spa_x,0.43*escala_y+spa_y),
    (0.59*escala_x+spa_x,0.46*escala_y+spa_y),
    (0.64*escala_x+spa_x,0.50*escala_y+spa_y), (0.66*escala_x+spa_x,0.52*escala_y+spa_y), 
    
    (0.67*escala_x+spa_x,0.51*escala_y+spa_y), (0.61*escala_x+spa_x,0.45*escala_y+spa_y),
    (0.61*escala_x+spa_x,0.43*escala_y+spa_y), (0.60*escala_x+spa_x,0.38*escala_y+spa_y), 
    (0.58*escala_x+spa_x,0.34*escala_y+spa_y)
    ]

    los13 = ptc.Polygon(los_vertices13, 
                    closed=True,
                    facecolor=barco_color,
                    edgecolor='k',
                    lw=1)
    
    los_vertices14 = [
    (0.44*escala_x+spa_x,0.39*escala_y+spa_y), (0.42*escala_x+spa_x,0.41*escala_y+spa_y),
    (0.44*escala_x+spa_x,0.42*escala_y+spa_y), (0.46*escala_x+spa_x,0.40*escala_y+spa_y), 
    (0.45*escala_x+spa_x,0.39*escala_y+spa_y)
    ]

    los14 = ptc.Polygon(los_vertices14, 
                    closed=True,
                    facecolor=barco_color,
                    edgecolor='k',
                    lw=1)
    
    los_vertices15 = [
    (0.48*escala_x+spa_x,0.39*escala_y+spa_y), (0.50*escala_x+spa_x,0.41*escala_y+spa_y),
    (0.55*escala_x+spa_x,0.42*escala_y+spa_y), (0.58*escala_x+spa_x,0.43*escala_y+spa_y), 
    (0.55*escala_x+spa_x,0.42*escala_y+spa_y), (0.50*escala_x+spa_x,0.41*escala_y+spa_y)
    ]

    los15 = ptc.Polygon(los_vertices15, 
                    closed=True,
                    facecolor=barco_color,
                    edgecolor='k',
                    lw=1)


    ax.add_patch(los)
    ax.add_patch(los2)
    ax.add_patch(los3)
    ax.add_patch(los7)
    ax.add_patch(los4)
    ax.add_patch(los5)
    ax.add_patch(los6)
    ax.add_patch(los8)
    ax.add_patch(los9)
    ax.add_patch(los10)
    ax.add_patch(los11)
    ax.add_patch(los12)
    ax.add_patch(los13)
    ax.add_patch(los14)
    ax.add_patch(los15)

    mar_vertices = [
    (0.38*escala_x+spa_x,0.27*escala_y+spa_y), (0.36*escala_x+spa_x,0.29*escala_y+spa_y),
    (0.38*escala_x+spa_x,0.28*escala_y+spa_y), (0.42*escala_x+spa_x,0.30*escala_y+spa_y), 
    (0.41*escala_x+spa_x,0.31*escala_y+spa_y), (0.38*escala_x+spa_x,0.30*escala_y+spa_y),
    (0.37*escala_x+spa_x,0.31*escala_y+spa_y), (0.33*escala_x+spa_x,0.30*escala_y+spa_y),
    (0.36*escala_x+spa_x,0.32*escala_y+spa_y), (0.39*escala_x+spa_x,0.31*escala_y+spa_y), 
    (0.43*escala_x+spa_x,0.34*escala_y+spa_y), (0.44*escala_x+spa_x,0.33*escala_y+spa_y),
    (0.46*escala_x+spa_x,0.33*escala_y+spa_y), (0.46*escala_x+spa_x,0.32*escala_y+spa_y),
    (0.41*escala_x+spa_x,0.27*escala_y+spa_y)
    ]

    mar = ptc.Polygon(mar_vertices, 
                    closed=True,
                    facecolor="k",
                    edgecolor='k',
                    lw=1)
    mar_vertices2 = [
    (0.47*escala_x+spa_x,0.29*escala_y+spa_y), (0.45*escala_x+spa_x,0.31*escala_y+spa_y),
    (0.46*escala_x+spa_x,0.32*escala_y+spa_y), (0.51*escala_x+spa_x,0.32*escala_y+spa_y), 
    (0.53*escala_x+spa_x,0.34*escala_y+spa_y), (0.55*escala_x+spa_x,0.32*escala_y+spa_y),
    (0.61*escala_x+spa_x,0.32*escala_y+spa_y), (0.63*escala_x+spa_x,0.30*escala_y+spa_y),
    (0.62*escala_x+spa_x,0.29*escala_y+spa_y), (0.60*escala_x+spa_x,0.30*escala_y+spa_y), 
    (0.58*escala_x+spa_x,0.29*escala_y+spa_y), (0.55*escala_x+spa_x,0.29*escala_y+spa_y),
    (0.53*escala_x+spa_x,0.31*escala_y+spa_y), (0.52*escala_x+spa_x,0.31*escala_y+spa_y),
    (0.50*escala_x+spa_x,0.29*escala_y+spa_y)
    ]

    mar2 = ptc.Polygon(mar_vertices2, 
                    closed=True,
                    facecolor="w",
                    edgecolor='k',
                    lw=1)
    
    mar_vertices3 = [
    (0.42*escala_x+spa_x,0.27*escala_y+spa_y), (0.41*escala_x+spa_x,0.28*escala_y+spa_y),
    (0.44*escala_x+spa_x,0.30*escala_y+spa_y), (0.47*escala_x+spa_x,0.29*escala_y+spa_y), 
    (0.50*escala_x+spa_x,0.28*escala_y+spa_y), (0.49*escala_x+spa_x,0.27*escala_y+spa_y),
    (0.46*escala_x+spa_x,0.27*escala_y+spa_y), (0.44*escala_x+spa_x,0.28*escala_y+spa_y),
    ]

    mar3 = ptc.Polygon(mar_vertices3, 
                    closed=True,
                    facecolor="w",
                    edgecolor='k',
                    lw=1)
    
    mar_vertices4 = [
    (0.53*escala_x+spa_x,0.27*escala_y+spa_y), (0.51*escala_x+spa_x,0.29*escala_y+spa_y),
    (0.52*escala_x+spa_x,0.30*escala_y+spa_y), (0.53*escala_x+spa_x,0.29*escala_y+spa_y), 
    (0.56*escala_x+spa_x,0.28*escala_y+spa_y)
    ]

    mar4 = ptc.Polygon(mar_vertices4, 
                    closed=True,
                    facecolor="w",
                    edgecolor='k',
                    lw=1)
    
    mar_vertices5 = [
    (0.61*escala_x+spa_x,0.27*escala_y+spa_y), (0.59*escala_x+spa_x,0.29*escala_y+spa_y),
    (0.60*escala_x+spa_x,0.30*escala_y+spa_y), (0.62*escala_x+spa_x,0.29*escala_y+spa_y), 
    (0.62*escala_x+spa_x,0.28*escala_y+spa_y), (0.62*escala_x+spa_x,0.27*escala_y+spa_y)
    ]

    mar5 = ptc.Polygon(mar_vertices5, 
                    closed=True,
                    facecolor="w",
                    edgecolor='k',
                    lw=1)


    ax.add_patch(mar)
    ax.add_patch(mar2)
    ax.add_patch(mar3)
    ax.add_patch(mar4)
    ax.add_patch(mar5)



    
    vvv_vertices = [
    (0.43*escala_x+spa_x,0.24*escala_y+spa_y), (0.46*escala_x+spa_x,0.24*escala_y+spa_y),
    (0.50*escala_x+spa_x,0.13*escala_y+spa_y), (0.54*escala_x+spa_x,0.24*escala_y+spa_y), 
    (0.57*escala_x+spa_x,0.24*escala_y+spa_y), (0.50*escala_x+spa_x,0.07*escala_y+spa_y)
    ]

    vvv = ptc.Polygon(vvv_vertices, 
                    closed=True,
                    facecolor="w",
                    edgecolor='k',
                    lw=1)
    
    ggg_vertices = [
    (0.49*escala_x+spa_x,0.09*escala_y+spa_y), (0.47*escala_x+spa_x,0.13*escala_y+spa_y),
    (0.45*escala_x+spa_x,0.15*escala_y+spa_y), (0.46*escala_x+spa_x,0.17*escala_y+spa_y), 
    (0.44*escala_x+spa_x,0.20*escala_y+spa_y), (0.42*escala_x+spa_x,0.16*escala_y+spa_y),
    (0.43*escala_x+spa_x,0.13*escala_y+spa_y), (0.46*escala_x+spa_x,0.10*escala_y+spa_y)
    ]

    ggg = ptc.Polygon(ggg_vertices, 
                    closed=True,
                    facecolor="w",
                    edgecolor='k',
                    lw=1)
    
    ggg_vertices1 = [
    (0.51*escala_x+spa_x,0.09*escala_y+spa_y), (0.56*escala_x+spa_x,0.10*escala_y+spa_y),
    (0.58*escala_x+spa_x,0.12*escala_y+spa_y), (0.58*escala_x+spa_x,0.16*escala_y+spa_y), 
    (0.49*escala_x+spa_x,0.16*escala_y+spa_y), (0.49*escala_x+spa_x,0.13*escala_y+spa_y),
    (0.55*escala_x+spa_x,0.13*escala_y+spa_y), (0.52*escala_x+spa_x,0.11*escala_y+spa_y)
    ]

    ggg1 = ptc.Polygon(ggg_vertices1, 
                    closed=True,
                    facecolor="w",
                    edgecolor='k',
                    lw=1)
    
    ggg_vertices2 = [
    (0.48*escala_x+spa_x,0.19*escala_y+spa_y), (0.53*escala_x+spa_x,0.19*escala_y+spa_y),
    (0.56*escala_x+spa_x,0.17*escala_y+spa_y), (0.58*escala_x+spa_x,0.19*escala_y+spa_y), 
    (0.56*escala_x+spa_x,0.21*escala_y+spa_y), (0.51*escala_x+spa_x,0.22*escala_y+spa_y),
    (0.47*escala_x+spa_x,0.22*escala_y+spa_y)
    ]

    ggg2 = ptc.Polygon(ggg_vertices2, 
                    closed=True,
                    facecolor="w",
                    edgecolor='k',
                    lw=1)

    ax.add_patch(vvv)
    ax.add_patch(ggg)
    ax.add_patch(ggg1)
    ax.add_patch(ggg2)

    rrr_vertices = [
    (0.20*escala_x+spa_x,0.51*escala_y+spa_y), (0.20*escala_x+spa_x,0.53*escala_y+spa_y),
    (0.21*escala_x+spa_x,0.53*escala_y+spa_y), (0.21*escala_x+spa_x,0.67*escala_y+spa_y), 
    (0.20*escala_x+spa_x,0.67*escala_y+spa_y), (0.20*escala_x+spa_x,0.69*escala_y+spa_y),
    (0.27*escala_x+spa_x,0.69*escala_y+spa_y), (0.30*escala_x+spa_x,0.66*escala_y+spa_y),
    
    (0.30*escala_x+spa_x,0.62*escala_y+spa_y), (0.28*escala_x+spa_x,0.60*escala_y+spa_y),
    (0.31*escala_x+spa_x,0.54*escala_y+spa_y), (0.33*escala_x+spa_x,0.53*escala_y+spa_y), 
    (0.33*escala_x+spa_x,0.51*escala_y+spa_y), (0.30*escala_x+spa_x,0.51*escala_y+spa_y),
    (0.28*escala_x+spa_x,0.53*escala_y+spa_y), (0.25*escala_x+spa_x,0.58*escala_y+spa_y),
    
    (0.24*escala_x+spa_x,0.58*escala_y+spa_y), (0.24*escala_x+spa_x,0.53*escala_y+spa_y),
    (0.25*escala_x+spa_x,0.53*escala_y+spa_y), (0.25*escala_x+spa_x,0.51*escala_y+spa_y),
    ]

    rrr = ptc.Polygon(rrr_vertices, 
                    closed=True,
                    facecolor="w",
                    edgecolor='k',
                    lw=1)
    
    ccc_vertices = [
    (0.21*escala_x+spa_x,0.66*escala_y+spa_y), (0.21*escala_x+spa_x,0.62*escala_y+spa_y),
    (0.20*escala_x+spa_x,0.61*escala_y+spa_y), (0.20*escala_x+spa_x,0.60*escala_y+spa_y), 
    (0.23*escala_x+spa_x,0.57*escala_y+spa_y), (0.26*escala_x+spa_x,0.57*escala_y+spa_y),
    (0.27*escala_x+spa_x,0.54*escala_y+spa_y), (0.22*escala_x+spa_x,0.54*escala_y+spa_y), 
    (0.17*escala_x+spa_x,0.59*escala_y+spa_y), (0.17*escala_x+spa_x,0.62*escala_y+spa_y)
    ]

    ccc = ptc.Polygon(ccc_vertices, 
                    closed=True,
                    facecolor="w",
                    edgecolor='k',
                    lw=1)
    
    ccc_vertices2 = [
    (0.24*escala_x+spa_x,0.64*escala_y+spa_y), (0.24*escala_x+spa_x,0.67*escala_y+spa_y),
    (0.30*escala_x+spa_x,0.67*escala_y+spa_y), (0.33*escala_x+spa_x,0.64*escala_y+spa_y), 
    (0.31*escala_x+spa_x,0.62*escala_y+spa_y), (0.29*escala_x+spa_x,0.64*escala_y+spa_y),
    ]

    ccc2 = ptc.Polygon(ccc_vertices2, 
                    closed=True,
                    facecolor="w",
                    edgecolor='k',
                    lw=1)
    
    ccc_vertices3 = [
    (0.30*escala_x+spa_x,0.55*escala_y+spa_y), (0.29*escala_x+spa_x,0.58*escala_y+spa_y),
    (0.31*escala_x+spa_x,0.59*escala_y+spa_y), (0.33*escala_x+spa_x,0.57*escala_y+spa_y), 
    (0.31*escala_x+spa_x,0.55*escala_y+spa_y)]

    ccc3 = ptc.Polygon(ccc_vertices3, 
                    closed=True,
                    facecolor="w",
                    edgecolor='k',
                    lw=1)
    
    rrr_vertices2 = [
    (0.24*escala_x+spa_x,0.61*escala_y+spa_y), (0.24*escala_x+spa_x,0.64*escala_y+spa_y),
    (0.28*escala_x+spa_x,0.64*escala_y+spa_y), (0.26*escala_x+spa_x,0.61*escala_y+spa_y), 
    ]

    rrr2 = ptc.Polygon(rrr_vertices2, 
                    closed=True,
                    facecolor="k",
                    edgecolor='k',
                    lw=1)
    
    ax.add_patch(rrr)
    ax.add_patch(ccc)
    ax.add_patch(ccc2)
    ax.add_patch(ccc3)
    ax.add_patch(rrr2)
    
def atletico_mineiro(ax, escala,  spa_x=0, spa_y=0 ,  neg=False):

    escala_x = escala
    if neg:
        escala_y = -escala
    else:
        escala_y = escala

    # losango
    los_vertices = [(0.50*escala_x+spa_x,0.02*escala_y+spa_y), (0.54*escala_x+spa_x,0.06*escala_y+spa_y),(0.55*escala_x+spa_x,0.06*escala_y+spa_y), 
    (0.63*escala_x+spa_x,0.14*escala_y+spa_y), (0.63*escala_x+spa_x,0.15*escala_y+spa_y), (0.67*escala_x+spa_x,0.19*escala_y+spa_y),
    (0.75*escala_x+spa_x,0.32*escala_y+spa_y), (0.78*escala_x+spa_x,0.42*escala_y+spa_y), (0.79*escala_x+spa_x,0.45*escala_y+spa_y),
    (0.80*escala_x+spa_x,0.52*escala_y+spa_y), (0.80*escala_x+spa_x,0.65*escala_y+spa_y), (0.70*escala_x+spa_x,0.64*escala_y+spa_y),
    (0.67*escala_x+spa_x,0.65*escala_y+spa_y), (0.59*escala_x+spa_x,0.67*escala_y+spa_y), (0.50*escala_x+spa_x,0.74*escala_y+spa_y),

    ((1-0.59)*escala_x+spa_x,0.67*escala_y+spa_y), ((1-0.67)*escala_x+spa_x,0.65*escala_y+spa_y), ((1-0.70)*escala_x+spa_x,0.64*escala_y+spa_y),
    ((1-0.80)*escala_x+spa_x,0.65*escala_y+spa_y), ((1-0.80)*escala_x+spa_x,0.52*escala_y+spa_y), ((1-0.79)*escala_x+spa_x,0.45*escala_y+spa_y),
    ((1-0.78)*escala_x+spa_x,0.42*escala_y+spa_y), ((1-0.75)*escala_x+spa_x,0.32*escala_y+spa_y), ((1-0.67)*escala_x+spa_x,0.19*escala_y+spa_y),
    ((1-0.63)*escala_x+spa_x,0.15*escala_y+spa_y), ((1-0.63)*escala_x+spa_x,0.14*escala_y+spa_y), ((1-0.55)*escala_x+spa_x,0.06*escala_y+spa_y),
    ((1-0.54)*escala_x+spa_x,0.06*escala_y+spa_y),
    ]

    los = ptc.Polygon(los_vertices, 
                    closed=True,
                    facecolor='w',
                    edgecolor='k',
                    lw=3)


    los_vertices2 = [(0.77*escala_x+spa_x,0.49*escala_y+spa_y),
    (0.78*escala_x+spa_x,0.52*escala_y+spa_y), (0.78*escala_x+spa_x,0.63*escala_y+spa_y), 
    (0.70*escala_x+spa_x,0.62*escala_y+spa_y), (0.67*escala_x+spa_x,0.63*escala_y+spa_y), 
    (0.59*escala_x+spa_x,0.65*escala_y+spa_y), (0.50*escala_x+spa_x,0.71*escala_y+spa_y),

    ((1-0.59)*escala_x+spa_x,0.65*escala_y+spa_y), ((1-0.67)*escala_x+spa_x,0.63*escala_y+spa_y), 
    ((1-0.70)*escala_x+spa_x,0.62*escala_y+spa_y), ((0.02+1-0.80)*escala_x+spa_x,0.63*escala_y+spa_y), 
    ((0.02+1-0.80)*escala_x+spa_x,0.52*escala_y+spa_y), ((1-0.77)*escala_x+spa_x,0.49*escala_y+spa_y),

    ]

    los2 = ptc.Polygon(los_vertices2, 
                    closed=True,
                    facecolor='k',
                    edgecolor='k',
                    lw=0)
    
    los_vertices3 = [
    (0.50*escala_x+spa_x,0.05*escala_y+spa_y), (0.53*escala_x+spa_x,0.08*escala_y+spa_y),
    (0.54*escala_x+spa_x,0.08*escala_y+spa_y), (0.54*escala_x+spa_x,0.46*escala_y+spa_y), 
    (0.46*escala_x+spa_x,0.46*escala_y+spa_y), (0.46*escala_x+spa_x,0.08*escala_y+spa_y),
    (0.47*escala_x+spa_x,0.08*escala_y+spa_y)
    ]

    los3 = ptc.Polygon(los_vertices3, 
                    closed=True,
                    facecolor='k',
                    edgecolor='w',
                    lw=0
                    )
    
    los_vertices4 = [
    (0.57*escala_x+spa_x,0.11*escala_y+spa_y), (0.62*escala_x+spa_x,0.16*escala_y+spa_y), 
    (0.62*escala_x+spa_x,0.17*escala_y+spa_y), (0.65*escala_x+spa_x,0.20*escala_y+spa_y),
    (0.65*escala_x+spa_x,0.46*escala_y+spa_y), (0.57*escala_x+spa_x,0.46*escala_y+spa_y)
    ]

    los4 = ptc.Polygon(los_vertices4, 
                    closed=True,
                    facecolor='k',
                    edgecolor='w',
                    lw=0
                    )
    
    los_vertices5 = [
    (0.43*escala_x+spa_x,0.11*escala_y+spa_y), (0.38*escala_x+spa_x,0.16*escala_y+spa_y), 
    (0.38*escala_x+spa_x,0.17*escala_y+spa_y), (0.35*escala_x+spa_x,0.20*escala_y+spa_y),
    (0.35*escala_x+spa_x,0.46*escala_y+spa_y), (0.43*escala_x+spa_x,0.46*escala_y+spa_y)
    ]

    los5 = ptc.Polygon(los_vertices5, 
                    closed=True,
                    facecolor='k',
                    edgecolor='w',
                    lw=0
                    )
    
    los_vertices6 = [
    (0.68*escala_x+spa_x,0.24*escala_y+spa_y),
    (0.73*escala_x+spa_x,0.33*escala_y+spa_y), (0.76*escala_x+spa_x,0.43*escala_y+spa_y), 
    (0.77*escala_x+spa_x,0.46*escala_y+spa_y), (0.68*escala_x+spa_x,0.46*escala_y+spa_y)
    ]

    los6 = ptc.Polygon(los_vertices6, 
                    closed=True,
                    facecolor='k',
                    edgecolor='w',
                    lw=0
                    )
    
    los_vertices7 = [
    (0.32*escala_x+spa_x,0.24*escala_y+spa_y),
    (0.27*escala_x+spa_x,0.33*escala_y+spa_y), (0.24*escala_x+spa_x,0.43*escala_y+spa_y), 
    (0.23*escala_x+spa_x,0.46*escala_y+spa_y), (0.32*escala_x+spa_x,0.46*escala_y+spa_y)
    ]

    los7 = ptc.Polygon(los_vertices7, 
                    closed=True,
                    facecolor='k',
                    edgecolor='w',
                    lw=0
                    )



    ax.add_patch(los)
    ax.add_patch(los2)
    ax.add_patch(los3)
    ax.add_patch(los4)
    ax.add_patch(los5)
    ax.add_patch(los6)
    ax.add_patch(los7)

    letra_vertices = [
    (0.28*escala_x+spa_x,0.58*escala_y+spa_y), (0.31*escala_x+spa_x,0.61*escala_y+spa_y),
    (0.36*escala_x+spa_x,0.61*escala_y+spa_y), (0.38*escala_x+spa_x,0.59*escala_y+spa_y), 
    (0.36*escala_x+spa_x,0.57*escala_y+spa_y), (0.33*escala_x+spa_x,0.58*escala_y+spa_y),
    (0.31*escala_x+spa_x,0.56*escala_y+spa_y), (0.31*escala_x+spa_x,0.55*escala_y+spa_y), 
    (0.33*escala_x+spa_x,0.53*escala_y+spa_y), (0.36*escala_x+spa_x,0.54*escala_y+spa_y),
    (0.38*escala_x+spa_x,0.52*escala_y+spa_y), (0.36*escala_x+spa_x,0.50*escala_y+spa_y), 
    (0.31*escala_x+spa_x,0.50*escala_y+spa_y), (0.28*escala_x+spa_x,0.53*escala_y+spa_y)
    ]

    letra = ptc.Polygon(letra_vertices, 
                    closed=True,
                    facecolor='w',
                    edgecolor='k',
                    lw=1
                    )
    
    letra_vertices2 = [
    (0.60*escala_x+spa_x,0.50*escala_y+spa_y), (0.60*escala_x+spa_x,0.61*escala_y+spa_y),
    (0.65*escala_x+spa_x,0.61*escala_y+spa_y), (0.66*escala_x+spa_x,0.54*escala_y+spa_y), 
    (0.67*escala_x+spa_x,0.61*escala_y+spa_y), (0.72*escala_x+spa_x,0.61*escala_y+spa_y),
    (0.72*escala_x+spa_x,0.50*escala_y+spa_y), (0.69*escala_x+spa_x,0.50*escala_y+spa_y), 
    (0.69*escala_x+spa_x,0.57*escala_y+spa_y), (0.68*escala_x+spa_x,0.50*escala_y+spa_y),
    (0.64*escala_x+spa_x,0.50*escala_y+spa_y), (0.63*escala_x+spa_x,0.57*escala_y+spa_y), 
    (0.63*escala_x+spa_x,0.50*escala_y+spa_y)
    ]

    letra2 = ptc.Polygon(letra_vertices2, 
                    closed=True,
                    facecolor='w',
                    edgecolor='k',
                    lw=1
                    )
    
    letra_vertices3 = [
    (0.44*escala_x+spa_x,0.50*escala_y+spa_y), (0.47*escala_x+spa_x,0.61*escala_y+spa_y),
    (0.51*escala_x+spa_x,0.61*escala_y+spa_y), (0.54*escala_x+spa_x,0.50*escala_y+spa_y), 
    (0.52*escala_x+spa_x,0.50*escala_y+spa_y), (0.50*escala_x+spa_x,0.52*escala_y+spa_y),
    (0.48*escala_x+spa_x,0.52*escala_y+spa_y), (0.46*escala_x+spa_x,0.50*escala_y+spa_y)
    ]

    letra3 = ptc.Polygon(letra_vertices3, 
                    closed=True,
                    facecolor='w',
                    edgecolor='k',
                    lw=1
                    )
    
    letra_vertices4 = [
    (0.48*escala_x+spa_x,0.54*escala_y+spa_y), (0.50*escala_x+spa_x,0.54*escala_y+spa_y),
    (0.49*escala_x+spa_x,0.58*escala_y+spa_y)
    ]

    letra4 = ptc.Polygon(letra_vertices4, 
                    closed=True,
                    facecolor='k',
                    edgecolor='k',
                    lw=0
                    )
    
    ax.add_patch(letra)
    ax.add_patch(letra2)
    ax.add_patch(letra3)
    ax.add_patch(letra4)

    estrela(ax, 18/100*escala, spa_x=0.50*escala_x+spa_x, spa_y=0.90*escala_y+spa_y, facecor ="y")

def ceara(ax, escala,  spa_x=0, spa_y=0 ,  neg=False):

    escala_x = escala
    if neg:
        escala_y = -escala
    else:
        escala_y = escala
    # losango
    los_vertices = [(0.50*escala_x+spa_x,0.02*escala_y+spa_y), (0.81*escala_x+spa_x,0.18*escala_y+spa_y), (0.89*escala_x+spa_x,0.26*escala_y+spa_y), 
    (0.90*escala_x+spa_x,0.29*escala_y+spa_y), (0.91*escala_x+spa_x,0.32*escala_y+spa_y), (0.91*escala_x+spa_x,0.40*escala_y+spa_y),
    (0.87*escala_x+spa_x,0.53*escala_y+spa_y), (0.84*escala_x+spa_x,0.59*escala_y+spa_y), (0.83*escala_x+spa_x,0.65*escala_y+spa_y),
    (0.86*escala_x+spa_x,0.74*escala_y+spa_y), (0.92*escala_x+spa_x,0.81*escala_y+spa_y), (0.83*escala_x+spa_x,0.92*escala_y+spa_y),
    (0.81*escala_x+spa_x,0.91*escala_y+spa_y), (0.74*escala_x+spa_x,0.90*escala_y+spa_y), (0.64*escala_x+spa_x,0.90*escala_y+spa_y),
    (0.56*escala_x+spa_x,0.92*escala_y+spa_y), (0.50*escala_x+spa_x,0.96*escala_y+spa_y),

    ((1-0.56)*escala_x+spa_x,0.92*escala_y+spa_y), ((1-0.64)*escala_x+spa_x,0.90*escala_y+spa_y), ((1-0.74)*escala_x+spa_x,0.90*escala_y+spa_y), 
    ((1-0.81)*escala_x+spa_x,0.91*escala_y+spa_y), ((1-0.83)*escala_x+spa_x,0.92*escala_y+spa_y), ((1-0.92)*escala_x+spa_x,0.81*escala_y+spa_y), 
    ((1-0.86)*escala_x+spa_x,0.74*escala_y+spa_y), ((1-0.83)*escala_x+spa_x,0.65*escala_y+spa_y), ((1-0.84)*escala_x+spa_x,0.59*escala_y+spa_y),
    ((1-0.87)*escala_x+spa_x,0.53*escala_y+spa_y), ((1-0.91)*escala_x+spa_x,0.40*escala_y+spa_y), ((1-0.91)*escala_x+spa_x,0.32*escala_y+spa_y), 
    ((1-0.90)*escala_x+spa_x,0.29*escala_y+spa_y), ((1-0.89)*escala_x+spa_x,0.26*escala_y+spa_y), ((1-0.81)*escala_x+spa_x,0.18*escala_y+spa_y),
    ]

    los = ptc.Polygon(los_vertices, 
                    closed=True,
                    facecolor='w',
                    edgecolor='k',
                    lw=3)


    los_vertices2 = [(0.50*escala_x+spa_x,0.07*escala_y+spa_y), (0.81*escala_x+spa_x,(0.05+0.18)*escala_y+spa_y), 
    (0.84*escala_x+spa_x,0.27*escala_y+spa_y), (0.85*escala_x+spa_x,0.29*escala_y+spa_y), 
    (0.86*escala_x+spa_x,0.32*escala_y+spa_y), (0.86*escala_x+spa_x,0.40*escala_y+spa_y),
    (0.82*escala_x+spa_x,0.53*escala_y+spa_y), (0.79*escala_x+spa_x,0.59*escala_y+spa_y), 
    (0.78*escala_x+spa_x,0.65*escala_y+spa_y), (0.81*escala_x+spa_x,0.74*escala_y+spa_y), 
    (0.81*escala_x+spa_x,0.86*escala_y+spa_y), (0.74*escala_x+spa_x,0.85*escala_y+spa_y), 
    (0.64*escala_x+spa_x,0.85*escala_y+spa_y), (0.56*escala_x+spa_x,0.87*escala_y+spa_y), 
    (0.50*escala_x+spa_x,0.91*escala_y+spa_y),

    ((1-0.56)*escala_x+spa_x,(-0.05+0.92)*escala_y+spa_y), ((1-0.64)*escala_x+spa_x,(-0.05+0.90)*escala_y+spa_y), 
    ((1-0.74)*escala_x+spa_x,(-0.05+0.90)*escala_y+spa_y), ((1-0.81)*escala_x+spa_x,(-0.05+0.91)*escala_y+spa_y), 
    ((1-0.83)*escala_x+spa_x,(-0.05+0.92)*escala_y+spa_y), ((0.05+1-0.92)*escala_x+spa_x,0.81*escala_y+spa_y), 
    ((0.05+1-0.86)*escala_x+spa_x,0.74*escala_y+spa_y), ((0.05+1-0.83)*escala_x+spa_x,0.65*escala_y+spa_y), 
    ((0.05+1-0.84)*escala_x+spa_x,0.59*escala_y+spa_y), ((0.05+1-0.87)*escala_x+spa_x,0.53*escala_y+spa_y), 
    ((0.05+1-0.91)*escala_x+spa_x,0.40*escala_y+spa_y), ((0.05+1-0.91)*escala_x+spa_x,0.32*escala_y+spa_y), 
    ((0.05+1-0.90)*escala_x+spa_x,0.29*escala_y+spa_y), ((0.05+1-0.89)*escala_x+spa_x,0.27*escala_y+spa_y), 
    ((1-0.81)*escala_x+spa_x,(0.05+0.18)*escala_y+spa_y),
    ]

    los2 = ptc.Polygon(los_vertices2, 
                    closed=True,
                    facecolor='k',
                    edgecolor='w',
                    lw=0)

    los_vertices3 = [(0.81*escala_x+spa_x,0.69*escala_y+spa_y), (0.82*escala_x+spa_x,0.86*escala_y+spa_y), 
    (0.16*escala_x+spa_x,0.52*escala_y+spa_y), (0.12*escala_x+spa_x,0.33*escala_y+spa_y),
    ]

    los3 = ptc.Polygon(los_vertices3, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0)

    los_vertices4 = [(0.33*escala_x+spa_x,0.13*escala_y+spa_y), (0.39*escala_x+spa_x,0.12*escala_y+spa_y), 
    (0.39*escala_x+spa_x,0.48*escala_y+spa_y), (0.33*escala_x+spa_x,0.48*escala_y+spa_y),
    ]

    los4 = ptc.Polygon(los_vertices4, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0)


    los_vertices5 = [(0.61*escala_x+spa_x,0.12*escala_y+spa_y), (0.66*escala_x+spa_x,0.13*escala_y+spa_y), 
    (0.66*escala_x+spa_x,0.62*escala_y+spa_y), (0.61*escala_x+spa_x,0.62*escala_y+spa_y),
    ]

    los5 = ptc.Polygon(los_vertices5, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0)


    ax.add_patch(los)
    ax.add_patch(los2)
    ax.add_patch(los3)
    ax.add_patch(los4)
    ax.add_patch(los5)

    letra_vertices = [
    (0.15*escala_x+spa_x,0.47*escala_y+spa_y), (0.17*escala_x+spa_x,0.50*escala_y+spa_y),
    (0.24*escala_x+spa_x,0.54*escala_y+spa_y), 
    (0.26*escala_x+spa_x,0.54*escala_y+spa_y), (0.28*escala_x+spa_x,0.51*escala_y+spa_y),
    (0.26*escala_x+spa_x,0.49*escala_y+spa_y), (0.24*escala_x+spa_x,0.50*escala_y+spa_y), 
    (0.22*escala_x+spa_x,0.49*escala_y+spa_y), (0.20*escala_x+spa_x,0.47*escala_y+spa_y),
    (0.21*escala_x+spa_x,0.44*escala_y+spa_y), (0.26*escala_x+spa_x,0.46*escala_y+spa_y), 
    (0.29*escala_x+spa_x,0.49*escala_y+spa_y), (0.31*escala_x+spa_x,0.45*escala_y+spa_y),
    (0.22*escala_x+spa_x,0.40*escala_y+spa_y), (0.19*escala_x+spa_x,0.40*escala_y+spa_y), 
    ]

    letra = ptc.Polygon(letra_vertices, 
                    closed=True,
                    facecolor='k',
                    edgecolor='w',
                    lw=0)
    
    letra_vertices2 = [
    (0.27*escala_x+spa_x,0.55*escala_y+spa_y), (0.28*escala_x+spa_x,0.56*escala_y+spa_y), 
    (0.37*escala_x+spa_x,0.61*escala_y+spa_y),
    (0.39*escala_x+spa_x,0.58*escala_y+spa_y), (0.32*escala_x+spa_x,0.54*escala_y+spa_y), 
    (0.33*escala_x+spa_x,0.54*escala_y+spa_y), (0.39*escala_x+spa_x,0.57*escala_y+spa_y),
    (0.40*escala_x+spa_x,0.54*escala_y+spa_y), (0.34*escala_x+spa_x,0.51*escala_y+spa_y), 
    (0.34*escala_x+spa_x,0.50*escala_y+spa_y), (0.41*escala_x+spa_x,0.54*escala_y+spa_y),
    (0.42*escala_x+spa_x,0.50*escala_y+spa_y), (0.34*escala_x+spa_x,0.46*escala_y+spa_y), 
    (0.31*escala_x+spa_x,0.47*escala_y+spa_y)
    ]

    letra2 = ptc.Polygon(letra_vertices2, 
                    closed=True,
                    facecolor='k',
                    edgecolor='w',
                    lw=0)
    
    letra_vertices3 = [
    (0.42*escala_x+spa_x,0.63*escala_y+spa_y), (0.47*escala_x+spa_x,0.65*escala_y+spa_y), 
    (0.51*escala_x+spa_x,0.63*escala_y+spa_y), (0.56*escala_x+spa_x,0.59*escala_y+spa_y),
    (0.54*escala_x+spa_x,0.57*escala_y+spa_y), (0.51*escala_x+spa_x,0.58*escala_y+spa_y), 
    (0.47*escala_x+spa_x,0.56*escala_y+spa_y), (0.46*escala_x+spa_x,0.54*escala_y+spa_y),
    (0.43*escala_x+spa_x,0.51*escala_y+spa_y), (0.42*escala_x+spa_x,0.52*escala_y+spa_y), 
    ]

    letra3 = ptc.Polygon(letra_vertices3, 
                    closed=True,
                    facecolor='k',
                    edgecolor='w',
                    lw=0)
    
    letra_vertices4 = [
    (0.46*escala_x+spa_x,0.58*escala_y+spa_y), (0.46*escala_x+spa_x,0.62*escala_y+spa_y), 
    (0.49*escala_x+spa_x,0.60*escala_y+spa_y)
    ]

    letra4 = ptc.Polygon(letra_vertices4, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0)
    
    letra_vertices5 = [
    (0.52*escala_x+spa_x,0.68*escala_y+spa_y), (0.54*escala_x+spa_x,0.70*escala_y+spa_y), 
    (0.63*escala_x+spa_x,0.74*escala_y+spa_y), (0.65*escala_x+spa_x,0.72*escala_y+spa_y),
    (0.66*escala_x+spa_x,0.68*escala_y+spa_y), (0.68*escala_x+spa_x,0.66*escala_y+spa_y), 
    (0.65*escala_x+spa_x,0.63*escala_y+spa_y), (0.64*escala_x+spa_x,0.65*escala_y+spa_y),
    (0.62*escala_x+spa_x,0.65*escala_y+spa_y), (0.59*escala_x+spa_x,0.63*escala_y+spa_y), 
    (0.59*escala_x+spa_x,0.61*escala_y+spa_y), (0.57*escala_x+spa_x,0.59*escala_y+spa_y),
    (0.55*escala_x+spa_x,0.61*escala_y+spa_y), (0.54*escala_x+spa_x,0.63*escala_y+spa_y), 
    (0.55*escala_x+spa_x,0.65*escala_y+spa_y), (0.53*escala_x+spa_x,0.65*escala_y+spa_y),
    ]

    letra5 = ptc.Polygon(letra_vertices5, 
                    closed=True,
                    facecolor='k',
                    edgecolor='w',
                    lw=0)
    
    letra_vertices6 = [
    (0.57*escala_x+spa_x,0.66*escala_y+spa_y), (0.57*escala_x+spa_x,0.68*escala_y+spa_y), 
    (0.61*escala_x+spa_x,0.70*escala_y+spa_y), (0.62*escala_x+spa_x,0.68*escala_y+spa_y)
    ]

    letra6 = ptc.Polygon(letra_vertices6, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0)
    
    letra_vertices7 = [
    (0.68*escala_x+spa_x,0.77*escala_y+spa_y), (0.73*escala_x+spa_x,0.79*escala_y+spa_y), 
    (0.77*escala_x+spa_x,0.77*escala_y+spa_y), (0.82*escala_x+spa_x,0.73*escala_y+spa_y),
    (0.80*escala_x+spa_x,0.71*escala_y+spa_y), (0.77*escala_x+spa_x,0.72*escala_y+spa_y), 
    (0.73*escala_x+spa_x,0.70*escala_y+spa_y), (0.72*escala_x+spa_x,0.68*escala_y+spa_y),
    (0.69*escala_x+spa_x,0.66*escala_y+spa_y), (0.68*escala_x+spa_x,0.67*escala_y+spa_y), 
    ]

    letra7 = ptc.Polygon(letra_vertices7, 
                    closed=True,
                    facecolor='k',
                    edgecolor='w',
                    lw=0)
    
    letra_vertices8 = [
    (0.72*escala_x+spa_x,0.72*escala_y+spa_y), (0.72*escala_x+spa_x,0.76*escala_y+spa_y), 
    (0.75*escala_x+spa_x,0.74*escala_y+spa_y)
    ]

    letra8 = ptc.Polygon(letra_vertices8, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0)
    
    letra_vertices9 = [
    (0.74*escala_x+spa_x,0.79*escala_y+spa_y), (0.74*escala_x+spa_x,0.81*escala_y+spa_y), 
    (0.76*escala_x+spa_x,0.83*escala_y+spa_y), (0.77*escala_x+spa_x,0.82*escala_y+spa_y),
    (0.76*escala_x+spa_x,0.79*escala_y+spa_y), (0.75*escala_x+spa_x,0.78*escala_y+spa_y), 
    ]

    letra9 = ptc.Polygon(letra_vertices9, 
                    closed=True,
                    facecolor='k',
                    edgecolor='w',
                    lw=0)
    
    ax.add_patch(letra)
    ax.add_patch(letra2)
    ax.add_patch(letra3)
    ax.add_patch(letra4)
    ax.add_patch(letra5)
    ax.add_patch(letra6)
    ax.add_patch(letra7)
    ax.add_patch(letra8)
    ax.add_patch(letra9)


    estrela(ax,12/100*escala, spa_x=0.33*escala_x+spa_x, spa_y=0.69*escala_y+spa_y, facecor ="w")

    estrela(ax,10/100*escala, spa_x=0.25*escala_x+spa_x, spa_y=0.76*escala_y+spa_y, facecor ="w")
 
    estrela(ax,10/100*escala, spa_x=0.33*escala_x+spa_x, spa_y=0.81*escala_y+spa_y, facecor ="w")

    estrela(ax,10/100*escala, spa_x=0.45*escala_x+spa_x, spa_y=0.83*escala_y+spa_y, facecor ="w")

    estrela(ax,10/100*escala, spa_x=0.54*escala_x+spa_x, spa_y=0.81*escala_y+spa_y, facecor ="w")

def palmeiras(ax, escala,  spa_x=0, spa_y=0 ,  neg=False):

    escala_x = escala
    if neg:
        escala_y = -escala
    else:
        escala_y = escala

    palmeiras_color = (0/255,100/255,55/255)
    cir = ptc.Circle(xy=(0.5*escala_x+spa_x,0.5*escala_y+spa_y), 
                    radius = 0.5*escala,
                    facecolor='w',
                    edgecolor='w',
                    lw=0)

    cir2 = ptc.Circle(xy=(0.5*escala_x+spa_x,0.5*escala_y+spa_y), 
                    radius = 0.49*escala,
                    facecolor=palmeiras_color,
                    edgecolor='w',
                    lw=0)
    cir3 = ptc.Circle(xy=(0.5*escala_x+spa_x,0.5*escala_y+spa_y), 
                    radius = 0.48*escala,
                    facecolor='w',
                    edgecolor='w',
                    lw=0)

    cir4 = ptc.Circle(xy=(0.5*escala_x+spa_x,0.5*escala_y+spa_y), 
                    radius = 0.47*escala,
                    facecolor=palmeiras_color,
                    edgecolor='w',
                    lw=0)

    cir5 = ptc.Circle(xy=(0.5*escala_x+spa_x,0.66*escala_y+spa_y), 
                    radius = 0.25*escala,
                    facecolor='w',
                    edgecolor='w',
                    lw=0)  

    cir6 = ptc.Circle(xy=(0.5*escala_x+spa_x,0.66*escala_y+spa_y), 
                    radius = 0.24*escala,
                    facecolor=palmeiras_color,
                    edgecolor='w',
                    lw=0)   
    cir7 = ptc.Circle(xy=(0.5*escala_x+spa_x,0.66*escala_y+spa_y), 
                    radius = 0.23*escala,
                    facecolor='w',
                    edgecolor='w',
                    lw=0)              

    ax.add_patch(cir)
    ax.add_patch(cir2)
    ax.add_patch(cir3)
    ax.add_patch(cir4)
    ax.add_patch(cir5)
    ax.add_patch(cir6)
    ax.add_patch(cir7)

    # losango
    los_vertices = [
    (0.50*escala_x+spa_x,0.89*escala_y+spa_y), (0.42*escala_x+spa_x,0.84*escala_y+spa_y),
    (0.41*escala_x+spa_x,0.83*escala_y+spa_y), (0.36*escala_x+spa_x,0.81*escala_y+spa_y), 
    (0.32*escala_x+spa_x,0.80*escala_y+spa_y), (0.32*escala_x+spa_x,0.71*escala_y+spa_y),
    (0.33*escala_x+spa_x,0.68*escala_y+spa_y), (0.34*escala_x+spa_x,0.65*escala_y+spa_y), 
    (0.39*escala_x+spa_x,0.54*escala_y+spa_y), (0.43*escala_x+spa_x,0.50*escala_y+spa_y), 
    (0.43*escala_x+spa_x,0.49*escala_y+spa_y), (0.50*escala_x+spa_x,0.43*escala_y+spa_y),

    (0.57*escala_x+spa_x,0.49*escala_y+spa_y), (0.57*escala_x+spa_x,0.50*escala_y+spa_y),
    (0.61*escala_x+spa_x,0.54*escala_y+spa_y), (0.66*escala_x+spa_x,0.65*escala_y+spa_y),
    (0.67*escala_x+spa_x,0.68*escala_y+spa_y), (0.68*escala_x+spa_x,0.71*escala_y+spa_y),
    (0.68*escala_x+spa_x,0.80*escala_y+spa_y), (0.64*escala_x+spa_x,0.81*escala_y+spa_y), 
    (0.59*escala_x+spa_x,0.83*escala_y+spa_y), (0.58*escala_x+spa_x,0.84*escala_y+spa_y),
    ]

    los = ptc.Polygon(los_vertices, 
                    closed=True,
                    facecolor='w',
                    edgecolor=palmeiras_color,
                    lw=1)
    
    los_vertices2 = [
    (0.50*escala_x+spa_x,0.87*escala_y+spa_y), 

    (0.42*escala_x+spa_x,0.82*escala_y+spa_y),
    (0.41*escala_x+spa_x,0.81*escala_y+spa_y), (0.36*escala_x+spa_x,0.79*escala_y+spa_y), 
    (0.34*escala_x+spa_x,0.78*escala_y+spa_y), (0.34*escala_x+spa_x,0.71*escala_y+spa_y),
    (0.35*escala_x+spa_x,0.68*escala_y+spa_y), (0.36*escala_x+spa_x,0.65*escala_y+spa_y), 
    (0.41*escala_x+spa_x,0.54*escala_y+spa_y), (0.45*escala_x+spa_x,0.50*escala_y+spa_y), 
    (0.45*escala_x+spa_x,0.49*escala_y+spa_y),

    (0.50*escala_x+spa_x,0.45*escala_y+spa_y),

    (0.55*escala_x+spa_x,0.49*escala_y+spa_y), (0.55*escala_x+spa_x,0.50*escala_y+spa_y),
    (0.59*escala_x+spa_x,0.54*escala_y+spa_y), (0.64*escala_x+spa_x,0.65*escala_y+spa_y),
    (0.65*escala_x+spa_x,0.68*escala_y+spa_y), (0.66*escala_x+spa_x,0.71*escala_y+spa_y),
    (0.66*escala_x+spa_x,0.78*escala_y+spa_y), (0.64*escala_x+spa_x,0.79*escala_y+spa_y), 
    (0.59*escala_x+spa_x,0.81*escala_y+spa_y), (0.58*escala_x+spa_x,0.82*escala_y+spa_y),
    ]

    los2 = ptc.Polygon(los_vertices2, 
                    closed=True,
                    facecolor='w',
                    edgecolor=palmeiras_color,
                    lw=1)
    
    linha_vertices = [
    (0.49*escala_x+spa_x,0.46*escala_y+spa_y), (0.51*escala_x+spa_x,0.46*escala_y+spa_y)
    ]

    linha = ptc.Polygon(linha_vertices, 
                    closed=True,
                    facecolor=palmeiras_color,
                    edgecolor=palmeiras_color,
                    lw=1)
    linha_vertices2 = [
    (0.45*escala_x+spa_x,0.49*escala_y+spa_y), (0.54*escala_x+spa_x,0.49*escala_y+spa_y)
    ]

    linha2 = ptc.Polygon(linha_vertices2, 
                    closed=True,
                    facecolor=palmeiras_color,
                    edgecolor=palmeiras_color,
                    lw=1)
    
    linha_vertices3 = [
    (0.43*escala_x+spa_x,0.52*escala_y+spa_y), (0.57*escala_x+spa_x,0.52*escala_y+spa_y)
    ]

    linha3 = ptc.Polygon(linha_vertices3, 
                    closed=True,
                    facecolor=palmeiras_color,
                    edgecolor=palmeiras_color,
                    lw=1)
    
    linha_vertices4 = [
    (0.40*escala_x+spa_x,0.55*escala_y+spa_y), (0.59*escala_x+spa_x,0.55*escala_y+spa_y)
    ]

    linha4 = ptc.Polygon(linha_vertices4, 
                    closed=True,
                    facecolor=palmeiras_color,
                    edgecolor=palmeiras_color,
                    lw=1)
    
    linha_vertices5 = [
    (0.39*escala_x+spa_x,0.58*escala_y+spa_y), (0.605*escala_x+spa_x,0.58*escala_y+spa_y)
    ]

    linha5 = ptc.Polygon(linha_vertices5, 
                    closed=True,
                    facecolor=palmeiras_color,
                    edgecolor=palmeiras_color,
                    lw=1)
    
    linha_vertices6 = [
    (0.38*escala_x+spa_x,0.61*escala_y+spa_y), (0.62*escala_x+spa_x,0.61*escala_y+spa_y)
    ]

    linha6 = ptc.Polygon(linha_vertices6, 
                    closed=True,
                    facecolor=palmeiras_color,
                    edgecolor=palmeiras_color,
                    lw=1)
    
    linha_vertices7 = [
    (0.36*escala_x+spa_x,0.64*escala_y+spa_y), (0.63*escala_x+spa_x,0.64*escala_y+spa_y)
    ]

    linha7 = ptc.Polygon(linha_vertices7, 
                    closed=True,
                    facecolor=palmeiras_color,
                    edgecolor=palmeiras_color,
                    lw=1)
    
    linha_vertices8 = [
    (0.35*escala_x+spa_x,0.67*escala_y+spa_y), (0.64*escala_x+spa_x,0.67*escala_y+spa_y)
    ]

    linha8 = ptc.Polygon(linha_vertices8, 
                    closed=True,
                    facecolor=palmeiras_color,
                    edgecolor=palmeiras_color,
                    lw=1)
    
    linha_vertices9 = [
    (0.34*escala_x+spa_x,0.70*escala_y+spa_y), (0.65*escala_x+spa_x,0.70*escala_y+spa_y),

    ]

    linha9 = ptc.Polygon(linha_vertices9, 
                    closed=True,
                    facecolor=palmeiras_color,
                    edgecolor=palmeiras_color,
                    lw=1)
    
    linha_vertices13 = [
    (0.34*escala_x+spa_x,0.73*escala_y+spa_y), (0.66*escala_x+spa_x,0.73*escala_y+spa_y)
    ]

    linha13 = ptc.Polygon(linha_vertices13, 
                    closed=True,
                    facecolor=palmeiras_color,
                    edgecolor=palmeiras_color,
                    lw=1)
    
    linha_vertices14 = [ 
    (0.34*escala_x+spa_x,0.76*escala_y+spa_y), (0.66*escala_x+spa_x,0.76*escala_y+spa_y)
    ]

    linha14 = ptc.Polygon(linha_vertices14, 
                    closed=True,
                    facecolor=palmeiras_color,
                    edgecolor=palmeiras_color,
                    lw=1)
    

    
    linha_vertices10 = [
    (0.35*escala_x+spa_x,0.79*escala_y+spa_y), (0.65*escala_x+spa_x,0.79*escala_y+spa_y)
    ]

    linha10 = ptc.Polygon(linha_vertices10, 
                    closed=True,
                    facecolor=palmeiras_color,
                    edgecolor=palmeiras_color,
                    lw=1)
    
    linha_vertices11 = [
    (0.41*escala_x+spa_x,0.82*escala_y+spa_y), (0.58*escala_x+spa_x,0.82*escala_y+spa_y)
    ]

    linha11 = ptc.Polygon(linha_vertices11, 
                    closed=True,
                    facecolor=palmeiras_color,
                    edgecolor=palmeiras_color,
                    lw=1)
    
    linha_vertices12 = [
    (0.46*escala_x+spa_x,0.85*escala_y+spa_y), (0.53*escala_x+spa_x,0.85*escala_y+spa_y)
    ]

    linha12 = ptc.Polygon(linha_vertices12, 
                    closed=True,
                    facecolor=palmeiras_color,
                    edgecolor=palmeiras_color,
                    lw=1)
    
    los_vertices3 = [
    (0.50*escala_x+spa_x,0.51*escala_y+spa_y), (0.47*escala_x+spa_x,0.55*escala_y+spa_y),
    (0.47*escala_x+spa_x,0.77*escala_y+spa_y), (0.50*escala_x+spa_x,0.80*escala_y+spa_y), 
    (0.53*escala_x+spa_x,0.80*escala_y+spa_y), (0.55*escala_x+spa_x,0.79*escala_y+spa_y),
    (0.56*escala_x+spa_x,0.76*escala_y+spa_y), (0.56*escala_x+spa_x,0.68*escala_y+spa_y), 
    (0.54*escala_x+spa_x,0.66*escala_y+spa_y), (0.51*escala_x+spa_x,0.66*escala_y+spa_y), 
    (0.50*escala_x+spa_x,0.67*escala_y+spa_y), (0.52*escala_x+spa_x,0.68*escala_y+spa_y),

    (0.52*escala_x+spa_x,0.70*escala_y+spa_y), (0.50*escala_x+spa_x,0.71*escala_y+spa_y),
    (0.48*escala_x+spa_x,0.70*escala_y+spa_y), (0.48*escala_x+spa_x,0.67*escala_y+spa_y),
    (0.51*escala_x+spa_x,0.64*escala_y+spa_y), (0.56*escala_x+spa_x,0.64*escala_y+spa_y),
    (0.59*escala_x+spa_x,0.67*escala_y+spa_y), (0.60*escala_x+spa_x,0.70*escala_y+spa_y), 
    (0.60*escala_x+spa_x,0.76*escala_y+spa_y), (0.58*escala_x+spa_x,0.80*escala_y+spa_y),

    (0.53*escala_x+spa_x,0.83*escala_y+spa_y), (0.48*escala_x+spa_x,0.82*escala_y+spa_y),
    (0.45*escala_x+spa_x,0.79*escala_y+spa_y), (0.43*escala_x+spa_x,0.80*escala_y+spa_y), 
    (0.42*escala_x+spa_x,0.79*escala_y+spa_y), (0.44*escala_x+spa_x,0.77*escala_y+spa_y),
    (0.44*escala_x+spa_x,0.70*escala_y+spa_y), (0.42*escala_x+spa_x,0.68*escala_y+spa_y), 
    (0.44*escala_x+spa_x,0.66*escala_y+spa_y), (0.44*escala_x+spa_x,0.57*escala_y+spa_y), 
    (0.42*escala_x+spa_x,0.55*escala_y+spa_y), (0.45*escala_x+spa_x,0.55*escala_y+spa_y),
    (0.45*escala_x+spa_x,0.53*escala_y+spa_y), (0.47*escala_x+spa_x,0.51*escala_y+spa_y),
    ]

    los3 = ptc.Polygon(los_vertices3, 
                    closed=True,
                    facecolor='w',
                    edgecolor=palmeiras_color,
                    lw=1)
    
    ax.add_patch(los)
    ax.add_patch(los2)

    ax.add_patch(linha)
    ax.add_patch(linha2)
    ax.add_patch(linha3)
    ax.add_patch(linha4)
    ax.add_patch(linha5)
    ax.add_patch(linha6)
    ax.add_patch(linha7)
    ax.add_patch(linha8)
    ax.add_patch(linha9)
    ax.add_patch(linha13)
    ax.add_patch(linha14)
    ax.add_patch(linha10)
    ax.add_patch(linha11)
    ax.add_patch(linha12)
    ax.add_patch(los3)

    letra_vertices = [
    (0.08*escala_x+spa_x,0.49*escala_y+spa_y), (0.08*escala_x+spa_x,0.52*escala_y+spa_y),
    (0.13*escala_x+spa_x,0.53*escala_y+spa_y), (0.16*escala_x+spa_x,0.54*escala_y+spa_y), 
    (0.25*escala_x+spa_x,0.55*escala_y+spa_y), (0.26*escala_x+spa_x,0.49*escala_y+spa_y),
    (0.24*escala_x+spa_x,0.47*escala_y+spa_y), (0.21*escala_x+spa_x,0.46*escala_y+spa_y), 
    (0.19*escala_x+spa_x,0.45*escala_y+spa_y), (0.16*escala_x+spa_x,0.46*escala_y+spa_y), 
    (0.15*escala_x+spa_x,0.48*escala_y+spa_y), (0.13*escala_x+spa_x,0.50*escala_y+spa_y),
    (0.11*escala_x+spa_x,0.50*escala_y+spa_y)
    ]

    letra = ptc.Polygon(letra_vertices, 
                    closed=True,
                    facecolor='w',
                    edgecolor=palmeiras_color,
                    lw=0)
    
    letra_vertices2 = [
    (0.18*escala_x+spa_x,0.49*escala_y+spa_y), (0.18*escala_x+spa_x,0.51*escala_y+spa_y),
    (0.23*escala_x+spa_x,0.52*escala_y+spa_y), (0.22*escala_x+spa_x,0.50*escala_y+spa_y), 
    (0.20*escala_x+spa_x,0.49*escala_y+spa_y)
    ]

    letra2 = ptc.Polygon(letra_vertices2, 
                    closed=True,
                    facecolor=palmeiras_color,
                    edgecolor=palmeiras_color,
                    lw=0)
    
    letra_vertices3 = [
    (0.10*escala_x+spa_x,0.37*escala_y+spa_y), (0.10*escala_x+spa_x,0.40*escala_y+spa_y),
    (0.30*escala_x+spa_x,0.47*escala_y+spa_y), (0.32*escala_x+spa_x,0.45*escala_y+spa_y),  
    (0.16*escala_x+spa_x,0.25*escala_y+spa_y), (0.14*escala_x+spa_x,0.29*escala_y+spa_y), 
    (0.18*escala_x+spa_x,0.33*escala_y+spa_y), (0.17*escala_x+spa_x,0.36*escala_y+spa_y),
    (0.15*escala_x+spa_x,0.38*escala_y+spa_y)
    ]

    letra3 = ptc.Polygon(letra_vertices3, 
                    closed=True,
                    facecolor='w',
                    edgecolor=palmeiras_color,
                    lw=0)
    
    letra_vertices4 = [
    (0.18*escala_x+spa_x,0.23*escala_y+spa_y), (0.18*escala_x+spa_x,0.24*escala_y+spa_y),
    (0.24*escala_x+spa_x,0.30*escala_y+spa_y), (0.25*escala_x+spa_x,0.32*escala_y+spa_y), 
    (0.33*escala_x+spa_x,0.40*escala_y+spa_y), (0.35*escala_x+spa_x,0.43*escala_y+spa_y),
    (0.37*escala_x+spa_x,0.42*escala_y+spa_y), (0.36*escala_x+spa_x,0.40*escala_y+spa_y), 
    (0.23*escala_x+spa_x,0.24*escala_y+spa_y), (0.27*escala_x+spa_x,0.20*escala_y+spa_y), 
    (0.25*escala_x+spa_x,0.17*escala_y+spa_y), (0.24*escala_x+spa_x,0.17*escala_y+spa_y)
    ]

    letra4 = ptc.Polygon(letra_vertices4, 
                    closed=True,
                    facecolor='w',
                    edgecolor=palmeiras_color,
                    lw=0)
    
    letra_vertices5 = [
    (0.27*escala_x+spa_x,0.15*escala_y+spa_y), (0.27*escala_x+spa_x,0.17*escala_y+spa_y),
    (0.39*escala_x+spa_x,0.39*escala_y+spa_y), (0.40*escala_x+spa_x,0.40*escala_y+spa_y), 
    (0.41*escala_x+spa_x,0.40*escala_y+spa_y), (0.42*escala_x+spa_x,0.38*escala_y+spa_y),
    (0.41*escala_x+spa_x,0.36*escala_y+spa_y), (0.41*escala_x+spa_x,0.30*escala_y+spa_y), 
    (0.40*escala_x+spa_x,0.27*escala_y+spa_y), (0.41*escala_x+spa_x,0.26*escala_y+spa_y), 
    (0.42*escala_x+spa_x,0.27*escala_y+spa_y), (0.43*escala_x+spa_x,0.31*escala_y+spa_y),
    (0.44*escala_x+spa_x,0.33*escala_y+spa_y), (0.46*escala_x+spa_x,0.38*escala_y+spa_y),

    (0.48*escala_x+spa_x,0.38*escala_y+spa_y), (0.48*escala_x+spa_x,0.28*escala_y+spa_y),
    (0.47*escala_x+spa_x,0.23*escala_y+spa_y), (0.47*escala_x+spa_x,0.09*escala_y+spa_y), 
    (0.45*escala_x+spa_x,0.08*escala_y+spa_y), (0.42*escala_x+spa_x,0.09*escala_y+spa_y),
    (0.44*escala_x+spa_x,0.24*escala_y+spa_y), (0.42*escala_x+spa_x,0.23*escala_y+spa_y), 
    (0.38*escala_x+spa_x,0.16*escala_y+spa_y), (0.38*escala_x+spa_x,0.26*escala_y+spa_y), 
    (0.37*escala_x+spa_x,0.27*escala_y+spa_y), (0.36*escala_x+spa_x,0.26*escala_y+spa_y),
    (0.35*escala_x+spa_x,0.23*escala_y+spa_y), (0.32*escala_x+spa_x,0.16*escala_y+spa_y),
    (0.31*escala_x+spa_x,0.13*escala_y+spa_y)
    ]

    letra5 = ptc.Polygon(letra_vertices5, 
                    closed=True,
                    facecolor='w',
                    edgecolor=palmeiras_color,
                    lw=0)
    
    letra_vertices6 = [
    (0.50*escala_x+spa_x,0.08*escala_y+spa_y), (0.50*escala_x+spa_x,0.38*escala_y+spa_y),
    (0.52*escala_x+spa_x,0.38*escala_y+spa_y), (0.55*escala_x+spa_x,0.39*escala_y+spa_y), 
    (0.55*escala_x+spa_x,0.37*escala_y+spa_y), (0.52*escala_x+spa_x,0.36*escala_y+spa_y),
    (0.53*escala_x+spa_x,0.28*escala_y+spa_y), (0.58*escala_x+spa_x,0.28*escala_y+spa_y), 
    (0.58*escala_x+spa_x,0.25*escala_y+spa_y), (0.53*escala_x+spa_x,0.25*escala_y+spa_y), 
    (0.54*escala_x+spa_x,0.22*escala_y+spa_y), (0.54*escala_x+spa_x,0.18*escala_y+spa_y), 
    (0.55*escala_x+spa_x,0.13*escala_y+spa_y), (0.62*escala_x+spa_x,0.14*escala_y+spa_y), 
    (0.62*escala_x+spa_x,0.12*escala_y+spa_y), (0.63*escala_x+spa_x,0.10*escala_y+spa_y), 
    (0.61*escala_x+spa_x,0.09*escala_y+spa_y)
    ]

    letra6 = ptc.Polygon(letra_vertices6, 
                    closed=True,
                    facecolor='w',
                    edgecolor=palmeiras_color,
                    lw=0)
    
    letra_vertices7 = [
    (0.19*escala_x+spa_x,0.39*escala_y+spa_y), (0.25*escala_x+spa_x,0.41*escala_y+spa_y),
    (0.21*escala_x+spa_x,0.37*escala_y+spa_y), (0.20*escala_x+spa_x,0.37*escala_y+spa_y)
    ]

    letra7 = ptc.Polygon(letra_vertices7, 
                    closed=True,
                    facecolor=palmeiras_color,
                    edgecolor=palmeiras_color,
                    lw=0)
    
    letra_vertices8 = [
    (0.65*escala_x+spa_x,0.11*escala_y+spa_y), (0.57*escala_x+spa_x,0.39*escala_y+spa_y),
    (0.59*escala_x+spa_x,0.39*escala_y+spa_y), (0.70*escala_x+spa_x,0.13*escala_y+spa_y)
    ]

    letra8 = ptc.Polygon(letra_vertices8, 
                    closed=True,
                    facecolor='w',
                    edgecolor=palmeiras_color,
                    lw=0)
    
    letra_vertices9 = [
    (0.74*escala_x+spa_x,0.15*escala_y+spa_y), (0.72*escala_x+spa_x,0.16*escala_y+spa_y),
    (0.61*escala_x+spa_x,0.39*escala_y+spa_y), (0.61*escala_x+spa_x,0.41*escala_y+spa_y), 
    (0.66*escala_x+spa_x,0.43*escala_y+spa_y), (0.68*escala_x+spa_x,0.41*escala_y+spa_y),
    (0.69*escala_x+spa_x,0.41*escala_y+spa_y), (0.74*escala_x+spa_x,0.36*escala_y+spa_y), 
    (0.75*escala_x+spa_x,0.33*escala_y+spa_y), (0.74*escala_x+spa_x,0.30*escala_y+spa_y), 
    (0.76*escala_x+spa_x,0.30*escala_y+spa_y), (0.84*escala_x+spa_x,0.25*escala_y+spa_y), 
    (0.81*escala_x+spa_x,0.22*escala_y+spa_y), (0.72*escala_x+spa_x,0.29*escala_y+spa_y), 
    (0.71*escala_x+spa_x,0.28*escala_y+spa_y), (0.77*escala_x+spa_x,0.18*escala_y+spa_y)
    ]

    letra9 = ptc.Polygon(letra_vertices9, 
                    closed=True,
                    facecolor='w',
                    edgecolor=palmeiras_color,
                    lw=0)
    
    letra_vertices10 = [
    (0.64*escala_x+spa_x,0.39*escala_y+spa_y), (0.66*escala_x+spa_x,0.39*escala_y+spa_y),
    (0.69*escala_x+spa_x,0.36*escala_y+spa_y), (0.70*escala_x+spa_x,0.32*escala_y+spa_y),
    (0.68*escala_x+spa_x,0.33*escala_y+spa_y), (0.66*escala_x+spa_x,0.36*escala_y+spa_y)
    ]

    letra10 = ptc.Polygon(letra_vertices10, 
                    closed=True,
                    facecolor=palmeiras_color,
                    edgecolor=palmeiras_color,
                    lw=0)
    
    letra_vertices11 = [
    (0.69*escala_x+spa_x,0.45*escala_y+spa_y), (0.70*escala_x+spa_x,0.47*escala_y+spa_y),
    (0.91*escala_x+spa_x,0.40*escala_y+spa_y), (0.90*escala_x+spa_x,0.37*escala_y+spa_y), 
    (0.85*escala_x+spa_x,0.39*escala_y+spa_y), (0.83*escala_x+spa_x,0.34*escala_y+spa_y),
    (0.87*escala_x+spa_x,0.30*escala_y+spa_y), (0.86*escala_x+spa_x,0.28*escala_y+spa_y), 
    (0.84*escala_x+spa_x,0.27*escala_y+spa_y)
    ]

    letra11 = ptc.Polygon(letra_vertices11, 
                    closed=True,
                    facecolor='w',
                    edgecolor=palmeiras_color,
                    lw=0)
    
    letra_vertices12 = [
    (0.76*escala_x+spa_x,0.42*escala_y+spa_y), (0.81*escala_x+spa_x,0.40*escala_y+spa_y),
    (0.80*escala_x+spa_x,0.38*escala_y+spa_y)
    ]

    letra12 = ptc.Polygon(letra_vertices12, 
                    closed=True,
                    facecolor=palmeiras_color,
                    edgecolor=palmeiras_color,
                    lw=0)
    
    letra_vertices13 = [
    (0.74*escala_x+spa_x,0.50*escala_y+spa_y), (0.74*escala_x+spa_x,0.53*escala_y+spa_y),
    (0.76*escala_x+spa_x,0.55*escala_y+spa_y), (0.79*escala_x+spa_x,0.55*escala_y+spa_y), 
    (0.79*escala_x+spa_x,0.53*escala_y+spa_y), (0.76*escala_x+spa_x,0.51*escala_y+spa_y),
    (0.77*escala_x+spa_x,0.50*escala_y+spa_y), (0.81*escala_x+spa_x,0.50*escala_y+spa_y), 
    (0.84*escala_x+spa_x,0.53*escala_y+spa_y), (0.90*escala_x+spa_x,0.53*escala_y+spa_y), 
    (0.92*escala_x+spa_x,0.51*escala_y+spa_y), (0.92*escala_x+spa_x,0.45*escala_y+spa_y), 
    (0.90*escala_x+spa_x,0.43*escala_y+spa_y), (0.86*escala_x+spa_x,0.44*escala_y+spa_y), 
    (0.86*escala_x+spa_x,0.47*escala_y+spa_y), (0.89*escala_x+spa_x,0.46*escala_y+spa_y), 
    (0.89*escala_x+spa_x,0.49*escala_y+spa_y), (0.87*escala_x+spa_x,0.51*escala_y+spa_y), 
    (0.79*escala_x+spa_x,0.47*escala_y+spa_y), (0.76*escala_x+spa_x,0.48*escala_y+spa_y)
    ]

    letra13 = ptc.Polygon(letra_vertices13, 
                    closed=True,
                    facecolor='w',
                    edgecolor=palmeiras_color,
                    lw=0)
    
    ax.add_patch(letra)
    ax.add_patch(letra2)
    ax.add_patch(letra3)
    ax.add_patch(letra4)
    ax.add_patch(letra5)
    ax.add_patch(letra6)
    ax.add_patch(letra7)
    ax.add_patch(letra8)
    ax.add_patch(letra9)
    ax.add_patch(letra10)
    ax.add_patch(letra11)
    ax.add_patch(letra12)
    ax.add_patch(letra13)

    estrela(ax,9/100*escala, spa_x=0.84*escala_x+spa_x, spa_y=0.62*escala_y+spa_y, facecor ="w")

    estrela(ax,7/100*escala, spa_x=0.82*escala_x+spa_x, spa_y=0.70*escala_y+spa_y, facecor ="w")
 
    estrela(ax,5/100*escala, spa_x=0.79*escala_x+spa_x, spa_y=0.77*escala_y+spa_y, facecor ="w")

    estrela(ax,3/100*escala, spa_x=0.75*escala_x+spa_x, spa_y=0.82*escala_y+spa_y, facecor ="w")

    estrela(ax,9/100*escala, spa_x=0.16*escala_x+spa_x, spa_y=0.62*escala_y+spa_y, facecor ="w")

    estrela(ax,7/100*escala, spa_x=0.18*escala_x+spa_x, spa_y=0.70*escala_y+spa_y, facecor ="w")
 
    estrela(ax,5/100*escala, spa_x=0.21*escala_x+spa_x, spa_y=0.77*escala_y+spa_y, facecor ="w")

    estrela(ax,3/100*escala, spa_x=0.25*escala_x+spa_x, spa_y=0.82*escala_y+spa_y, facecor ="w")

def cruzeiro(ax, escala,  spa_x=0, spa_y=0 ,  neg=False):

    escala_x = escala
    if neg:
        escala_y = -escala
    else:
        escala_y = escala

    cruzeiro_color = (47/255,82/255,158/255)
    cir = ptc.Circle(xy=(0.5*escala_x+spa_x,0.5*escala_y+spa_y), 
                    radius = 0.5*escala,
                    facecolor='w',
                    edgecolor='w',
                    lw=0)
    
    cir2 = ptc.Circle(xy=(0.5*escala_x+spa_x,0.5*escala_y+spa_y), 
                    radius = 0.49*escala,
                    facecolor= cruzeiro_color,
                    edgecolor='w',
                    lw=0)
    
    cir3 = ptc.Circle(xy=(0.5*escala_x+spa_x,0.5*escala_y+spa_y), 
                    radius = 0.48*escala,
                    facecolor='w',
                    edgecolor='w',
                    lw=0)
    
    cir4 = ptc.Circle(xy=(0.5*escala_x+spa_x,0.5*escala_y+spa_y), 
                    radius = 0.34*escala,
                    facecolor= cruzeiro_color,
                    edgecolor='w',
                    lw=0)
    ax.add_patch(cir)
    ax.add_patch(cir2)
    ax.add_patch(cir3)
    ax.add_patch(cir4)

    letra_vertices = [
    (0.05*escala_x+spa_x,0.50*escala_y+spa_y), (0.06*escala_x+spa_x,0.57*escala_y+spa_y),
    (0.14*escala_x+spa_x,0.56*escala_y+spa_y), (0.14*escala_x+spa_x,0.50*escala_y+spa_y), 
    (0.12*escala_x+spa_x,0.50*escala_y+spa_y), (0.13*escala_x+spa_x,0.54*escala_y+spa_y),
    (0.11*escala_x+spa_x,0.54*escala_y+spa_y), (0.10*escala_x+spa_x,0.50*escala_y+spa_y), 
    (0.09*escala_x+spa_x,0.50*escala_y+spa_y), (0.09*escala_x+spa_x,0.55*escala_y+spa_y),
    (0.07*escala_x+spa_x,0.55*escala_y+spa_y), (0.07*escala_x+spa_x,0.50*escala_y+spa_y)
    ]

    letra = ptc.Polygon(letra_vertices, 
                    closed=True,
                    facecolor=cruzeiro_color,
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices2 = [
    (0.06*escala_x+spa_x,0.44*escala_y+spa_y), (0.08*escala_x+spa_x,0.46*escala_y+spa_y),
    (0.08*escala_x+spa_x,0.43*escala_y+spa_y), (0.07*escala_x+spa_x,0.42*escala_y+spa_y), 
    (0.09*escala_x+spa_x,0.40*escala_y+spa_y), (0.10*escala_x+spa_x,0.41*escala_y+spa_y),
    (0.10*escala_x+spa_x,0.45*escala_y+spa_y), (0.11*escala_x+spa_x,0.47*escala_y+spa_y), 
    (0.13*escala_x+spa_x,0.46*escala_y+spa_y), (0.15*escala_x+spa_x,0.44*escala_y+spa_y),
    (0.15*escala_x+spa_x,0.41*escala_y+spa_y), (0.13*escala_x+spa_x,0.39*escala_y+spa_y),

    (0.14*escala_x+spa_x,0.43*escala_y+spa_y), (0.13*escala_x+spa_x,0.44*escala_y+spa_y), 
    (0.11*escala_x+spa_x,0.42*escala_y+spa_y), (0.11*escala_x+spa_x,0.39*escala_y+spa_y),
    (0.10*escala_x+spa_x,0.38*escala_y+spa_y), (0.08*escala_x+spa_x,0.38*escala_y+spa_y), 
    (0.06*escala_x+spa_x,0.41*escala_y+spa_y)
    ]

    letra2 = ptc.Polygon(letra_vertices2, 
                    closed=True,
                    facecolor=cruzeiro_color,
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices3 = [
    (0.09*escala_x+spa_x,0.33*escala_y+spa_y), (0.16*escala_x+spa_x,0.37*escala_y+spa_y),
    (0.19*escala_x+spa_x,0.32*escala_y+spa_y), (0.18*escala_x+spa_x,0.29*escala_y+spa_y), 
    (0.14*escala_x+spa_x,0.29*escala_y+spa_y), (0.12*escala_x+spa_x,0.32*escala_y+spa_y),
    (0.10*escala_x+spa_x,0.31*escala_y+spa_y)
    ]

    letra3 = ptc.Polygon(letra_vertices3, 
                    closed=True,
                    facecolor=cruzeiro_color,
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices4 = [
    (0.15*escala_x+spa_x,0.33*escala_y+spa_y), (0.16*escala_x+spa_x,0.32*escala_y+spa_y),
    (0.16*escala_x+spa_x,0.31*escala_y+spa_y), (0.15*escala_x+spa_x,0.32*escala_y+spa_y)
    ]

    letra4 = ptc.Polygon(letra_vertices4, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0
                    )
    
    letra5 = ptc.Circle(xy=(0.21*escala_x+spa_x,0.22*escala_y+spa_y), 
                    radius = 0.05*escala,
                    facecolor= cruzeiro_color,
                    edgecolor='w',
                    lw=0)
    
    letra6 = ptc.Circle(xy=(0.21*escala_x+spa_x,0.22*escala_y+spa_y), 
                    radius = 0.03*escala,
                    facecolor='w',
                    edgecolor='w',
                    lw=0)
    letra_vertices7 = [
    (0.26*escala_x+spa_x,0.12*escala_y+spa_y), (0.30*escala_x+spa_x,0.20*escala_y+spa_y),
    (0.35*escala_x+spa_x,0.17*escala_y+spa_y), (0.36*escala_x+spa_x,0.15*escala_y+spa_y), 
    (0.33*escala_x+spa_x,0.12*escala_y+spa_y), (0.33*escala_x+spa_x,0.10*escala_y+spa_y),
    (0.32*escala_x+spa_x,0.09*escala_y+spa_y), (0.31*escala_x+spa_x,0.10*escala_y+spa_y), 
    (0.31*escala_x+spa_x,0.14*escala_y+spa_y), (0.28*escala_x+spa_x,0.14*escala_y+spa_y), 
    (0.28*escala_x+spa_x,0.12*escala_y+spa_y)
    ]

    letra7 = ptc.Polygon(letra_vertices7, 
                    closed=True,
                    facecolor=cruzeiro_color,
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices8 = [
    (0.31*escala_x+spa_x,0.17*escala_y+spa_y), (0.32*escala_x+spa_x,0.16*escala_y+spa_y),
    (0.32*escala_x+spa_x,0.15*escala_y+spa_y), (0.31*escala_x+spa_x,0.16*escala_y+spa_y)
    ]

    letra8 = ptc.Polygon(letra_vertices8, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices9 = [
    (0.39*escala_x+spa_x,0.14*escala_y+spa_y), (0.39*escala_x+spa_x,0.15*escala_y+spa_y),
    (0.46*escala_x+spa_x,0.14*escala_y+spa_y), (0.46*escala_x+spa_x,0.13*escala_y+spa_y), 
    (0.43*escala_x+spa_x,0.13*escala_y+spa_y), (0.42*escala_x+spa_x,0.07*escala_y+spa_y),
    (0.40*escala_x+spa_x,0.06*escala_y+spa_y), (0.41*escala_x+spa_x,0.13*escala_y+spa_y)
    ]

    letra9 = ptc.Polygon(letra_vertices9, 
                    closed=True,
                    facecolor=cruzeiro_color,
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices10 = [
    (0.49*escala_x+spa_x,0.05*escala_y+spa_y), (0.49*escala_x+spa_x,0.14*escala_y+spa_y),
    (0.56*escala_x+spa_x,0.14*escala_y+spa_y), (0.56*escala_x+spa_x,0.12*escala_y+spa_y), 
    (0.51*escala_x+spa_x,0.12*escala_y+spa_y), (0.51*escala_x+spa_x,0.10*escala_y+spa_y),
    (0.56*escala_x+spa_x,0.10*escala_y+spa_y), (0.56*escala_x+spa_x,0.09*escala_y+spa_y), 
    (0.51*escala_x+spa_x,0.09*escala_y+spa_y), (0.51*escala_x+spa_x,0.07*escala_y+spa_y),
    (0.56*escala_x+spa_x,0.07*escala_y+spa_y), (0.56*escala_x+spa_x,0.05*escala_y+spa_y)
    ]

    letra10 = ptc.Polygon(letra_vertices10, 
                    closed=True,
                    facecolor=cruzeiro_color,
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices11 = [
    (0.65*escala_x+spa_x,0.15*escala_y+spa_y), (0.66*escala_x+spa_x,0.18*escala_y+spa_y),
    (0.70*escala_x+spa_x,0.19*escala_y+spa_y), (0.72*escala_x+spa_x,0.18*escala_y+spa_y), 
    (0.71*escala_x+spa_x,0.17*escala_y+spa_y), (0.69*escala_x+spa_x,0.18*escala_y+spa_y),
    (0.67*escala_x+spa_x,0.15*escala_y+spa_y), (0.68*escala_x+spa_x,0.13*escala_y+spa_y), 
    (0.71*escala_x+spa_x,0.12*escala_y+spa_y), (0.72*escala_x+spa_x,0.14*escala_y+spa_y),
    (0.74*escala_x+spa_x,0.15*escala_y+spa_y), (0.74*escala_x+spa_x,0.13*escala_y+spa_y), 
    (0.71*escala_x+spa_x,0.10*escala_y+spa_y), (0.69*escala_x+spa_x,0.10*escala_y+spa_y),
    (0.66*escala_x+spa_x,0.12*escala_y+spa_y)
    ]

    letra11 = ptc.Polygon(letra_vertices11, 
                    closed=True,
                    facecolor=cruzeiro_color,
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices12 = [
    (0.73*escala_x+spa_x,0.22*escala_y+spa_y), (0.75*escala_x+spa_x,0.24*escala_y+spa_y),
    (0.79*escala_x+spa_x,0.20*escala_y+spa_y), (0.81*escala_x+spa_x,0.22*escala_y+spa_y), 
    (0.83*escala_x+spa_x,0.20*escala_y+spa_y), (0.79*escala_x+spa_x,0.16*escala_y+spa_y)
    ]

    letra12 = ptc.Polygon(letra_vertices12, 
                    closed=True,
                    facecolor=cruzeiro_color,
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices13 = [
    (0.80*escala_x+spa_x,0.29*escala_y+spa_y), (0.81*escala_x+spa_x,0.31*escala_y+spa_y),
    (0.85*escala_x+spa_x,0.28*escala_y+spa_y), (0.88*escala_x+spa_x,0.30*escala_y+spa_y), 
    (0.82*escala_x+spa_x,0.34*escala_y+spa_y), (0.83*escala_x+spa_x,0.36*escala_y+spa_y),
    (0.90*escala_x+spa_x,0.31*escala_y+spa_y), (0.87*escala_x+spa_x,0.26*escala_y+spa_y), 
    (0.84*escala_x+spa_x,0.26*escala_y+spa_y)
    ]

    letra13 = ptc.Polygon(letra_vertices13, 
                    closed=True,
                    facecolor=cruzeiro_color,
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices14 = [
    (0.85*escala_x+spa_x,0.39*escala_y+spa_y), (0.85*escala_x+spa_x,0.43*escala_y+spa_y),
    (0.86*escala_x+spa_x,0.45*escala_y+spa_y), (0.89*escala_x+spa_x,0.45*escala_y+spa_y), 
    (0.90*escala_x+spa_x,0.44*escala_y+spa_y), (0.91*escala_x+spa_x,0.45*escala_y+spa_y),
    (0.93*escala_x+spa_x,0.45*escala_y+spa_y), (0.94*escala_x+spa_x,0.42*escala_y+spa_y), 
    (0.93*escala_x+spa_x,0.37*escala_y+spa_y)
    ]

    letra14 = ptc.Polygon(letra_vertices14, 
                    closed=True,
                    facecolor=cruzeiro_color,
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices15 = [
    (0.87*escala_x+spa_x,0.41*escala_y+spa_y), (0.88*escala_x+spa_x,0.43*escala_y+spa_y),
    (0.88*escala_x+spa_x,0.41*escala_y+spa_y)
    ]

    letra15 = ptc.Polygon(letra_vertices15, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices16 = [
    (0.90*escala_x+spa_x,0.41*escala_y+spa_y), (0.91*escala_x+spa_x,0.42*escala_y+spa_y),
    (0.91*escala_x+spa_x,0.40*escala_y+spa_y)
    ]

    letra16 = ptc.Polygon(letra_vertices16, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices17 = [
    (0.86*escala_x+spa_x,0.49*escala_y+spa_y), (0.86*escala_x+spa_x,0.56*escala_y+spa_y),
    (0.87*escala_x+spa_x,0.56*escala_y+spa_y), (0.87*escala_x+spa_x,0.51*escala_y+spa_y), 
    (0.89*escala_x+spa_x,0.51*escala_y+spa_y), (0.89*escala_x+spa_x,0.56*escala_y+spa_y),
    (0.91*escala_x+spa_x,0.56*escala_y+spa_y), (0.91*escala_x+spa_x,0.52*escala_y+spa_y), 
    (0.93*escala_x+spa_x,0.52*escala_y+spa_y), (0.93*escala_x+spa_x,0.57*escala_y+spa_y),
    (0.94*escala_x+spa_x,0.57*escala_y+spa_y), (0.95*escala_x+spa_x,0.50*escala_y+spa_y)
    ]

    letra17 = ptc.Polygon(letra_vertices17, 
                    closed=True,
                    facecolor=cruzeiro_color,
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices18 = [
    (0.13*escala_x+spa_x,0.75*escala_y+spa_y), (0.15*escala_x+spa_x,0.77*escala_y+spa_y),
    (0.17*escala_x+spa_x,0.77*escala_y+spa_y), (0.17*escala_x+spa_x,0.75*escala_y+spa_y), 
    (0.14*escala_x+spa_x,0.73*escala_y+spa_y), (0.15*escala_x+spa_x,0.71*escala_y+spa_y),
    (0.18*escala_x+spa_x,0.70*escala_y+spa_y), (0.20*escala_x+spa_x,0.72*escala_y+spa_y), 
    (0.19*escala_x+spa_x,0.74*escala_y+spa_y), (0.20*escala_x+spa_x,0.75*escala_y+spa_y),
    (0.21*escala_x+spa_x,0.74*escala_y+spa_y), (0.21*escala_x+spa_x,0.70*escala_y+spa_y), 
    (0.19*escala_x+spa_x,0.68*escala_y+spa_y), (0.15*escala_x+spa_x,0.68*escala_y+spa_y),
    (0.13*escala_x+spa_x,0.70*escala_y+spa_y)
    ]

    letra18 = ptc.Polygon(letra_vertices18, 
                    closed=True,
                    facecolor=cruzeiro_color,
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices19 = [
    (0.25*escala_x+spa_x,0.76*escala_y+spa_y), (0.20*escala_x+spa_x,0.81*escala_y+spa_y),
    (0.20*escala_x+spa_x,0.83*escala_y+spa_y), (0.24*escala_x+spa_x,0.86*escala_y+spa_y), 
    (0.27*escala_x+spa_x,0.85*escala_y+spa_y), (0.27*escala_x+spa_x,0.83*escala_y+spa_y),
    (0.31*escala_x+spa_x,0.81*escala_y+spa_y), (0.29*escala_x+spa_x,0.80*escala_y+spa_y), 
    (0.25*escala_x+spa_x,0.81*escala_y+spa_y), (0.26*escala_x+spa_x,0.78*escala_y+spa_y)
    ]

    letra19 = ptc.Polygon(letra_vertices19, 
                    closed=True,
                    facecolor=cruzeiro_color,
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices20 = [
    (0.23*escala_x+spa_x,0.82*escala_y+spa_y), (0.24*escala_x+spa_x,0.83*escala_y+spa_y),
    (0.25*escala_x+spa_x,0.83*escala_y+spa_y), (0.24*escala_x+spa_x,0.82*escala_y+spa_y)
    ]

    letra20 = ptc.Polygon(letra_vertices20, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices21 = [
    (0.30*escala_x+spa_x,0.90*escala_y+spa_y), (0.32*escala_x+spa_x,0.91*escala_y+spa_y),
    (0.34*escala_x+spa_x,0.85*escala_y+spa_y), (0.38*escala_x+spa_x,0.85*escala_y+spa_y), 
    (0.36*escala_x+spa_x,0.92*escala_y+spa_y), (0.37*escala_x+spa_x,0.93*escala_y+spa_y),
    (0.38*escala_x+spa_x,0.92*escala_y+spa_y), (0.40*escala_x+spa_x,0.86*escala_y+spa_y), 
    (0.39*escala_x+spa_x,0.84*escala_y+spa_y), (0.34*escala_x+spa_x,0.83*escala_y+spa_y)
    ]

    letra21 = ptc.Polygon(letra_vertices21, 
                    closed=True,
                    facecolor=cruzeiro_color,
                    edgecolor='w',
                    lw=0
                    )
    

    letra_vertices22 = [
    (0.43*escala_x+spa_x,0.93*escala_y+spa_y), (0.43*escala_x+spa_x,0.94*escala_y+spa_y),
    (0.50*escala_x+spa_x,0.94*escala_y+spa_y), (0.50*escala_x+spa_x,0.92*escala_y+spa_y), 
    (0.47*escala_x+spa_x,0.89*escala_y+spa_y), (0.47*escala_x+spa_x,0.87*escala_y+spa_y),
    (0.51*escala_x+spa_x,0.87*escala_y+spa_y), (0.51*escala_x+spa_x,0.86*escala_y+spa_y), 
    (0.44*escala_x+spa_x,0.86*escala_y+spa_y), (0.44*escala_x+spa_x,0.88*escala_y+spa_y),
    (0.47*escala_x+spa_x,0.91*escala_y+spa_y), (0.47*escala_x+spa_x,0.93*escala_y+spa_y)
    ]

    letra22 = ptc.Polygon(letra_vertices22, 
                    closed=True,
                    facecolor=cruzeiro_color,
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices23 = [
    (0.54*escala_x+spa_x,0.86*escala_y+spa_y), (0.56*escala_x+spa_x,0.94*escala_y+spa_y),
    (0.63*escala_x+spa_x,0.93*escala_y+spa_y), (0.62*escala_x+spa_x,0.91*escala_y+spa_y), 
    (0.57*escala_x+spa_x,0.92*escala_y+spa_y), (0.57*escala_x+spa_x,0.90*escala_y+spa_y),
    (0.62*escala_x+spa_x,0.89*escala_y+spa_y), (0.61*escala_x+spa_x,0.88*escala_y+spa_y), 
    (0.57*escala_x+spa_x,0.89*escala_y+spa_y), (0.57*escala_x+spa_x,0.87*escala_y+spa_y),
    (0.61*escala_x+spa_x,0.86*escala_y+spa_y), (0.61*escala_x+spa_x,0.85*escala_y+spa_y)
    ]

    letra23 = ptc.Polygon(letra_vertices23, 
                    closed=True,
                    facecolor=cruzeiro_color,
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices24 = [
    (0.64*escala_x+spa_x,0.83*escala_y+spa_y), (0.68*escala_x+spa_x,0.91*escala_y+spa_y),
    (0.70*escala_x+spa_x,0.90*escala_y+spa_y), (0.66*escala_x+spa_x,0.82*escala_y+spa_y)
    ]

    letra24 = ptc.Polygon(letra_vertices24, 
                    closed=True,
                    facecolor=cruzeiro_color,
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices25 = [
    (0.69*escala_x+spa_x,0.81*escala_y+spa_y), (0.73*escala_x+spa_x,0.86*escala_y+spa_y),
    (0.75*escala_x+spa_x,0.87*escala_y+spa_y), (0.79*escala_x+spa_x,0.84*escala_y+spa_y), 
    (0.79*escala_x+spa_x,0.81*escala_y+spa_y), (0.78*escala_x+spa_x,0.80*escala_y+spa_y),
    (0.77*escala_x+spa_x,0.80*escala_y+spa_y), (0.77*escala_x+spa_x,0.78*escala_y+spa_y), 
    (0.75*escala_x+spa_x,0.76*escala_y+spa_y), (0.74*escala_x+spa_x,0.77*escala_y+spa_y),
    (0.75*escala_x+spa_x,0.80*escala_y+spa_y), (0.73*escala_x+spa_x,0.82*escala_y+spa_y), 
    (0.71*escala_x+spa_x,0.79*escala_y+spa_y)
    ]

    letra25 = ptc.Polygon(letra_vertices25, 
                    closed=True,
                    facecolor=cruzeiro_color,
                    edgecolor='w',
                    lw=0
                    )
    
    letra_vertices26 = [
    (0.75*escala_x+spa_x,0.84*escala_y+spa_y), (0.76*escala_x+spa_x,0.83*escala_y+spa_y),
    (0.76*escala_x+spa_x,0.82*escala_y+spa_y), (0.75*escala_x+spa_x,0.83*escala_y+spa_y)
    ]

    letra26 = ptc.Polygon(letra_vertices26, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0
                    )
    
    letra27 = ptc.Circle(xy=(0.83*escala_x+spa_x,0.73*escala_y+spa_y), 
                    radius = 0.05*escala,
                    facecolor= cruzeiro_color,
                    edgecolor='w',
                    lw=0)
    
    letra28 = ptc.Circle(xy=(0.83*escala_x+spa_x,0.73*escala_y+spa_y), 
                    radius = 0.03*escala,
                    facecolor='w',
                    edgecolor='w',
                    lw=0)
    
    ax.add_patch(letra)
    ax.add_patch(letra2)
    ax.add_patch(letra3)
    ax.add_patch(letra4)
    ax.add_patch(letra5)
    ax.add_patch(letra6)
    ax.add_patch(letra7)
    ax.add_patch(letra8)
    ax.add_patch(letra9)
    ax.add_patch(letra10)
    ax.add_patch(letra11)
    ax.add_patch(letra12)
    ax.add_patch(letra13)
    ax.add_patch(letra14)
    ax.add_patch(letra15)
    ax.add_patch(letra16)
    ax.add_patch(letra17)
    ax.add_patch(letra18)
    ax.add_patch(letra19)
    ax.add_patch(letra20)
    ax.add_patch(letra21)
    ax.add_patch(letra22)
    ax.add_patch(letra23)
    ax.add_patch(letra24)
    ax.add_patch(letra25)
    ax.add_patch(letra26)
    ax.add_patch(letra27)
    ax.add_patch(letra28)

    estrela(ax,13/100*escala, spa_x=0.50*escala_x+spa_x, spa_y=0.27*escala_y+spa_y, facecor ="w")

    estrela(ax,13/100*escala, spa_x=0.69*escala_x+spa_x, spa_y=0.55*escala_y+spa_y, facecor ="w")

    estrela(ax,13/100*escala, spa_x=0.50*escala_x+spa_x, spa_y=0.72*escala_y+spa_y, facecor ="w")
 
    estrela(ax,13/100*escala, spa_x=0.31*escala_x+spa_x, spa_y=0.55*escala_y+spa_y, facecor ="w")

    estrela(ax,9/100*escala, spa_x=0.55*escala_x+spa_x, spa_y=0.49*escala_y+spa_y, facecor ="w")

def indefinido(ax, escala,  spa_x=0, spa_y=0 ,  neg=False):

    escala_x = escala
    if neg:
        escala_y = -escala
    else:
        escala_y = escala
    cir = ptc.Circle(xy=(0.5*escala_x+spa_x,0.5*escala_y+spa_y), 
                    radius = 0.5*escala,
                    facecolor= 'w',
                    edgecolor='w',
                    lw=0)
    
    cir2 = ptc.Circle(xy=(0.5*escala_x+spa_x,0.5*escala_y+spa_y), 
                    radius = 0.49*escala,
                    facecolor= 'k',
                    edgecolor='w',
                    lw=0)
    cir3 = ptc.Circle(xy=(0.5*escala_x+spa_x,0.5*escala_y+spa_y), 
                    radius = 0.46*escala,
                    facecolor= 'w',
                    edgecolor='w',
                    lw=0)
    
    cir4 = ptc.Circle(xy=(0.50*escala_x+spa_x,0.70*escala_y+spa_y), 
                    radius = 0.15*escala,
                    facecolor= 'k',
                    edgecolor='w',
                    lw=0)
    
    cir5 = ptc.Circle(xy=(0.50*escala_x+spa_x,0.70*escala_y+spa_y), 
                    radius = 0.06*escala,
                    facecolor= 'w',
                    edgecolor='w',
                    lw=0)
    
    cir6 = ptc.Circle(xy=(0.50*escala_x+spa_x,0.25*escala_y+spa_y), 
                    radius = 0.05*escala,
                    facecolor= 'k',
                    edgecolor='w',
                    lw=0)
    ax.add_patch(cir)
    ax.add_patch(cir2)
    ax.add_patch(cir3)
    ax.add_patch(cir4)
    ax.add_patch(cir5)
    ax.add_patch(cir6)


    ret_vertices = [
    (0.55*escala_x+spa_x,0.69*escala_y+spa_y), (0.49*escala_x+spa_x,0.52*escala_y+spa_y),
    (0.35*escala_x+spa_x,0.52*escala_y+spa_y), (0.35*escala_x+spa_x,0.69*escala_y+spa_y)
    ]

    ret = ptc.Polygon(ret_vertices, 
                    closed=True,
                    facecolor='w',
                    edgecolor='w',
                    lw=0
                    )

    ret_vertices2 = [
    (0.46*escala_x+spa_x,0.35*escala_y+spa_y), (0.54*escala_x+spa_x,0.35*escala_y+spa_y), 
    (0.54*escala_x+spa_x,0.46*escala_y+spa_y), (0.55*escala_x+spa_x,0.55*escala_y+spa_y),
    (0.60*escala_x+spa_x,0.59*escala_y+spa_y), (0.56*escala_x+spa_x,0.67*escala_y+spa_y), 
    (0.49*escala_x+spa_x,0.61*escala_y+spa_y),
    (0.46*escala_x+spa_x,0.55*escala_y+spa_y)
    ]

    ret2 = ptc.Polygon(ret_vertices2, 
                    closed=True,
                    facecolor='k',
                    edgecolor='w',
                    lw=0
                    )
    
    ax.add_patch(ret)
    ax.add_patch(ret2)

    # altura/largura

def escolher(nome, ax, escala,  spa_x=0, spa_y=0 ,  neg=False):
    dic = {'Vasco da Gama':0,
           'Botafogo':1,
           'Ceará':2,
           'Criciúma':3,
           'Atlético Goianiense':4,
           'Cruzeiro':5,
           'Athletico Paranaense':6,
           'Palmeiras':7,
           'Fluminense':8,
           'Goiás':9,
           'Fortaleza':10,
           'Flamengo':11,
           'Atlético Mineiro':12,
           'São Paulo':13,
           }
    
    if nome in dic:
        if dic[nome]>=7:
            if dic[nome]==7:
                return(palmeiras(ax, escala,  spa_x, spa_y ,  neg))
            elif dic[nome]==8:
                return(fluminense(ax, escala,  spa_x, spa_y ,  neg))
            elif dic[nome]==9:
                return(goias(ax, escala,  spa_x, spa_y ,  neg))
            elif dic[nome]==10:
                return(fortaleza(ax, escala,  spa_x, spa_y ,  neg))
            elif dic[nome]==11:
                return(flamengo(ax, escala,  spa_x, spa_y ,  neg))
            elif dic[nome]==12:
                return(atletico_mineiro(ax, escala,  spa_x, spa_y ,  neg))
            else:
                return(sao_paulo(ax, escala,  spa_x, spa_y ,  neg))
            
        else:
            if dic[nome]==0:
                return(vasco(ax, escala,  spa_x, spa_y ,  neg))
            elif dic[nome]==1:
                return(botafogo(ax, escala,  spa_x, spa_y ,  neg))
            elif dic[nome]==2:
                return(ceara(ax, escala,  spa_x, spa_y ,  neg))
            elif dic[nome]==3:
                return(criciuma(ax, escala,  spa_x, spa_y ,  neg))
            elif dic[nome]==4:
                return(atletico_goianiense(ax, escala,  spa_x, spa_y ,  neg))
            elif dic[nome]==5:
                return(cruzeiro(ax, escala,  spa_x, spa_y ,  neg))
            else:
                return(athetico_paranaense(ax, escala,  spa_x, spa_y ,  neg))
    else:
        return(indefinido(ax, escala,  spa_x, spa_y ,  neg))
