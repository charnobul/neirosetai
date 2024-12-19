from transformers import GPT2LMHeadModel, GPT2Tokenizer

class ChatBot:
    def __init__(self):
        self.model_name = "gpt2"
        self.model = GPT2LMHeadModel.from_pretrained(self.model_name)
        self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_name)
        self.history = []

    def generate_response(self, user_input):
        self.history.append(user_input)
        input_ids = self.tokenizer.encode(" ".join(self.history), return_tensors="pt")
        output = self.model.generate(input_ids, max_length=1000, pad_token_id=self.tokenizer.eos_token_id)
        response = self.tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
        self.history.append(response)
        return response
