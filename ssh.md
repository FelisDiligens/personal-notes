---
title: SSH
---

# SSH

## Commands

- `ssh`
- `scp` - OpenSSH secure file copy
- Authentication:
	- `ssh-copy-id` and `ssh-keygen`
	- `sshpass`

## SCP - OpenSSH secure file copy

Syntax:

```
scp <source> <destination>
```

To copy a file from `B` to `A` while logged into `B`:

```
scp /path/to/file username@a:/path/to/destination
```

To copy a file from `B` to `A` while logged into `A`:

```
scp username@b:/path/to/file /path/to/destination
```

> Source: https://unix.stackexchange.com/a/106482


## Authenticate using key

### Copy key to server

1. Generate key (this only needs to be done once):
```
$ ssh-keygen -t rsa -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/user/.ssh/id_rsa
Your public key has been saved in /home/user/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:redacted user@host
The key's randomart image is:
+---[RSA 4096]----+
|                 |
|                 |
|                 |
|                 |
|    redacted     |
|                 |
|                 |
|                 |
|                 |
+----[SHA256]-----+
```
(when asked for something just press enter)

1. Copy key to server:
```bash
$ ssh-copy-id -i ~/.ssh/id_rsa user@remote
```
(although the argument `-i <path>` should not be necessary)

1. Login with key:
```bash
ssh -i ~/.ssh/id_rsa user@remote
```
(although the argument `-i <path>` should not be necessary)

### If `ssh-copy-id` doesn't work

```bash
cat ~/.ssh/id_rsa.pub | ssh user@remote "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### Edit authorized keys on the server

```bash
vim ~/.ssh/authorized_keys
```
