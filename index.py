import numpy as np
from numpy.random import default_rng as rng
import matplotlib.pyplot as plt


rng = rng(seed=100)


ssp = [1,0]  #state space:1 for heads, 0 for tails
asp = [1,0] #action space:1 bet on heads , 0 bet on tails 


def epoch():
    tr = 0
    for _ in range(100):
        a = rng.choice(asp)
        s = rng.choice(ssp)
        if a == s:
            tr += 1
    return tr

rl = np.array([epoch() for _ in range(250)])

epochs = np.insert(np.arange(1, len(rl)+1), 0, 0)
scores = np.insert(rl, 0, 0)

epochs = np.insert(np.arange(1, len(rl)+1), 0, 0)
scores = np.insert(rl, 0, 0)


fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(epochs, scores, marker='o', linestyle='-', color='blue', markersize=3)
ax.axhline(rl.mean(), color='red', linestyle='--', label=f'Moyenne = {rl.mean():.2f}')


ax.spines['left'].set_position('zero')   
ax.spines['bottom'].set_position('zero') 
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


ax.set_title("Score obtenu à chaque epoch\n(1 epoch = 100 tirages)")
ax.set_xlabel("Numéro de l'epoch",)
ax.set_ylabel("Nombre de réussites sur 1 epoch",)
ax.set_xticks(range(0, len(rl)+1, 25))
ax.set_yticks(range(0, 101, 10))
ax.set_xlim(0, len(rl))
ax.set_ylim(0, 100)
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.legend()
plt.tight_layout()
plt.show()


















