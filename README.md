# Prompt Engineering Playground

This project was inspired by the talk [Pydantic is all you need: Jason Liu](https://www.youtube.com/watch?v=yj-wSRJwrrc)

The goal is to experiment with `Pydantic` and `OpenAI` APIs to implement complex prompt engineering patterns. 

## Setup

Clone or fork this repository.

1. Create a `.env` file using the `env_config-SAMPLE` as a template.
2. Rename the `SAMPLE-key.txt` files to `key.txt` and add your API key.

## Build

```
$ ./build.sh
```

## Run

```
$ ./run.sh <command>
```

Eg:
```
$ ./run.sh python -m prompt_engineering
```
