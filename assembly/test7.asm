.data
space: .asciiz "\n"
errmsg: .asciiz "Index out of bounds\n"
.text
.globl main
main:
TEST7:
li $a0 10
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 '1'
sb $a0 0($sp)
addiu $sp $sp -4
move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
lw $a0 12($fp)
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 50
lw $t1 4($sp)
add $a0 $t1 $a0
addiu $sp $sp 4
sw $a0 8($fp)
lw $a0 12($fp)
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
lw $t1 4($sp)
div $a0 $t1 $a0
addiu $sp $sp 4
sw $a0 8($fp)
lw $a0 8($fp)
li $v0 1
syscall
la $a0 space
li $v0 4
syscall
lw $ra 4($sp)
addiu $sp $sp 4
lw $fp 4($sp)
addiu $sp $sp 16
jr $ra
li $v0 10
syscall
