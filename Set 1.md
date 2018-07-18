# Set 1

### Challenge 1: Convert hex to base64
Straight forward hex to b64 and back, I used the standart python encode function.

### Challenge 2: Fixed xor
I chose to systematically check if the input can be decoded as hex or b64 and if not, assume it's byte input, else convert it to bytes. The conversion then happens on a byte for byte basis.

### Challenge 3: Single-byte XOR cipher
There are several ways to do this. All involve testing the result of xoring the text against a range of characters. The first way is to use the Vigenere approach and basically test the distribution of characters vs. a frequency distribution of letters in the english language. In my opinion overkill which is why I went for the second method which involves looping only through printable chars (a-bA-B09 and punctuation, newlines etc.) and checking if the output is all printable chars. The reason is that using xor yields values from 0-255 but only ~30-120 are printable. I.e. the chance of getting a printable char is about 1/3. The chance of getting all printable chars for a deciphered text, whereby that text is not the original, is extremely unlinkely the longer the text.
I modified the original xor function to check whether the input of a and b is equal, or if one has length 1 to keep the code compact.

### Challenge 4: Detect single-character XOR
Frankly, bruteforce is the key. Run each string through the script from challenge 3 and find the only printable one. 

### Challenge 5: Implement repeating-key XOR
Took the xor function and added code for when the length isn't equal but none of the lengths is 1. THen you basically encrypt looping over the shorter string. Not really rocket science...

### Challenge 6: Break repeating-key XOR
That one was a bit longer and more complicated. The basic idea is that the encryption schema will be like this given the key "KEY":
```
THIS IS THE SECRET PASSPHRASE
KEYKEYKEYKEYKEYKEYKEYKEYKEYKE
```
The result (in hex):
```
1f0d1018651018650d03007918001a19000d6b15181816090317181800
```

The good thing about xor is that it is deterministic. a xor b will always be c for the same pair (a,b). In repeating ciphers, we also know that for a key of length n, every n^th letter will be encoded by the same key char. So if we were to break up the result in blocks of 3 (length of 'KEY'), we'd get the following decryption schema:
```
1f0d10
K E Y
186510
K E Y
```
etc.

What we see is that if we were to take  one byte for every 3 bytes of the encrypted text and xor it against 'K' we would obtain readable text. 

The idea is thus simple: break up the encrypted text in blocks of length n, transpose and basically use single byte xor decryption methods on each transposed block to yield the key. But wait, we don't know the key length. How to do that? Well, the easiest as suggested by the challenge, is to compute the Hamming distance between the first 2 consecutive blocks of length i in the ciphertext. The Hamming distance is just the number of bits that need to be changed to transform a in b. 
E.g.:
```
dist('A','B') is:
A: 0b1000001
B: 0b1000010
          ^^
2 bits changed so distance is 2      
```
Easy as pie. By taking that distance and dividing it by blocksize, you get a normalized distance. Taking the smallest distance will most probably yield the key length (the challenge suggests taking 2-3 of the smallest values). I actually took the first 4 and computed the average normalized distance for all pair combinations within that group.

This yields the correct key length. I added a padding function to my blockbreaking method to avoid issues during transposing, transposed and then solved each individual transposed block as a single byte xor as outlined above which yielded the semi-correct text (2 chars were missing but you could get them from context...)

### Challenge 7: AES in ECB mode
Yeah dawg, I used python's inbuilt AES cipher for that...

### Challenge 8: Detect AES in ECB mode
Actually relatively easy because of what was discussed for Challenge 6: xor is deterministic and so is AES ECB: same text yields same cipher. What I did there was take each hex string, decode it, breakblock it in chunks of 16 (I tried up to 40 just to be thorough) and then use itertools to create each possible combination of 2 blocks within each string and subsequently assert whether they were identical. Only one text satisfied those requirements and done we are.





