from openai import OpenAI
from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv

import os

load_dotenv()
client = OpenAI(api_key=os.environ['OPENAI_KEY'])
app = Flask(__name__)

def analyze_contracts(contract1: str, contract2: str) -> str:
    prompt = (
        "I have two contracts. Please analyze these contracts and extract only the statements that "
        "directly contradict each other. do not add the statment if they do not fullly contradict or can mutually coexist\n\n"
        "Contract 1:\n"
        f"{contract1}\n\n"
        "Contract 2:\n"
        f"{contract2}\n\n"
        "Contradictory statements:"
    )

    response = client.chat.completions.create(model=os.environ['ACTIVE_MODEL'],
    messages= [      {
        "role": "system",
        "content": """You are a helpful assistant. your output is strictly in JSON format like this 
        [
        {
            "original": "[exact text from original contract]",
            "later": "[exact text from second contract]"
        }
        ]
        pls do not include backticks ```json """
      },{ "role": "user", "content":prompt }],
    max_tokens=1500,
    temperature=0.2,
    top_p=1.0,
    n=1,
    stop=None)

    return response.choices[0].message.content.strip()

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    contract1 = data.get('contract1', '')
    contract2 = data.get('contract2', '')

    if not contract1 or not contract2:
        return jsonify({"error": "Both contract1 and contract2 are required"}), 400

    contradictions = analyze_contracts(contract1, contract2)
    return jsonify(contradictions)

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True)
