.data
space: .asciiz "\n"
errmsg: .asciiz "Index out of bounds\n"
.text
.globl main
main:
TEST2:
addiu $sp $sp -80
addiu $sp $sp -80
li $a0 ' '
sb $a0 0($sp)
addiu $sp $sp -4
li $a0 2
sw $a0 0($sp)
addiu $sp $sp -4
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
li $a0 0
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
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 4($fp)
mul $a0 $a0 4
blt $a0 80 l3
la $a0 errmsg
li $v0 4
syscall
li $v0 10
syscall
l3:
sub $a0 $a0 172
mul $a0 $a0 -1
lw $t1 4($sp)
addiu $sp $sp 4
add $a0 $a0 $fp
sw $t1 0($a0)
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
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
lw $t4 8($sp)
lw $t5 4($sp)
sw $t4 4($sp)
sw $t5 8($sp)
addiu $fp $fp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 19
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 8($sp)
sub $a0 $a0 1
sw $a0 4($fp)
l4:
lw $a0 4($fp)
add $a0 $a0 1
lw $t4 4($sp)
bgt $a0 $t4 l5
sw $a0 4($fp)
li $a0 20
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 4($fp)
lw $t1 4($sp)
sub $a0 $t1 $a0
addiu $sp $sp 4
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 4($fp)
mul $a0 $a0 4
blt $a0 80 l6
la $a0 errmsg
li $v0 4
syscall
li $v0 10
syscall
l6:
sub $a0 $a0 92
mul $a0 $a0 -1
lw $t1 4($sp)
addiu $sp $sp 4
add $a0 $a0 $fp
sw $t1 0($a0)
j l4
l5:
addiu $sp $sp 4
addiu $sp $sp 4
lw $t4 8($sp)
lw $t5 4($sp)
sw $t4 4($sp)
sw $t5 8($sp)
addiu $fp $fp 4
addiu $sp $sp 4
ll2:
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
lw $t4 8($sp)
lw $t5 4($sp)
sw $t4 4($sp)
sw $t5 8($sp)
addiu $fp $fp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 19
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 8($sp)
sub $a0 $a0 1
sw $a0 4($fp)
l7:
lw $a0 4($fp)
add $a0 $a0 1
lw $t4 4($sp)
bgt $a0 $t4 l8
sw $a0 4($fp)
lw $a0 8($fp)
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 4($fp)
mul $a0 $a0 4
sub $a0 $a0 172
mul $a0 $a0 -1
add $a0 $a0 $fp
lw $a0 0($a0)
lw $t1 4($sp)
mul $a0 $t1 $a0
addiu $sp $sp 4
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 4($fp)
mul $a0 $a0 4
sub $a0 $a0 92
mul $a0 $a0 -1
add $a0 $a0 $fp
lw $a0 0($a0)
lw $t1 4($sp)
add $a0 $t1 $a0
addiu $sp $sp 4
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 4($fp)
mul $a0 $a0 4
blt $a0 80 l9
la $a0 errmsg
li $v0 4
syscall
li $v0 10
syscall
l9:
sub $a0 $a0 92
mul $a0 $a0 -1
lw $t1 4($sp)
addiu $sp $sp 4
add $a0 $a0 $fp
sw $t1 0($a0)
j l7
l8:
addiu $sp $sp 4
addiu $sp $sp 4
lw $t4 8($sp)
lw $t5 4($sp)
sw $t4 4($sp)
sw $t5 8($sp)
addiu $fp $fp 4
addiu $sp $sp 4
ll3:
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
lw $t4 8($sp)
lw $t5 4($sp)
sw $t4 4($sp)
sw $t5 8($sp)
addiu $fp $fp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 19
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 8($sp)
sub $a0 $a0 1
sw $a0 4($fp)
l10:
lw $a0 4($fp)
add $a0 $a0 1
lw $t4 4($sp)
bgt $a0 $t4 l11
sw $a0 4($fp)
lw $a0 4($fp)
mul $a0 $a0 4
sub $a0 $a0 92
mul $a0 $a0 -1
add $a0 $a0 $fp
lw $a0 0($a0)
li $v0 1
syscall
lw $a0 12($fp)
li $v0 11
syscall
j l10
l11:
addiu $sp $sp 4
addiu $sp $sp 4
lw $t4 8($sp)
lw $t5 4($sp)
sw $t4 4($sp)
sw $t5 8($sp)
addiu $fp $fp 4
addiu $sp $sp 4
ll4:
la $a0 space
li $v0 4
syscall
lw $ra 4($sp)
addiu $sp $sp 4
lw $fp 4($sp)
addiu $sp $sp 172
jr $ra
li $v0 10
syscall
