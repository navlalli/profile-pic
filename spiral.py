""" Create spiral in the centre with faded colours """

import numpy as np
import matplotlib.pyplot as plt
import colorcet

def create_background(save=0):
    """ Create background for profile pic """
    N = 1000
    background = np.zeros((N, N))
    height = np.linspace(0, 1, N)
    bg_val = 5 * height ** 2 + height
    bg_val /= np.max(bg_val)
    print(f"{np.max(bg_val) = }")
    for i in range(N):
        background[i, :] = bg_val[i]
    
    print(f"{np.max(background) = }")
    print(f"{np.min(background) = }")
    fig, ax = plt.subplots(constrained_layout=True)
    p = ax.imshow(background, cmap='cet_bmw', vmax=1.3)
    ax.invert_yaxis()
    fig.colorbar(p, ax=ax)
    # ax.set_xticks([])
    # ax.set_yticks([])
    plt.show()

    # Plot for saving
    fig, ax = plt.subplots(constrained_layout=True)
    ax.imshow(background, cmap='cet_bmw', vmax=1.3)
    ax.invert_yaxis()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    if save:
        fig.savefig("./img/18_3_23.png", dpi=200)
    plt.show()


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
        
    # col_arr = np.zeros((N, N))
    # col_arr[0, :] = y
    # y = np.linspace(0, 999, N, dtype=np.int)
    # ysq = 1.2 * y **2 - 0.2 * y + 1
    # background[:, y] = ysq
    # print(f"{background = }")
    create_background(save=1)
    # log_spiral()
