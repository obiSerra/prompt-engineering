import argparse
import json
import re
from prompt_engineering.__main__ import gen_document

# from prompt_engineering.gpt_client import GptClient


def gen_document_cli(input_file: str):
    print("Generating document...")
    with open(input_file, "r") as f:
        config = f.read()

    print(gen_document(config))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ChatGPT CLI - Document Generation")
    parser.add_argument("input_file", help="The input file with the instructions")

    args = parser.parse_args()
    # gen_document(**vars(args))
