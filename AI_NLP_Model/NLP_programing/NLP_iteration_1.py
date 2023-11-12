import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments

model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)


dataset = TextDataset(
    tokenizer=tokenizer,
    file_path="/content/data_nlp.txt",
    block_size=128,
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False,
)


training_args = TrainingArguments(
    output_dir="./output_1",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=8,
    save_steps=10_000,
    save_total_limit=2,
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)

trainer.train()

trainer.save_model()

fine_tuned_model = GPT2LMHeadModel.from_pretrained("/content/output_1")  # Replace with your fine-tuned model directory


fine_tuned_model.eval()


prompt =  """Accecident Details 
"""


generated_text = fine_tuned_model.generate(input_ids=tokenizer.encode(prompt, return_tensors='pt'), max_length=1000, num_return_sequences=1, no_repeat_ngram_size=2)


generated_text = tokenizer.decode(generated_text[0], skip_special_tokens=True)
print(generated_text)
