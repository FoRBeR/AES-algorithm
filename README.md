# AES-algorithm
This is an implementation of the AES-128 algorithm that encrypts one block of data (16 bytes).
The project consists of 5 scripts.
## Description of the algorithm.
This is a block algorithm, it consists of 4 main functions:
1. `SubBytes()`
2. `ShiftRows()`
3. `MixColumns()`
4. `AddRoundKey()`
### `SubBytes()`
Performs a byte replacement on the s_box table.
Encryption table:
|      |  0   |  1   |  2   |  3   |  4   |  5   | 6    |  7   |  8   |  9   |  A   |  B   |  C   |  D   |  E   |  F   |
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
|  0   | 0x63 | 0x7c | 0x77 | 0x7b | 0xf2 | 0x6b | 0x6f | 0xc5 | 0x30 | 0x01 | 0x67 | 0x2b | 0xfe | 0xd7 | 0xab | 0x76 | 
|  1   | 0xca | 0x82 | 0xc9 | 0x7d | 0xfa | 0x59 | 0x47 | 0xf0 | 0xad | 0xd4 | 0xa2 | 0xaf | 0x9c | 0xa4 | 0x72 | 0xc0 | 
|  2   | 0xb7 | 0xfd | 0x93 | 0x26 | 0x36 | 0x3f | 0xf7 | 0xcc | 0x34 | 0xa5 | 0xe5 | 0xf1 | 0x71 | 0xd8 | 0x31 | 0x15 | 
|  3   | 0x04 | 0xc7 | 0x23 | 0xc3 | 0x18 | 0x96 | 0x05 | 0x9a | 0x07 | 0x12 | 0x80 | 0xe2 | 0xeb | 0x27 | 0xb2 | 0x75 | 
|  4   | 0x09 | 0x83 | 0x2c | 0x1a | 0x1b | 0x6e | 0x5a | 0xa0 | 0x52 | 0x3b | 0xd6 | 0xb3 | 0x29 | 0xe3 | 0x2f | 0x84 | 
|  5   | 0x53 | 0xd1 | 0x00 | 0xed | 0x20 | 0xfc | 0xb1 | 0x5b | 0x6a | 0xcb | 0xbe | 0x39 | 0x4a | 0x4c | 0x58 | 0xcf | 
|  6   | 0xd0 | 0xef | 0xaa | 0xfb | 0x43 | 0x4d | 0x33 | 0x85 | 0x45 | 0xf9 | 0x02 | 0x7f | 0x50 | 0x3c | 0x9f | 0xa8 | 
|  7   | 0x51 | 0xa3 | 0x40 | 0x8f | 0x92 | 0x9d | 0x38 | 0xf5 | 0xbc | 0xb6 | 0xda | 0x21 | 0x10 | 0xff | 0xf3 | 0xd2 | 
|  8   | 0xcd | 0x0c | 0x13 | 0xec | 0x5f | 0x97 | 0x44 | 0x17 | 0xc4 | 0xa7 | 0x7e | 0x3d | 0x64 | 0x5d | 0x19 | 0x73 | 
|  9   | 0x60 | 0x81 | 0x4f | 0xdc | 0x22 | 0x2a | 0x90 | 0x88 | 0x46 | 0xee | 0xb8 | 0x14 | 0xde | 0x5e | 0x0b | 0xdb | 
|  A   | 0xe0 | 0x32 | 0x3a | 0x0a | 0x49 | 0x06 | 0x24 | 0x5c | 0xc2 | 0xd3 | 0xac | 0x62 | 0x91 | 0x95 | 0xe4 | 0x79 | 
|  B   | 0xe7 | 0xc8 | 0x37 | 0x6d | 0x8d | 0xd5 | 0x4e | 0xa9 | 0x6c | 0x56 | 0xf4 | 0xea | 0x65 | 0x7a | 0xae | 0x08 | 
|  C   | 0xba | 0x78 | 0x25 | 0x2e | 0x1c | 0xa6 | 0xb4 | 0xc6 | 0xe8 | 0xdd | 0x74 | 0x1f | 0x4b | 0xbd | 0x8b | 0x8a | 
|  D   | 0x70 | 0x3e | 0xb5 | 0x66 | 0x48 | 0x03 | 0xf6 | 0x0e | 0x61 | 0x35 | 0x57 | 0xb9 | 0x86 | 0xc1 | 0x1d | 0x9e | 
|  E   | 0xe1 | 0xf8 | 0x98 | 0x11 | 0x69 | 0xd9 | 0x8e | 0x94 | 0x9b | 0x1e | 0x87 | 0xe9 | 0xce | 0x55 | 0x28 | 0xdf | 
|  F   | 0x8c | 0xa1 | 0x89 | 0x0d | 0xbf | 0xe6 | 0x42 | 0x68 | 0x41 | 0x99 | 0x2d | 0x0f | 0xb0 | 0x54 | 0xbb | 0x16 |

