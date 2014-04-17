.data
space: .asciiz "\n"
errmsg: .asciiz "Index out of bounds\n"
.text
.globl main
main:
TEST17:
li $a0 0
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
li $a0 1
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 2
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 3
lw $t1 4($sp)
mul $a0 $t1 $a0
addiu $sp $sp 4
lw $t1 4($sp)
add $a0 $t1 $a0
addiu $sp $sp 4
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 3
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 4
lw $t1 4($sp)
add $a0 $t1 $a0
addiu $sp $sp 4
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 5
lw $t1 4($sp)
mul $a0 $t1 $a0
addiu $sp $sp 4
lw $t1 4($sp)
mul $a0 $t1 $a0
addiu $sp $sp 4
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 3
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 5
lw $t1 4($sp)
add $a0 $t1 $a0
addiu $sp $sp 4
lw $t1 4($sp)
sub $a0 $t1 $a0
addiu $sp $sp 4
sw $a0 12($fp)
lw $a0 12($fp)
li $v0 1
syscall
lw $ra 4($sp)
addiu $sp $sp 4
lw $fp 4($sp)
addiu $sp $sp 16
jr $ra
li $v0 10
syscall
