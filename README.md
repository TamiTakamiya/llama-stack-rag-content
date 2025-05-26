# llama-stack-rag-content

## Setup

```commandline
git clone git@github.com:TamiTakamiya/llama-stack-rag-content.git
python3.11 -m venv .venv
source .venv/bin/activate
llama stack build --template remote-vllm --image-type venv --image-name .venv
SQLITE_STORE_DIR=./db python3.11 ./main.py
```

## References
- [Using Llama Stack as a Library](https://llama-stack.readthedocs.io/en/latest/distributions/importing_as_library.html)