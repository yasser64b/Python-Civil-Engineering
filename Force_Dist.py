import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

# Defining the Structure Properties 

# H=np.array(input('input a list of story heights from 1st floor to to end [18,10,10,10,10, ...]='))
Floors=np.arange(1,31)
H=[18, 10, 10, 10, 10, 10, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 10,10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
h=np.cumsum(H)
W=np.array(30*[961])
Cv=0.1
k=2 # Assuming T>2 sec
#12.8.3 Vertical Distribution of Seismic Forces Per ASCE 7-16 
w_h_k=np.sum(W*(h**k)) # Sigm(wi*hi^k)
C_vx=np.array([(W[i]*(h[i]**k))/w_h_k for i in range(len(W))])
# Force distribution 
F_x=C_vx*Cv
#  Shear 
Shear=np.cumsum(F_x[::-1])[::-1]
Shear_load= Shear*W.sum()

# Plot the results
fig, ax=plt.subplots(nrows=1, ncols=2, figsize=(10,15))
ax[0].barh(Floors, F_x, label='Force',height=0.8 , color='r', tick_label=Floors)
ax[1].barh(Floors, Shear, label='Shear',height=0.8 , color='b', tick_label=Floors, )
ax[0].legend(loc='upper right')
ax[1].legend()
ax[0].set_ylabel('Floor')
ax[0].set_xlabel('Force (W)')
ax[1].set_xlabel('Shear (W)')
ax[0].set_ylim([0,31])
ax[1].set_ylim([0,31])
ax[0].set_xlim([0,0.03])
ax[1].set_xlim([0,0.15])

ax[0].set_title('Distributed Force (W)')
ax[1].set_title('Distributed Shear (W)')

for i in range(0,2): 
    rects = ax[i].patches
    for rect in rects:
        # Get X and Y placement of label from rect.
        x_value = rect.get_width()
        y_value = rect.get_y() + rect.get_height() / 2

        # Number of points between bar and label. Change to your liking.
        space = 1
        # Vertical alignment for positive values
        ha = 'left'

        # If value of bar is negative: Place label left of bar
        if x_value < 0:
            # Invert space to place label to the left
            space *= -1
            # Horizontally align label at right
            ha = 'right'

        # Use X value as label and format number with one decimal place
        label = "{:.3f}".format(x_value)
    # Create annotation
        ax[i].annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(space, 0),          # Horizontally shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            va='center',                # Vertically center label
            ha=ha)                      # Horizontally align label differently for
                                        # positive and negative values.

plt.show()
# plt.savefig('Force_Shear Dist.png', dpi=300, bbox_inches='tight')







