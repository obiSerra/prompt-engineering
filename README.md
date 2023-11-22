# Docker Environment for ML


This is a boilerplate repository for my docker environments for ML.

## Usage

Build and run a docker container with a specific ML setup.
Use the `working-dir` folder to mount your project folder into the docker container.

### Setup

Clone or fork this repository.

1. Update the `Dockerfile` according to your project needs.
2. Create a `.env` file using the `env_config-SAMPLE` as a template.

### Build

```
$ ./build.sh
```

#### Manual Build

```
$ docker build -t <docker-build-name>  .
```

### Run

```
$ ./run.sh
```

#### Manual Run
```
$ docker run -p 8888:8888 -v ./working-dir:/home/jovyan/working-dir <docker-build-name>
```


