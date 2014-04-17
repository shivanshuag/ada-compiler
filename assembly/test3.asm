.text
FIB:
move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
lw $a0 4($fp)
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
lw $t1 4($sp)
seq $a0 $t1 $a0
addiu $sp $sp 4
beq $a0 0 l1
li $a0 0
lw $ra 4($sp)
addiu $sp $sp 12
lw $fp 0($sp)
jr $ra
j l2
l1:
lw $a0 4($fp)
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 1
lw $t1 4($sp)
seq $a0 $t1 $a0
addiu $sp $sp 4
beq $a0 0 l3
li $a0 1
lw $ra 4($sp)
addiu $sp $sp 12
lw $fp 0($sp)
jr $ra
j l4
l3:
sw $fp 0($sp)
addiu $sp $sp -4
lw $a0 4($fp)
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 1
lw $t1 4($sp)
sub $a0 $t1 $a0
addiu $sp $sp 4
sw $a0 0($sp)
addiu $sp $sp -4
jal FIB
sw $a0 0($sp)
addiu $sp $sp -4
sw $fp 0($sp)
addiu $sp $sp -4
lw $a0 4($fp)
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 2
lw $t1 4($sp)
sub $a0 $t1 $a0
addiu $sp $sp 4
sw $a0 0($sp)
addiu $sp $sp -4
jal FIB
lw $t1 4($sp)
add $a0 $t1 $a0
addiu $sp $sp 4
lw $ra 4($sp)
addiu $sp $sp 12
lw $fp 0($sp)
jr $ra
l4:
l2:
lw $ra 4($sp)
addiu $sp $sp 4
lw $fp 4($sp)
addiu $sp $sp 8
jr $ra
.data
space: .asciiz "\n"
errmsg: .asciiz "Index out of bounds\n"
.text
.globl main
main:
TEST3:
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
li $a0 6
sw $a0 8($fp)
sw $fp 0($sp)
addiu $sp $sp -4
lw $a0 8($fp)
sw $a0 0($sp)
addiu $sp $sp -4
jal FIB
sw $a0 4($fp)
lw $a0 4($fp)
li $v0 1
syscall
la $a0 space
li $v0 4
syscall
lw $ra 4($sp)
addiu $sp $sp 4
lw $fp 4($sp)
addiu $sp $sp 12
jr $ra
li $v0 10
syscall
