# Mock Extractors

For testing workflow engines. Very much WIP, and probably useless to anybody else.

## How to run

```bash
docker build -t test/me2 -f Dockerfile.me2 .
makeflow -c --jx extractors.jx
ls -alt output/* 
makeflow --jx --retry-count=10 --max-local=10 extractors.jx
ls -alt output/*
```