Decryption table:
|      |  0   |  1   |  2   |  3   |  4   |  5   | 6    |  7   |  8   |  9   |  A   |  B   |  C   |  D   |  E   |  F   |
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
|  0   | 0x52 | 0x09 | 0x6a | 0xd5 | 0x30 | 0x36 | 0xa5 | 0x38 | 0xbf | 0x40 | 0xa3 | 0x9e | 0x81 | 0xf3 | 0xd7 | 0xfb |
|  1   | 0x7c | 0xe3 | 0x39 | 0x82 | 0x9b | 0x2f | 0xff | 0x87 | 0x34 | 0x8e | 0x43 | 0x44 | 0xc4 | 0xde | 0xe9 | 0xcb |
|  2   | 0x54 | 0x7b | 0x94 | 0x32 | 0xa6 | 0xc2 | 0x23 | 0x3d | 0xee | 0x4c | 0x95 | 0x0b | 0x42 | 0xfa | 0xc3 | 0x4e |
|  3   | 0x08 | 0x2e | 0xa1 | 0x66 | 0x28 | 0xd9 | 0x24 | 0xb2 | 0x76 | 0x5b | 0xa2 | 0x49 | 0x6d | 0x8b | 0xd1 | 0x25 |
|  4   | 0x72 | 0xf8 | 0xf6 | 0x64 | 0x86 | 0x68 | 0x98 | 0x16 | 0xd4 | 0xa4 | 0x5c | 0xcc | 0x5d | 0x65 | 0xb6 | 0x92 |
|  5   | 0x6c | 0x70 | 0x48 | 0x50 | 0xfd | 0xed | 0xb9 | 0xda | 0x5e | 0x15 | 0x46 | 0x57 | 0xa7 | 0x8d | 0x9d | 0x84 |
|  6   | 0x90 | 0xd8 | 0xab | 0x00 | 0x8c | 0xbc | 0xd3 | 0x0a | 0xf7 | 0xe4 | 0x58 | 0x05 | 0xb8 | 0xb3 | 0x45 | 0x06 |
|  7   | 0xd0 | 0x2c | 0x1e | 0x8f | 0xca | 0x3f | 0x0f | 0x02 | 0xc1 | 0xaf | 0xbd | 0x03 | 0x01 | 0x13 | 0x8a | 0x6b |
|  8   | 0x3a | 0x91 | 0x11 | 0x41 | 0x4f | 0x67 | 0xdc | 0xea | 0x97 | 0xf2 | 0xcf | 0xce | 0xf0 | 0xb4 | 0xe6 | 0x73 |
|  9   | 0x96 | 0xac | 0x74 | 0x22 | 0xe7 | 0xad | 0x35 | 0x85 | 0xe2 | 0xf9 | 0x37 | 0xe8 | 0x1c | 0x75 | 0xdf | 0x6e |
|  A   | 0x47 | 0xf1 | 0x1a | 0x71 | 0x1d | 0x29 | 0xc5 | 0x89 | 0x6f | 0xb7 | 0x62 | 0x0e | 0xaa | 0x18 | 0xbe | 0x1b |
|  B   | 0xfc | 0x56 | 0x3e | 0x4b | 0xc6 | 0xd2 | 0x79 | 0x20 | 0x9a | 0xdb | 0xc0 | 0xfe | 0x78 | 0xcd | 0x5a | 0xf4 |
|  C   | 0x1f | 0xdd | 0xa8 | 0x33 | 0x88 | 0x07 | 0xc7 | 0x31 | 0xb1 | 0x12 | 0x10 | 0x59 | 0x27 | 0x80 | 0xec | 0x5f |
|  D   | 0x60 | 0x51 | 0x7f | 0xa9 | 0x19 | 0xb5 | 0x4a | 0x0d | 0x2d | 0xe5 | 0x7a | 0x9f | 0x93 | 0xc9 | 0x9c | 0xef |
|  E   | 0xa0 | 0xe0 | 0x3b | 0x4d | 0xae | 0x2a | 0xf5 | 0xb0 | 0xc8 | 0xeb | 0xbb | 0x3c | 0x83 | 0x53 | 0x99 | 0x61 |
|  F   | 0x17 | 0x2b | 0x04 | 0x7e | 0xba | 0x77 | 0xd6 | 0x26 | 0xe1 | 0x69 | 0x14 | 0x63 | 0x55 | 0x21 | 0x0c | 0x7d |

