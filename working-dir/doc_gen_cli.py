import argparse
import json
import re
from prompt_engineering.__main__ import gen_document

# from prompt_engineering.gpt_client import GptClient


def gen_document_cli(**kwargs):
    print("Generating document...")

    print(kwargs)

    exit()

    # with open("document-input.md", "r") as f:
    #     config = [re.sub(r"\n", "", l) for l in f.readlines()]

    with open("document-input.md", "r") as f:
        config = f.read()

    print(gen_document(config))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ChatGPT CLI - Document Generation")
    parser.add_argument("-i", "--input", metavar="input_file", help="The input file with the instructions")

    args = parser.parse_args()
    gen_document[args.command](**vars(args))
