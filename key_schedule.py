from input import input_key
from const import rcon, s_box
import numpy as np

np.set_printoptions(formatter={'int': hex})

# Первые 16 байт начальные
key = np.copy(input_key)

# Генерация остальных
for i in range(4, 44):
    if i % 4 != 0:
        w = key[i - 1] ^ key[i - 4]
    # Генерация первой строки ключа раунда
    else:
        t = np.roll(key[i - 1], -1)  # RotWord
        for j in range(4):  # SubWord
            t[j] = s_box[t[j]]
        t = t ^ rcon[i // 4 - 1]  # получили temporary word
        w = t ^ key[i - 4]
    key = np.vstack([key, w])
