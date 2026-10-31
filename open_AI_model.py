
from transformers import AutoTokenizer, AutoModelForCausalLM

models = {
    "GPT-2": "openai-community/gpt2",
    "DistilGPT-2": "distilbert/distilgpt2"
}

for name, model_name in models.items():
    print(f"\nDownloading {name}...")

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    print(f"{name} downloaded successfully!")

print("\nAll models are ready.")
