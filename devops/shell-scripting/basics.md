### Conditional `if` Statement Example

```bash
a=40
b=20

if [ $a -gt $b ]
then
    echo "a is greater"
else
    echo "b is greater"
fi
```

Compares the values of two variables and executes different commands based on the result of the comparison.

Explanation:

- `a=40` : Assigns the value `40` to variable `a`.
- `b=20` : Assigns the value `20` to variable `b`.
- `if [ $a -gt $b ]` : Checks whether `a` is greater than `b`.
- `then` : Begins the block of commands executed when the condition is true.
- `echo "a is greater"` : Prints a message if `a` is greater than `b`.
- `else` : Begins the block of commands executed when the condition is false.
- `echo "b is greater"` : Prints a message if `a` is not greater than `b`.
- `fi` : Ends the `if` statement.

Output:

```bash
a is greater
```

Common Numeric Comparison Operators:

| Operator | Meaning                  |
| -------- | ------------------------ |
| `-eq`    | Equal to                 |
| `-ne`    | Not equal to             |
| `-gt`    | Greater than             |
| `-ge`    | Greater than or equal to |
| `-lt`    | Less than                |
| `-le`    | Less than or equal to    |

Notes:

- There must be spaces after `[` and before `]`.
- For numeric comparisons, use operators like `-gt`, `-lt`, and `-eq`.
- Using `>` inside `[ ]` performs string comparison or redirection-related behavior depending on the shell and is not recommended for numeric comparisons.

# Loops in Shell Scripting

## `for` Loop

A `for` loop executes a block of code repeatedly for each item in a list or range.

### Example

```bash
for i in 1 2 3 4 5
do
    echo $i
done
```

Explanation:

- `for i in 1 2 3 4 5` : Iterates through each value in the list.
- `do` : Begins the loop body.
- `echo $i` : Prints the current value of `i`.
- `done` : Ends the loop.

Output:

```bash
1
2
3
4
5
```

### Range Example

```bash
for i in {1..5}
do
    echo $i
done
```

Output:

```bash
1
2
3
4
5
```

### Practical Example

```bash
for file in *.log
do
    echo $file
done
```

Lists all `.log` files in the current directory.

---

## `while` Loop

A `while` loop executes as long as the specified condition remains true.

### Example

```bash
count=1

while [ $count -le 5 ]
do
    echo $count
    count=$((count + 1))
done
```

Explanation:

- `count=1` : Initializes the counter.
- `while [ $count -le 5 ]` : Continues looping while count is less than or equal to 5.
- `echo $count` : Prints the current count value.
- `count=$((count + 1))` : Increments the counter.
- `done` : Ends the loop.

Output:

```bash
1
2
3
4
5
```

### Practical Example

```bash
while read line
do
    echo $line
done < file.txt
```

Reads a file line by line and processes each line.

---

## `do-while` Loop

Shell scripting does not provide a built-in `do-while` loop. Similar behavior can be achieved using an infinite loop with a conditional break.

### Example

```bash
count=1

while true
do
    echo $count
    count=$((count + 1))

    if [ $count -gt 5 ]
    then
        break
    fi
done
```

Explanation:

- `while true` : Creates an infinite loop.
- `echo $count` : Prints the current value.
- `count=$((count + 1))` : Increments the counter.
- `if [ $count -gt 5 ]` : Checks if the condition to stop has been met.
- `break` : Exits the loop.
- `done` : Ends the loop.

Output:

```bash
1
2
3
4
5
```

This mimics a traditional do-while loop because the loop body executes at least once before the condition is checked.

---

## Loop Control Statements

### `break`

Immediately exits the loop.

Example:

```bash
for i in {1..10}
do
    if [ $i -eq 5 ]
    then
        break
    fi

    echo $i
done
```

Output:

```bash
1
2
3
4
```

---

### `continue`

Skips the current iteration and moves to the next iteration.

Example:

```bash
for i in {1..5}
do
    if [ $i -eq 3 ]
    then
        continue
    fi

    echo $i
done
```

Output:

```bash
1
2
4
5
```
