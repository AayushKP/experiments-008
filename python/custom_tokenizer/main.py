import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Aayush Kashyap"
tokens = enc.encode(text)

# [25216, 3274, 0, 3673, 1308, 382, 355, 356, 1776, 68586, 88, 403]
print("Tokens", tokens)

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 355, 356, 1776, 68586, 88, 403])
print("decoded", decoded)
