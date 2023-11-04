import gradio as gr
import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

model_name = "/content/output_2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = TFGPT2LMHeadModel.from_pretrained(model_name)

import gradio as gr

def generate_text(inp):
  input_ids = tokenizer.encode(inp, return_tensors='tf')
  beam_output = model.generate(input_ids,max_length=100,num_beams=5,no_repeat_ngram_size=2,early_stopping=True)
  output = tokenizer.decode(beam_output[0], skip_special_token=True,clean_up_tokenization_spaces=True)
  return ".".join(output.split(".")[:-1]) + "."

# Create a Gradio interface with text input and text output
iface = gr.Interface(
    fn=generate_text,
    inputs="text",
    outputs="text",
    title="GPT-2",
    description="Hello GPT2."
)

# Launch the Gradio interface
iface.launch()