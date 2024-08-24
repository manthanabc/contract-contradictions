# Contract Compliance App

## what?
Using LLMs to SPOT contradictions in given contracts

## using
Flask, openai, HTML, CSS, JS

## how?
Current implementation uses one shot prompting via gpt-4o or gpt-4o-mini

```bash
git clone github.com/manthanabc/contract-contradictions cc
cd cc
pip install -r requirements.txt
python app.py
```

## Roadmap

- Data preprocessing
- SFT with gpt-4o
- Introduce RAG
- Support for fileuploads via pdf
- Add support for lama 3.1
- Benchmarking and evaluations
