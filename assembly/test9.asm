.data
space: .asciiz "\n"
errmsg: .asciiz "Index out of bounds\n"
.text
.globl main
main:
TEST9:
move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
lw $t4 8($sp)
lw $t5 4($sp)
sw $t4 4($sp)
sw $t5 8($sp)
addiu $fp $fp -4
li $a0 5
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 19
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 8($sp)
sub $a0 $a0 1
sw $a0 4($fp)
l1:
lw $a0 4($fp)
add $a0 $a0 1
lw $t4 4($sp)
bgt $a0 $t4 l2
sw $a0 4($fp)
lw $a0 4($fp)
li $v0 1
syscall
j l1
l2:
addiu $sp $sp 4
addiu $sp $sp 4
lw $t4 8($sp)
lw $t5 4($sp)
sw $t4 4($sp)
sw $t5 8($sp)
addiu $fp $fp 4
addiu $sp $sp 4
ll1:
lw $ra 4($sp)
addiu $sp $sp 4
lw $fp 4($sp)
addiu $sp $sp 4
jr $ra
li $v0 10
syscall
