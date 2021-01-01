import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

fig = plt.figure()

r = 2.6
x = 0.4
Itrations  = 20
iii = []

Range = 0
Data = []
imgs = []

while Range != Itrations:

    x = r*x*(1-x)
   
    Data.append(x)
    y = np.array(Data)
    iii = plt.plot(y, 'o-', ms = 5, mfc = 'r', animated = True) 
    
    #img = plt.imshow(iii, animated = True)
    imgs.append([iii])
    Range += 1

Gif = ani.ArtistAnimation(fig,imgs, interval=50, blit=True,
                                repeat_delay=1000 )

plt.show()