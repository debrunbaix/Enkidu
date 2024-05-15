# Report for login at 2024-05-15

<div></div>
## Summary

- [General Information](#general-information)
- [Security of the Binary](#security-of-the-binary)
- [Strings](#strings)
- [Assembly Code](#assembly-code)
- [Code Analysis](#code-analysis)
- [Exploits](#exploits)
- [Credits](#credits)

<div></div>
## Enumeration

### Binary Information

<table>
<tr>
<th>File Name</th>
<th>Path</th>
<th>Format</th>
<th>Bit</th>
</tr>
<tr>
<td>login</td>
<td>app/testFile/login</td>
<td>ELF</td>
<td>32-bit</td>
</tr>
</table>

### Security of the Binary

<table>
<tr><th colspan='4'>Basic Security Features</th></tr>
<tr>
<th>Linked</th>
<th>Stripped</th>
<th>RELRO</th>
<th>Canary</th>
</tr>
<tr>
<td>dynamically linked</td>
<td>no</td>
<td>partial</td>
<td>no</td>
</tr>
</table>

<table>
<tr><th colspan='3'>Advanced Security Mechanisms</th></tr>
<tr>
<th>NX</th>
<th>PIE</th>
<th>RPath</th>
</tr>
<tr>
<td>no</td>
<td>no</td>
<td>no</td>
</tr>
</table>

<table>
<tr><th colspan='3'>Security Meta-Information</th></tr>
<tr>
<th>RunPath</th>
<th>Symbols</th>
<th>Fortify Source</th>
</tr>
<tr>
<td>no</td>
<td>yes</td>
<td>no</td>
</tr>
</table>

### Strings

- Enter admin password: 
- pass
- Correct Password!
- Incorrect Password!
- Successfully logged in as Admin (authorised=%d) :)
- Failed to log in as Admin (authorised=%d) :(
- login.c
- .note.gnu.build-id

### Vulnerable Functions

- gets
- printf

### Libraries

- linux-gate.so.1
- libc.so.6
- /lib/ld-linux.so.2

### Assembly Code
```assembly
xor ebp, ebp
pop esi
mov ecx, esp
and esp, 0xfffffff0
push eax
push esp
push edx
call 0x80490b3
add ebx, 0x2f70
lea eax, [ebx - 0x2d40]
push eax
lea eax, [ebx - 0x2da0]
push eax
push ecx
push esi
mov eax, 0x8049192
push eax
call 0x8049070
hlt
mov ebx, dword ptr [esp]
ret
nop
nop
nop
nop
nop
ret
nop
nop
nop
nop
nop
nop
nop
nop
mov ebx, dword ptr [esp]
ret
nop
nop
nop
nop
nop
nop
mov eax, 0x804c028
cmp eax, 0x804c028
je 0x8049110
mov eax, 0
test eax, eax
je 0x8049110
push ebp
mov ebp, esp
sub esp, 0x14
push 0x804c028
call eax
add esp, 0x10
leave
ret
lea esi, [esi]
nop
ret
lea esi, [esi]
lea esi, [esi]
nop
mov eax, 0x804c028
sub eax, 0x804c028
mov edx, eax
shr eax, 0x1f
sar edx, 2
add eax, edx
sar eax, 1
je 0x8049158
mov edx, 0
test edx, edx
je 0x8049158
push ebp
mov ebp, esp
sub esp, 0x10
push eax
push 0x804c028
call edx
add esp, 0x10
leave
ret
lea esi, [esi]
ret
lea esi, [esi]
cmp byte ptr [0x804c028], 0
jne 0x8049180
push ebp
mov ebp, esp
sub esp, 8
call 0x80490e0
mov byte ptr [0x804c028], 1
leave
ret
lea esi, [esi]
ret
lea esi, [esi]
lea esi, [esi]
nop
jmp 0x8049120
lea ecx, [esp + 4]
and esp, 0xfffffff0
push dword ptr [ecx - 4]
push ebp
mov ebp, esp
push ebx
push ecx
sub esp, 0x10
call 0x80490d0
add ebx, 0x2e57
mov dword ptr [ebp - 0xc], 0
sub esp, 0xc
lea eax, [ebx - 0x1ff8]
push eax
call 0x8049060
add esp, 0x10
sub esp, 0xc
lea eax, [ebp - 0x12]
push eax
call 0x8049050
add esp, 0x10
sub esp, 8
lea eax, [ebx - 0x1fe1]
push eax
lea eax, [ebp - 0x12]
push eax
call 0x8049030
add esp, 0x10
test eax, eax
jne 0x804920c
sub esp, 0xc
lea eax, [ebx - 0x1fdc]
push eax
call 0x8049060
add esp, 0x10
mov dword ptr [ebp - 0xc], 1
jmp 0x804921e
sub esp, 0xc
lea eax, [ebx - 0x1fca]
push eax
call 0x8049060
add esp, 0x10
cmp dword ptr [ebp - 0xc], 0
je 0x804923b
sub esp, 8
push dword ptr [ebp - 0xc]
lea eax, [ebx - 0x1fb4]
push eax
call 0x8049040
add esp, 0x10
jmp 0x8049250
sub esp, 8
push dword ptr [ebp - 0xc]
lea eax, [ebx - 0x1f80]
push eax
call 0x8049040
add esp, 0x10
mov eax, 0
lea esp, [ebp - 8]
pop ecx
pop ebx
pop ebp
lea esp, [ecx - 4]
ret
nop
push ebp
call 0x80492c1
add ebp, 0x2d9a
push edi
push esi
push ebx
sub esp, 0xc
mov ebx, ebp
mov edi, dword ptr [esp + 0x28]
call 0x8049000
lea ebx, [ebp - 0xf0]
lea eax, [ebp - 0xf4]
sub ebx, eax
sar ebx, 2
je 0x80492b5
xor esi, esi
lea esi, [esi]
sub esp, 4
push edi
push dword ptr [esp + 0x2c]
push dword ptr [esp + 0x2c]
call dword ptr [ebp + esi*4 - 0xf4]
add esi, 1
add esp, 0x10
cmp ebx, esi
jne 0x8049298
add esp, 0xc
pop ebx
pop esi
pop edi
pop ebp
ret
lea esi, [esi]
ret
mov ebp, dword ptr [esp]
ret
```

<div></div>
## Code Analysis

### Pseudo C Code

### ChatGPT Analysis

## Exploit

### Fuzzing
### Buffer Overflow

### Format String

## Credits

This report was generated using automated tools and the expert analysis of security researchers.
