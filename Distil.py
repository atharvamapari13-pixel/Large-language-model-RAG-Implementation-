
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "distilbert/distilgpt2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

text = "Artificial intelligence is"

# Convert text into token IDs
inputs = tokenizer(text, return_tensors="pt")
print("Token IDs:", inputs["input_ids"])

# Generate text
outputs = model.generate(
    **inputs,
    max_new_tokens=20,
    do_sample=False,
    pad_token_id=tokenizer.eos_token_id
)

print("Generated text:")
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
