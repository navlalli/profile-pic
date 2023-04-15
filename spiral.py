""" Create spiral in the centre with faded colours """

import numpy as np
import scipy
import matplotlib.pyplot as plt
import matplotlib as mpl
import colorcet as cc
import skimage.draw as draw 
import PIL 

def plot_ppic(ppic, save_name="", save=0):
    """ Plot profile picture """
    # If 2d array (scalar values)
    if ppic.ndim == 2:
        fig, ax = plt.subplots(constrained_layout=True)
        p = ax.imshow(ppic, cmap='cet_bmw', vmax=1.3)
        ax.invert_yaxis()
        ax.set_aspect('equal')
        if not save:
            fig.colorbar(p, ax=ax)
        if save:
            ax.set_xticks([])
            ax.set_yticks([])
            fig.savefig(f"./img/{save_name}.png", dpi=200)
        plt.show()
    # If 3d array (RGB values)
    elif ppic.ndim == 3:
        fig, ax = plt.subplots(figsize=(5, 5), constrained_layout=True)
        ax.imshow(ppic)
        ax.set_aspect('equal')
        if save:
            ax.set_xticks([])
            ax.set_yticks([])
            fig.savefig(f"./img/{save_name}.png", dpi=200)
        plt.show()


def create_background(save=0):
    """ Create background for profile pic - simple gradient in color """
    background = np.zeros((N, N))
    height = np.linspace(0, 1, N)
    bg_val = 5 * height ** 2 + height
    bg_val /= np.max(bg_val)
    print(f"{np.max(bg_val) = }")
    for i in range(N):
        background[i, :] = bg_val[i]
    
    print(f"{np.max(background) = }")
    print(f"{np.min(background) = }")
    # fig, ax = plt.subplots(constrained_layout=True)
    # p = ax.imshow(background, cmap='cet_bmw', vmax=1.3)
    # ax.invert_yaxis()
    # fig.colorbar(p, ax=ax)
    # # ax.set_xticks([])
    # # ax.set_yticks([])
    # plt.show()

    if save:
        # Plot for saving
        fig, ax = plt.subplots(constrained_layout=True)
        ax.imshow(background, cmap='cet_bmw', vmax=1.3)
        ax.invert_yaxis()
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_aspect('equal')
        fig.savefig("./img/15_4_23.png", dpi=200)
    plt.show()

    return background

def create_background_spiral(ppic, save=0):
    """ Create background with a spiral plotted """
    a = 0
    b = 10
    theta = np.linspace(0, 12*np.pi, 1000)
    r = a + b * theta
    x = 500 + r * np.cos(theta)
    y = 500 + r * np.sin(theta)
    print(f"{np.rint(x).astype(int) = }")
    print(f"{np.rint(y).astype(int) = }")
    # xint = np.rint(x).astype(int)
    # yint = np.rint(y).astype(int)
    # background[yint, xint] = 1.3
    
    # fig, ax = plt.subplots(figsize=(5, 5), constrained_layout=True)
    # p = ax.imshow(ppic, cmap='cet_bmw', vmax=1.3)
    # ax.invert_yaxis()
    # ax.set_aspect('equal')
    # # fig.colorbar(p, ax=ax)
    # ax.plot(x, y, 'w-', lw=3)
    # ax.set_xticks([])
    # ax.set_yticks([])
    # # fig.savefig("./img/background_spiral.jpeg", dpi=200)
    # plt.show()

    three = np.array(PIL.Image.open("./img/background_spiral.jpeg"))
    np.testing.assert_equal(np.shape(ppic), np.shape(three)[:-1])
    print(f"{three = }")
    plot_ppic(three, save_name="ppic_spiral_15_4_23", save=1)
    




def color_creator(cmap_name, N, min=0, max=1, invert=0):
    """ Creates a list of N colors from the colormap cmap """
    cmap = mpl.cm.get_cmap(cmap_name)
    # Part through the colormap, specify min and max to crop colormap
    if invert:
        pa = np.linspace(max, min , N)
    else:
        pa = np.linspace(min, max , N)
    # Creates list of colors from the colormap
    cols = np.zeros((N, 4))
    for i in range(N):
        cols[i] = cmap(pa[i])
    return cols