### `ShiftRows()`
This function shifts rows by a number of places equal to the row number in the matrix.

|     |  0  |  1  |  2  |  3  |
|:---:|:---:|:---:|:---:|:---:|
|  0  | A   | B   | C   | D   |
|  1  | A   | B   | C   | D   |
|  2  | A   | B   | C   | D   |
|  3  | A   | B   | C   | D   |

|     |  0  |  1  |  2  |  3  |
|:---:|:---:|:---:|:---:|:---:|
|  0  | A   | B   | C   | D   |
|  1  | B   | C   | D   | A   | 
|  2  | C   | D   | A   | B   |
|  3  | D   | A   | B   | C   |

### `MixColumns()`
This function works with columns, the field GF(2^8) is used.
Each column is multiplied by a matrix.

Encryption matrix
|     |  0  |  1  |  2  |  3  |
|:---:|:---:|:---:|:---:|:---:|
|  0  | 02  |03   |01   |01   |
|  1  |01   |02   |03   |01   |
|  2  |01   |01   |02   |03   |
|  3  |03   |01   |01   |02   |

Decryption matrix
|     |  0  |  1  |  2  |  3  |
|:---:|:---:|:---:|:---:|:---:|
|  0  | 0e  |0b   |0d   |09   |
|  1  |09   |0e   |0b   |0d   |
|  2  |0d   |09   |0e   |0b   |
|  3  |0b   |0d   |09   |0e   |

##### New addition and multiplication rules:

a) Addition in field GF(2^8) is equivalent to XOR operation.

b) Multiplying by {01} does not change what is being multiplied.

c) Multiplication by {02} is performed according to the rule: if the multiplied value is less than {80}, it is shifted to the left by 1 bit. If the value being multiplied is greater than or equal to {80}, it is first shifted left by 1 bit, and then the result of the shift is XORed with the value {1b}. The result may jump beyond the value {ff}, that is, beyond the boundaries of one byte. In this case, you need to return the remainder of dividing the result by {100}.

d) Multiplication by other constants can be expressed in terms of the previous.

##### Transformations:

n*{03} = n*{02} + n*{01}

n*{09} = n*{02}\*{02}\*{02} + n*{01}

n*{0b} = b*{02}\*{02}\*{02} + n*{02} + n*{01}

n*{0d} = n*{02}\*{02}\*{02} + n*{02}\*{02} + n*{01}

n*{0е} = n*{02}\*{02}\*{02} + n*{02}\*{02} + b*{02}

### `AddRoundKey()`
The transformation performs a bitwise XOR of the block and round key columns.

## Description of the key generation algorithm.

Process:
1. The first four words (W0, W1, W2, W3) are derived from the cipher key. The cipher key is represented as an array of 16 bytes (k0 to k15). The first four bytes (k0 to k3) become W0, the next four bytes (k4 to k7) become W1, and so on. In other words, the serial connection (concatenation) of the words in this group copies the cipher key.
2. The rest of the words (Wi), where i = 4 - 43, is obtained as follows:

a. `If (i mod 4) != 0`, then `Wi = W(i-1) XOR W(i-4)`

b. `If (i mod 4) = 0` then `Wi = t XOR W(i-4)`

Where `t` is a temporary word which counts as `SubWord(Rotword(Wi-1)) XOR RCon(i//4)`

