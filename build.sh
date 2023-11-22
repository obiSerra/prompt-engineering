#!/usr/bin/env bash


source ./.env


echo "[+] Build docker image:"
echo "${ML_PROJECT_NAME}"

docker build -t $ML_PROJECT_NAME  .