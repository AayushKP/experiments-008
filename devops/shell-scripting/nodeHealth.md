### `set -x`

Enables shell debugging mode. Each command and its expanded arguments are printed to the terminal before execution. Useful for troubleshooting shell scripts.

Example:

```bash
set -x
echo $HOME
```

Output:

```bash
+ echo /home/ec2-user
/home/ec2-user
```

---

### `set -e`

Causes the shell script to exit immediately if any command returns a non-zero (error) status. Helps prevent scripts from continuing after a failure.

Example:

```bash
set -e
mkdir test
cd nonexistent_directory
echo "This line will not execute"
```

---

### `set -o`

Displays the current status of all shell options.

Example:

```bash
set -o
```

Output:

```bash
errexit         off
nounset         off
xtrace          off
```

---

### `df -h`

Displays disk space usage for all mounted filesystems in a human-readable format (KB, MB, GB, TB).

Example:

```bash
df -h
```

Use case:

- Check available disk space.
- Identify full filesystems.

---

### `free -g`

Displays system memory usage in gigabytes.

Example:

```bash
free -g
```

Shows:

- Total memory
- Used memory
- Free memory
- Buffers/cache
- Swap usage

---

### `nproc`

Displays the number of available CPU processing units (cores).

Example:

```bash
nproc
```

Use case:

- Determine how many CPU cores are available.
- Useful for configuring parallel jobs.

---

### `ps -ef`

Displays detailed information about all running processes.

Options:

- `-e` : Show all processes.
- `-f` : Full-format listing.

Example:

```bash
ps -ef
```

Common information shown:

- User
- Process ID (PID)
- Parent Process ID (PPID)
- Start time
- Command

---

### `ps -ef | grep "amazon"`

Searches the process list for processes containing the word `"amazon"`.

Example:

```bash
ps -ef | grep "amazon"
```

Use case:

- Verify whether a specific application or service is running.

---

### `ps -ef | grep "amazon" | awk -F" " '{print $2}'`

Finds processes containing `"amazon"` and prints the second column, which is typically the Process ID (PID).

Example:

```bash
ps -ef | grep "amazon" | awk -F" " '{print $2}'
```

Use case:

- Retrieve process IDs for monitoring or termination.

---

### `cat logfile | grep "error"`

Searches a log file for lines containing the word `"error"`.

Example:

```bash
cat logfile | grep "error"
```

Recommended form:

```bash
grep "error" logfile
```

Use case:

- Identify errors in application or system logs.

---

### `curl url`

Sends an HTTP request to the specified URL and displays the response.

Example:

```bash
curl https://example.com
```

Use case:

- Test APIs.
- Download content.
- Verify website accessibility.

---

### `curl -X GET url`

Sends an explicit HTTP GET request to the specified URL.

Example:

```bash
curl -X GET https://example.com/api
```

Note:

- `GET` is the default method, so `curl url` and `curl -X GET url` usually behave the same.

---

### `wget url | grep search_keyword`

Downloads content from a URL and searches for a specific keyword in the response.

Example:

```bash
wget -qO- https://example.com | grep "success"
```

Options used in practice:

- `-q` : Quiet mode.
- `-O-` : Write output to standard output.

Use case:

- Validate content returned by a webpage or API.

---

### `sudo su -`

Switches to the root user and loads the root user's login environment.

Example:

```bash
sudo su -
```

Use case:

- Perform administrative tasks requiring root privileges.

---

### `su ec2-user`

Switches from the current user to the `ec2-user` account.

Example:

```bash
su ec2-user
```

Use case:

- Run commands as the EC2 default user without logging out.

---

### `sudo find / -name pam`

Searches the entire filesystem for files or directories named `pam`.

Example:

```bash
sudo find / -name pam
```

Options:

- `/` : Start searching from the root directory.
- `-name pam` : Match files/directories with the exact name `pam`.

Use case:

- Locate files, directories, or configurations related to PAM (Pluggable Authentication Modules).
