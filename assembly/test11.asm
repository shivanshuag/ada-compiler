.data
space: .asciiz "\n"
errmsg: .asciiz "Index out of bounds\n"
.text
.globl main
main:
TEST11:
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
li $a0 10
sw $a0 12($fp)
li $a0 3
sw $a0 8($fp)
lw $a0 8($fp)
sw $a0 0($sp)
addiu $sp $sp -4
el0:
li $a0 1
lw $t1 4($sp)
beq $a0 $t1 l2
j el1
l2:
lw $a0 12($fp)
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 1
lw $t1 4($sp)
mul $a0 $t1 $a0
addiu $sp $sp 4
sw $a0 4($fp)
j l1
el1:
li $a0 2
lw $t1 4($sp)
beq $a0 $t1 l3
j el2
l3:
lw $a0 12($fp)
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 2
lw $t1 4($sp)
mul $a0 $t1 $a0
addiu $sp $sp 4
sw $a0 4($fp)
j l1
el2:
li $a0 3
lw $t1 4($sp)
beq $a0 $t1 l4
j el3
l4:
lw $a0 12($fp)
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 3
lw $t1 4($sp)
mul $a0 $t1 $a0
addiu $sp $sp 4
sw $a0 4($fp)
j l1
el3:
j l5
j el4
l5:
lw $a0 12($fp)
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 4
lw $t1 4($sp)
mul $a0 $t1 $a0
addiu $sp $sp 4
sw $a0 4($fp)
j l1
el4:
l1:
addiu $sp $sp 4
lw $a0 4($fp)
li $v0 1
syscall
lw $ra 4($sp)
addiu $sp $sp 4
lw $fp 4($sp)
addiu $sp $sp 16
jr $ra
li $v0 10
syscall
