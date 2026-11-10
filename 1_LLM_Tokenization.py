from transformers import AutoTokenizer

# Load pretrained tokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")

# Input Sentance
sentance = " I Love AI"

# Convert the sentance into tokens
tokens = tokenizer.tokenize(sentance)

token_ids = tokenizer.encode(
    sentance,
    add_special_tokens = False
)

# Convert token ids back to next
decoded = tokenizer.decode(token_ids)

print("Original Sentance :",sentance)

print("Tokens:", tokens)

print("Token IDs:",token_ids)

print("Decoded Sentances:",decoded)