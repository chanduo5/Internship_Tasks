# Linux Fundamentals — Week 1 (DevOps Internship)

**Davine Technologies — DevOps Internship**
**Submitted by:** Chander Mohan Meena
**Topic:** Hands-on Activity — Linux File & Directory Management

## Overview

This activity demonstrates core Linux file and directory management skills as part of Week 1 of the DevOps Internship. It covers creating a project directory structure, managing files, setting permissions, and compressing directories — foundational skills used later in automation, scripting, and cloud infrastructure tasks.

## Objectives

- Reinforce understanding of basic Linux commands
- Get hands-on practice with users, groups, files, and permissions
- Build a foundation for later weeks involving automation, scripting, and cloud infrastructure

## Environment

- OS: Kali Linux
- Shell: Bash (zsh-style prompt)
- User: `kali`

## Steps Performed

### 1. Create the Directory Structure

```bash
cd
ls
mkdir devops
cd devops
mkdir projects/ logs/ scripts/
ls
cd ..
```

Created a `devops/` directory containing three subdirectories: `projects`, `logs`, and `scripts`.

### 2. Create Sample Files

```bash
touch devops/projects/main.py devops/logs/system.logs devops/scripts/deploy.sh
```

Verified each file landed in its correct subdirectory:

```bash
cd devops/logs && ls      # system.logs
cd ../scripts && ls       # deploy.sh
cd ../projects && ls      # main.py
```

### 3. Set Appropriate Permissions

```bash
ls -ld devops/
# drwxrwxr-x 5 kali kali 4096 Jul 24 08:35 devops/

chmod -R 755 devops/
ls -ld devops/
# drwxr-xr-x 5 kali kali 4096 Jul 24 08:35 devops/

chmod +x devops/scripts/deploy.sh
```

- Applied `755` recursively to the `devops/` directory (owner: read/write/execute, group & others: read/execute).
- Made `deploy.sh` executable for use as a deployment script.

### 4. Compress the Folder into a ZIP File

```bash
sudo apt update && sudo apt install zip
zip -r devops_compressed.zip devops/
ls -lh devops_compressed.zip
# -rw-rw-r-- 1 kali kali 1.2K Jul 24 08:57 devops_compressed.zip
```

## Directory Structure

```
devops/
├── logs/
│   └── system.logs
├── projects/
│   └── main.py
└── scripts/
    └── deploy.sh
```

## Commands Used

| Command | Purpose |
|---|---|
| `mkdir` | Create directories |
| `touch` | Create empty files |
| `ls` | List directory contents |
| `cd` | Change directory |
| `chmod` | Change file/directory permissions |
| `zip` | Compress files/directories into an archive |
| `sudo apt install` | Install a package (zip utility) |

## Key Takeaways

- `chmod -R 755` recursively sets read/write/execute for the owner and read/execute for group and others — appropriate for scripts and project folders that don't contain sensitive data.
- `chmod +x` is required separately to make a specific script executable.
- `zip -r` archives an entire directory tree, preserving its structure.

---
*Part of the DevOps Internship program at Davine Technologies.*
