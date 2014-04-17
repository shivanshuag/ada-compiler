.data
space: .asciiz "\n"
errmsg: .asciiz "Index out of bounds\n"
.text
.globl main
main:
TEST4:
li $a0 3
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
lw $a0 8($fp)
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 1
lw $t1 4($sp)
seq $a0 $t1 $a0
addiu $sp $sp 4
beq $a0 0 l1
li $a0 1
sw $a0 4($fp)
lw $a0 4($fp)
li $v0 1
syscall
j l2
l1:
lw $a0 8($fp)
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 4
lw $t1 4($sp)
slt $a0 $t1 $a0
addiu $sp $sp 4
beq $a0 0 l3
li $a0 2
sw $a0 4($fp)
lw $a0 4($fp)
li $v0 1
syscall
lw $a0 8($fp)
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 3
lw $t1 4($sp)
seq $a0 $t1 $a0
addiu $sp $sp 4
beq $a0 0 l4
li $a0 3
sw $a0 4($fp)
lw $a0 4($fp)
li $v0 1
syscall
j l5
l4:
l5:
j l6
l3:
lw $a0 8($fp)
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 8
lw $t1 4($sp)
slt $a0 $t1 $a0
addiu $sp $sp 4
beq $a0 0 l7
li $a0 4
sw $a0 4($fp)
lw $a0 4($fp)
li $v0 1
syscall
j l8
l7:
lw $a0 8($fp)
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 16
lw $t1 4($sp)
slt $a0 $t1 $a0
addiu $sp $sp 4
beq $a0 0 l9
li $a0 8
sw $a0 4($fp)
lw $a0 4($fp)
li $v0 1
syscall
j l10
l9:
l10:
l8:
l6:
l2:
lw $ra 4($sp)
addiu $sp $sp 4
lw $fp 4($sp)
addiu $sp $sp 12
jr $ra
li $v0 10
syscall
