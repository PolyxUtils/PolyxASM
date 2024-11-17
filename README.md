# PolyxASM

/!\ This read file is outdated, please do not associate it with the current version of the project

# Size of operands:
    
| Bits | Polasm | amd64 | arm64 | Risc V |
| - | - | - | - | - |
| 64 | Q (Qword) | R | X | |
| 32 | D (Dword) | E | W | |
| 16 | W (Word)  |   |   | |
| 8  | B (Byte)  |   |   | |

# Instruction set

 - [ABS](#abs)
 - 

## ABS
 Takes the absolute value of the signed integer stored in the source register and writes the result in the source register.


 - ABS regQ[dst], regQ[src]
```assembly_x86
mov dst, src 
neg dst
cmovl dst, src
```
 - ABS regD[dst], regD[src]




 - [ARM Documentation](https://developer.arm.com/documentation/ddi0602/2024-09/Base-Instructions/ABS--Absolute-value-?lang=en)
