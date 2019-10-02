# Mock Extractors and Makeflow

For testing workflow engines. Very much WIP, and probably useless to anybody else.

## Install requirements

- Makeflow: <https://ccl.cse.nd.edu/software/manuals/makeflow.html#installing>
- Docker: <https://docs.docker.com/install/>


### MacOS specific

`flock`:

```bash
brew tap discoteq/discoteq
brew install flock
``` 


## Configure

Copy `jx-args.json.example` to `jx-args.json` and modify to suit.


## How to run

```bash
# Clear the workflow output directory
makeflow -c --jx --jx-args=jx-args.json extractors.jx

# Run the workflow
makeflow --jx --jx-args=jx-args.json --retry-count=10 --max-local=10 extractors.jx

# Check the output
ls -alt output/*
```

Use Docker to run workflow:

```bash
# Build the Docker image
docker build -t test/mock-extractors -f Dockerfile .

# Save the Docker image as a TAR file
docker save -o mock-extractors-image.tar test/mock-extractors:latest

# Clear the workflow output directory
makeflow -c --jx --jx-args=jx-args.json extractors.jx

# Run the workflow
makeflow --jx --jx-args=jx-args.json --docker=test/mock-extractors --docker-tar=mock-extractors-image.tar --retry-count=10 --max-local=10 extractors.jx

# Check the output
ls -alt output/*
```


## See what the workflow looks like rendered as JSON

```bash
jx2json --pretty extractors.jx > extractors.json
```
