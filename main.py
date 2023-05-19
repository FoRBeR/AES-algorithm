import numpy as np
from gf import *
from input import input_block, count_of_rounds
from key_schedule import key
from const import s_box, columns_mat, inv_s_box, inv_columns_mat

np.set_printoptions(formatter={'int': hex})


def sub_bytes(block: np.ndarray, inv=False) -> np.ndarray:
    new_block = np.copy(block)
    for i in range(4):
        for j in range(4):
            if inv:
                new_block[i, j] = inv_s_box[block[i, j]]
            else:
                new_block[i, j] = s_box[block[i, j]]
    return new_block


def shift_rows(block: np.ndarray, inv=False) -> np.ndarray:
    new_block = np.copy(block)
    for i in range(1, 4):
        if inv:
            new_block[i] = np.roll(block[i], i)
        else:
            new_block[i] = np.roll(block[i], -i)
    return new_block


def mix_columns(block: np.ndarray, inv=False) -> np.ndarray:
    new_block = np.copy(block)
    for i in range(4):
        if not inv:
            new_block[0, i] = mul02(block[0, i]) ^ mul03(block[1, i]) ^ block[2, i] ^ block[3, i]
            new_block[1, i] = block[0, i] ^ mul02(block[1, i]) ^ mul03(block[2, i]) ^ block[3, i]
            new_block[2, i] = block[0, i] ^ block[1, i] ^ mul02(block[2, i]) ^ mul03(block[3, i])
            new_block[3, i] = mul03(block[0, i]) ^ block[1, i] ^ block[2, i] ^ mul02(block[3, i])
        else:
            new_block[0, i] = mul0e(block[0, i]) ^ mul0b(block[1, i]) ^ mul0d(block[2, i]) ^ mul09(block[3, i])
            new_block[1, i] = mul09(block[0, i]) ^ mul0e(block[1, i]) ^ mul0b(block[2, i]) ^ mul0d(block[3, i])
            new_block[2, i] = mul0d(block[0, i]) ^ mul09(block[1, i]) ^ mul0e(block[2, i]) ^ mul0b(block[3, i])
            new_block[3, i] = mul0b(block[0, i]) ^ mul0d(block[1, i]) ^ mul09(block[2, i]) ^ mul0e(block[3, i])

    return new_block


def add_round_key(block: np.ndarray, round_key: np.ndarray) -> np.ndarray:
    new_block = block[:, [0]] ^ round_key[:, [0]]
    for i in range(1, 4):
        new_column = block[:, [i]] ^ round_key[:, [i]]
        new_block = np.hstack([new_block, new_column])
    return new_block


def block_encrypt(block: np.ndarray) -> np.ndarray:
    # INITIAL ROUND
    block = add_round_key(block, key[0:4].T)
    # ROUNDS 1 - PENULTIMATE
    for round_num in range(1, count_of_rounds):
        block = sub_bytes(block)
        block = shift_rows(block)
        block = mix_columns(block)
        block = add_round_key(block, key[4 * round_num:4 * round_num + 4].T)
    # LAST ROUND
    block = sub_bytes(block)
    block = shift_rows(block)
    block = add_round_key(block, key[40:44].T)
    return block


def block_decrypt(block: np.ndarray) -> np.ndarray:
    # LAST ROUND
    block = add_round_key(block, key[40:44].T)
    # ROUNDS PENULTIMATE - 1
    for round_num in range(count_of_rounds - 1, 0, -1):
        block = shift_rows(block, True)
        block = sub_bytes(block, True)
        block = add_round_key(block, key[4 * round_num:4 * round_num + 4].T)
        block = mix_columns(block, True)
    # 0 ROUND
    block = shift_rows(block, True)
    block = sub_bytes(block, True)
    block = add_round_key(block, key[0:4].T)
    return block


if __name__ == '__main__':
    print(input_block, end='\n\n')
    print(block_encrypt(input_block), end='\n\n')
    print(block_decrypt(block_encrypt(input_block)), end='\n\n')
