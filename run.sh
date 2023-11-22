#!/usr/bin/env bash


source ./.env


echo "[+] Runnning docker env:"
echo "${ML_PROJECT_NAME}"

docker run -v ./working-dir:/home/working-dir $ML_PROJECT_NAME $@

echo "[+] Done"