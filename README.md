# PolyxASM

# Size of operands:
    
| Bits | Polasm | amd64 | arm64 |
| - | - | - | - |
| 64 | Q (Qword) | R | X |
| 32 | D (Dword) | E | W |
| 16 | W (Word)  |   |   |
| 8  | B (Byte)  |   |   |

# Instruction set

 - [ABS](#abs)
 - 

## ABS
 Takes the absolute value of the signed integer stored in the source register and writes the result in the source register.


 - ABS [Qn], [Qm]
 - ABS [Dn], [Dm]

```assembly_x86
mov Qn, Qm ;store eax in ebx
neg Qn
cmovl Qn, Qm
```


 - [ARM Documentation](https://developer.arm.com/documentation/ddi0602/2024-09/Base-Instructions/ABS--Absolute-value-?lang=en)