`RotWord (rotate word)` is a procedure similar to the ShiftRows transformation, but only applies to one row. The procedure takes a word as an array of four bytes and shifts each byte to the left with a conversion.

`SubWord (substitute word)` is a procedure similar to SubBytes conversion, but only applies to one string. The procedure takes each byte in a word and replaces it with another.

`Round Constants` Each Rcon round constant is a 4-byte value in which the rightmost three bytes are always zero.

## Description of scripts.
### input.py
Stores mutable variables:
+ `count_of_rounds`: this variable indicates the number of encryption rounds
+ `input_key`: tuple of 16 bytes, is the key
+ `input_block`: tuple of 16 bytes, input block
### const.py
Stores constants:
+ `s_box`: table for the `SubBytes()` function, used in encryption
+ `inv_s_box`: the table for the `SubBytes()` function is used in decryption
+ `rcon`: table for generating keys
+ `columns_mat`: table for `MixColumns()`, used in encryption
+ `inv_columns_mat`: the table for `MixColumns()` is used in decryption
### gf.py
The functions in the GF(2^8) field are separated into a separate file.
List:
+ `mul02`: multiply by 02
+ `mul03`: multiply by 03
+ `mul09`: multiply by 09
+ `mul0b`: multiply by 0b
+ `mul0d`: multiply by 0d
+ `mul0e`: multiply by 0e
The transformations used for these functions are given above.
### key_schedule.py
Key generation is separated into this script, the only variable received is `key`, which is the extended key.
### main.py
Main script. Encryption and decryption are broken down into functions for convenience.

Function description:
#### `sub_bytes(block: np.ndarray, inv=False) -> np.ndarray`
This is an implementation of the `SubBytes` function.

Accepts the block as a NumPy 4\*4 matrix and a boolean variable `inv`, which defaults to `False`.

The function works for both encryption and decryption, which is determined by the `inv` argument. When `inv = True`, decryption occurs, encryption occurs by default.

The function uses `s_box` and `inv_s_box` and returns a NumPy array.

#### `shift_rows(block: np.ndarray, inv=False) -> np.ndarray`
This is an implementation of the `ShiftRows` function.

Accepts the block as a NumPy 4\*4 matrix and a boolean variable `inv`, which defaults to `False`.

The function works for both encryption and decryption, which is determined by the `inv` argument. When `inv = True`, decryption occurs, encryption occurs by default.

The function implements shift, returns a NumPy array.

#### `mix_columns(block: np.ndarray, inv=False) -> np.ndarray`
This is the implementation of the `MixColumns` function.

Accepts the block as a NumPy 4\*4 matrix and a boolean variable `inv`, which defaults to `False`.

The function works for both encryption and decryption, which is determined by the `inv` argument. When `inv = True`, decryption occurs, encryption occurs by default.

The function implements multiplication in the field GF(2^8), returns a NumPy array.

#### `add_round_key(block: np.ndarray, round_key: np.ndarray) -> np.ndarray`
This is the implementation of the `AddRoundKey` function.

Takes a block as a NumPy 4\*4 matrix and a round key.

The function is symmetrical for encryption/decryption.

It implements XOR of key and block, returns a NumPy array.

#### `block_encrypt(block: np.ndarray) -> np.ndarray`
Encryption function.

Works in this order:
1) initial round

     a. `AddRoundKey()` *--zero round key*
2) rounds 1 - penultimate

     a. `SubBytes()`
     
     b. `ShiftRows()`
     
     c. `MixColumns()`
     
     d. `AddRoundKey()`
3) last round

     a. `SubBytes()`
     
     b. `ShiftRows()`
     
     c. `AddRoundKey()` *--last round key*

#### `block_decrypt(block: np.ndarray) -> np.ndarray`
Decryption function.

Works in this order:
1) last round

     a. `AddRoundKey()` *--last round key*
2) rounds penultimate - 1

     a. `ShiftRows()`
     
     b. `SubBytes()`
     
     c. `AddRoundKey()`
     
     d. `MixColumns()`
3) 0 round

     a. `ShiftRows()`
     
     b. `SubBytes()`
     
     c. `AddRoundKey()` *--zero round key*
