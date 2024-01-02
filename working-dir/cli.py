import argparse
import json
import re
from prompt_engineering.__main__ import gen_document

# from prompt_engineering.gpt_client import GptClient


def gen_document_cli(**kwargs):
    print("Generating document...")

    # print(kwargs)

    with open("document-input.md", "r") as f:
        config = [re.sub(r"\n", "", l) for l in f.readlines()]

    print(gen_document("\n".join(config)))


def gen_summary():
    print("Generating summary...")


if __name__ == "__main__":
    commands = {"generate-document": gen_document_cli, "generate-summary": gen_summary}
    parser = argparse.ArgumentParser(description="ChatGPT CLI")
    parser.add_argument("command", metavar="cmd", choices=list(commands.keys()), help="the command to run")
    parser.add_argument("-c", "--config", metavar="config", help="the config file to use")

    args = parser.parse_args()
    commands[args.command](**vars(args))