def add_colored_line(ppic):
    """ Add colored line with colors based on a colormap """
    # Save to jpg so can reopen as an array with three channel color data
    fig, ax = plt.subplots(figsize=(5, 5), constrained_layout=True)
    p = ax.imshow(ppic, cmap='cet_bmw', vmax=1.3)
    ax.invert_yaxis()
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    # fig.savefig("./img/background.jpeg", dpi=200)
    # plt.show()

    # Open jpg as three channel colour data 
    three = np.array(PIL.Image.open("./img/background.jpeg"))
    np.testing.assert_equal(np.shape(ppic), np.shape(three)[:-1])
    # Get coordinates of line 

    rr, cc = draw.line(150, 850, 850, 150)  
    rr1, cc1 = draw.line(150+1, 850, 850+1, 150)  
    rr2, cc2 = draw.line(150+2, 850, 850+2, 150)  
    # rr, cc = draw.rectangle((500, 500), (120, 120))  
    print(f"{np.shape(rr) = }")
    print(f"{np.shape(cc) = }")
    cols = color_creator("cet_rainbow", len(rr))
    for i in range(len(rr)):
        draw.set_color(three, (rr[i], cc[i]), cols[i,:-1]*255)
        draw.set_color(three, (rr1[i], cc1[i]), cols[i][:-1]*255)
        draw.set_color(three, (rr2[i], cc2[i]), cols[i][:-1]*255)

    # plot_ppic(three, save_name="ppic_multiline_13_4_23", save=0)
    

def plot_spiral():
    """ Plot logarithmic spiral """
    # a = 10
    # k = 0.5
    a = 0
    b = 8
    theta = np.linspace(0, 10*np.pi, 1000)
    r = a + b * theta
    x = 500 + r * np.cos(theta)
    y = 500 + r * np.sin(theta)
    # phi = np.linspace(0, 2*np.pi, 100)
    # x = a * np.exp(k * phi) * np.cos(phi)
    # y = a * np.exp(k * phi) * np.sin(phi)
    fig, ax = plt.subplots(constrained_layout=True)
    ax.plot(x, y, 'k-', lw=5)
    plt.show()



def add_noise(ppic):
    """ Add noise """
    np.random.seed(8)
    frac_height = 0.25
    n_height = round(frac_height * N)
    rand_arr = 1.2 * np.random.rand(n_height, N) - 0.6
    print(f"{np.min(rand_arr) = }")
    print(f"{np.max(rand_arr) = }")
    pixel_start = 10
    ppic[pixel_start:pixel_start+n_height, :] += rand_arr
    smoothed_ppic = scipy.ndimage.gaussian_filter(ppic, sigma=3, mode='nearest')
    plot_ppic(smoothed_ppic)
    
def add_moon(ppic):
    """ Add moon-like object """
    rr, cc = draw.disk((730, 730), 40, shape=(N, N))
    ppic[rr, cc] = 1.22
    smoothed_ppic = scipy.ndimage.gaussian_filter(ppic, sigma=3, mode='nearest')
    plot_ppic(smoothed_ppic, save_name="ppic_moon_25_3_23", save=0)




def log_spiral():
    k = 5
    a = 1
    phi = np.linspace(0, 1, 100)
    r = a * np.exp(k * phi)
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    fig, ax = plt.subplots(constrained_layout=True)
    ax.plot(x, y, 'k-')
    # ax.set_xlabel("", fontsize=12)
    # ax.set_ylabel("", fontsize=12)
    # ax.legend(loc="best")
    plt.show()

def plot_background(bg):

    fig, ax = plt.subplots(constrained_layout=True)
    p = ax.imshow(bg, cmap='gray')
    fig.colorbar(p, ax=ax)
    ax.set_xlabel("", fontsize=12)
    ax.set_ylabel("", fontsize=12)
    # ax.legend(loc="best")
    plt.show()

if __name__ == "__main__":
    N = 1000  # Size length of square (pixels)
        
    # col_arr = np.zeros((N, N))
    # col_arr[0, :] = y
    # y = np.linspace(0, 999, N, dtype=np.int)
    # ysq = 1.2 * y **2 - 0.2 * y + 1
    # background[:, y] = ysq
    # print(f"{background = }")

    # With moon
    # ppic = create_background(save=0)
    # add_moon(ppic)

    # With colored line
    # ppic = create_background(save=0)
    # add_colored_line(ppic)
    
    # Plot spiral
    # plot_spiral()

    # With Archimedean spiral
    ppic = create_background(save=0)
    create_background_spiral(ppic)


    # plot_ppic(ppic)
    # add_noise(ppic)
    # log_spiral()
