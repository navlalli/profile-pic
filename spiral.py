""" Create spiral in the centre with faded colours """

import numpy as np
import scipy
import matplotlib.pyplot as plt
import colorcet

from skimage.draw import disk

def plot_ppic(ppic, save_name="", save=0):
    """ Plot profile picture """
    # Plot for saving
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


def create_background(save=0):
    """ Create background for profile pic """
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
        fig.savefig("./img/18_3_23.png", dpi=200)
    plt.show()

    return background

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
    rr, cc = disk((730, 730), 40, shape=(N, N))
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
    ppic = create_background(save=0)
    add_moon(ppic)
    # plot_ppic(ppic)
    # add_noise(ppic)
    # log_spiral()
