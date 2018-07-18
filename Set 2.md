# Set 2

### Challenge 1: Implement PKCS#7 padding
I slightly modified and extracted the padding algo I used for the breakcipher and made it a standalone function. #notrocketscience

### Challenge 2: Implement CBC mode
I'm a visual guy, I need to see to understand. Googling "Decrypt CBC" yield a hundred images that explain how exactly. It's pretty straightforward: CBC uses ECB with a twist. You encrypt as follows:

1. Pad plaintext to be divisible by the key length keylen
2. Divide the plaintext in blocks of size keylen
3. Take the first block, xor it with a chosen initialization vector IV and encrypt it using simple ECB
4. Take the second block, xor it with the previous bloc and encrypt it with ECB
5. DO 4 WHILE not the last block

In order to decrypt you do the exact opposite:

1. Divide the ciphertext in blocks of size keylen
2. Take the first block, decrypt it using ECB and the key, then xor it with your IV
3. Take the second block, decrypt it using ECB and the key, then xor it with the previous block
4. DO 3 WHILE not the last block

A simple implementation in python quickly yields the desired plaintext.

### Challenge 3
