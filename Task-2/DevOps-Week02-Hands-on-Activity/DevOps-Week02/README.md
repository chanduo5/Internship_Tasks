# DevOps-Week02

Hands-on Git & GitHub activity for the DevOps internship — managing source code
of a small sample application through branching, merging, conflict resolution,
and pull requests, simulating a real team collaboration workflow.

## Project Structure

| File | Purpose |
|---|---|
| `app.py` | Sample Python application entry point with logging |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Container build definition with healthcheck |
| `config.yaml` | Application and server configuration |
| `.gitignore` | Files/folders excluded from version control |

## Features
- Logging added to app.py for better traceability during runtime.
- Dockerfile updated with a HEALTHCHECK instruction for container monitoring.

## Git Workflow Followed

1. Initialized repository and committed baseline project files to `main`.
2. Created `feature/add-logging` branch -> added logging to `app.py`, updated README.
3. Created `feature/docker-improvements` branch -> added Docker healthcheck, updated `config.yaml`, updated README.
4. Merged `feature/add-logging` into `main` (clean merge).
5. Merged `feature/docker-improvements` into `main` -> conflict in `README.md`
   (both branches edited the same `## Features` section) -> resolved manually
   by keeping both feature entries.
6. Opened a Pull Request for review before merging into `main`.

## Getting Started

\`\`\`bash
git clone https://github.com/<your-username>/DevOps-Week02.git
cd DevOps-Week02
pip install -r requirements.txt
python app.py
\`\`\`

### Run with Docker

\`\`\`bash
docker build -t devops-week02 .
docker run devops-week02
\`\`\`

## Author
Chandu - Junior DevOps Engineer (Intern)
