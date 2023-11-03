import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "/content/output_2"  # Path to the directory where your trained model is saved
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def generate_legal_document():
    document = {}  # Initialize an empty dictionary to store document sections

    # Collect information from the user for different sections
    document['Title_Information'] = input("Enter title_information: ")
    document['Petitioner_Information'] = input("Enter petitioner_information: ")
    document['Respondent_Information'] = input("respondent_information: ")
    document['Accident_detail'] = input("Enter accident_detai: ")
    document['Description_of_deceased_and_accident_impact'] = input("Enter Description_of_deceased_and_accident_impact: ")
    document['Loss_and_compensation_claim'] = input("Enter Loss_and_compensation_claim: ")


    # Repeat the above line for other sections (Petitioner_Information, Respondent_Information, etc.)

    # Generate content for each section using the model
    for section, prompt in document.items():
        if prompt:
            generated_text = model.generate(
                input_ids=tokenizer.encode(prompt, return_tensors='pt'),
                max_length=500,  # Adjust the length as needed
                num_return_sequences=1,
                no_repeat_ngram_size=2,
                top_k=50,
                top_p=0.95,
            )
            generated_text = tokenizer.decode(generated_text[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
            document[section] = generated_text

    # Combine sections into the final document
    final_document = "\n\n".join([f"{section}:\n{content}" for section, content in document.items() if content])
    return final_document

# Generate a legal document based on user input
generated_document = generate_legal_document()
print(generated_document)
