# import sys
# import json
# import torch
# from transformers import GPT2LMHeadModel, GPT2Tokenizer

# model_name = "C:/Users/DELL/Desktop/lexys/content/output_2"
#   # Path to the directory where your trained model is saved
# model = GPT2LMHeadModel.from_pretrained(model_name)
# tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# def generate_legal_document(data):
#     try:
#         document = json.loads(data)
        
#         # Rest of your code to process the document...

#         final_document = "\n\n".join(
#             [f"{section}:\n{content}" for section, content in document.items() if content])
#         return final_document

#     except Exception as e:
#         print(f"Error processing data: {e}")
#         sys.exit(1)

# # Receive data from Node.js
# input_data = sys.stdin.read()

# try:
#     generated_document = generate_legal_document(input_data)
#     print(generated_document)

# except Exception as e:
#     print(f"Error generating document: {e}")
#     sys.exit(1)



# -------------------------------------------------------------------------------- -4oee-e--e-------------------------------------
# import torch
# from transformers import GPT2LMHeadModel, GPT2Tokenizer

# model_name = "C:/Users/DELL/Desktop/lexys/content/output_2"
#   # Path to the directory where your trained model is saved
# model = GPT2LMHeadModel.from_pretrained(model_name)
# tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# def generate_legal_document():
#     document = {}  # Initialize an empty dictionary to store document sections

#     # Collect information from the user for different sections
#     document['Title_Information'] = input("Enter title_information: ")
#     document['Petitioner_Information'] = input("Enter petitioner_information: ")
#     document['Respondent_Information'] = input("respondent_information: ")
#     document['Accident_detail'] = input("Enter accident_detai: ")
#     document['Description_of_deceased_and_accident_impact'] = input("Enter Description_of_deceased_and_accident_impact: ")
#     document['Loss_and_compensation_claim'] = input("Enter Loss_and_compensation_claim: ")


#     # Repeat the above line for other sections (Petitioner_Information, Respondent_Information, etc.)

#     # Generate content for each section using the model
#     for section, prompt in document.items():
#         if prompt:
#             generated_text = model.generate(
#                 input_ids=tokenizer.encode(prompt, return_tensors='pt'),
#                 max_length=500,  # Adjust the length as needed
#                 num_return_sequences=1,
#                 no_repeat_ngram_size=2,
#                 top_k=50,
#                 top_p=0.95,
#             )
#             generated_text = tokenizer.decode(generated_text[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
#             document[section] = generated_text

#     # Combine sections into the final document
#     final_document = "\n\n".join([f"{section}:\n{content}" for section, content in document.items() if content])
#     return final_document

# # Generate a legal document based on user input
# generated_document = generate_legal_document()
# print(generated_document)



# import sys
# import json
# from transformers import GPT2LMHeadModel, GPT2Tokenizer

# model_name = "C:/Users/DELL/Desktop/lexys/content/output_2"
# model = GPT2LMHeadModel.from_pretrained(model_name)
# tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# def generate_legal_document(data):
#     try:
#         document = json.loads(data)
        
#         for section, prompt in document.items():
#             if prompt:
#                 generated_text = model.generate(
#                     input_ids=tokenizer.encode(prompt, return_tensors='pt'),
#                     max_length=500,  # Adjust the length as needed
#                     num_return_sequences=1,
#                     no_repeat_ngram_size=2,
#                     top_k=50,
#                     top_p=0.95,
#                 )
#                 generated_text = tokenizer.decode(generated_text[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
#                 document[section] = generated_text

#         final_document = "\n\n".join([f"{section}:\n{content}" for section, content in document.items() if content])
#         return final_document

#     except Exception as e:
#         print(f"Error processing data: {e}")
#         sys.exit(1)

# # Receive data from Node.js
# input_data = sys.stdin.read()

# try:
#     generated_document = generate_legal_document(input_data)
#     print(generated_document)

# except Exception as e:
#     print(f"Error generating document: {e}")
#     sys.exit(1)





# import sys
# import json
# from transformers import GPT2LMHeadModel, GPT2Tokenizer

# def generate_legal_document(data):
#     try:
#         model_name = "C:\\Users\\DELL\\Desktop\\lexys\\content\\output_2"  # Update with your model path
#         model = GPT2LMHeadModel.from_pretrained(model_name)
#         tokenizer = GPT2Tokenizer.from_pretrained(model_name)

#         document = json.loads(data)
        
#         for section, prompt in document.items():
#             if prompt:
#                 generated_text = model.generate(
#                     input_ids=tokenizer.encode(prompt, return_tensors='pt'),
#                     max_length=500,  # Adjust the length as needed
#                     num_return_sequences=1,
#                     no_repeat_ngram_size=2,
#                     top_k=50,
#                     top_p=0.95,
#                 )
#                 generated_text = tokenizer.decode(generated_text[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
#                 document[section] = generated_text

#         final_document = "\n\n".join([f"{section}:\n{content}" for section, content in document.items() if content])
#         return final_document

#     except Exception as e:
#         return f"Error processing data: {e}"

# # Receive data from Node.js
# input_data = sys.stdin.read()

# try:
#     generated_document = generate_legal_document(input_data)
#     print(generated_document)

# except Exception as e:
#     print(f"Error generating document: {e}")





# import sys
# import json
# from transformers import GPT2LMHeadModel, GPT2Tokenizer

# model_name = "C:/Users/DELL/Desktop/lexys/content/output_2"  # Path to the directory where your trained model is saved
# model = GPT2LMHeadModel.from_pretrained(model_name)
# tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# def generate_legal_document(data):
#     try:
#         document = json.loads(data)
        
#         for section, prompt in document.items():
#             if prompt:
#                 generated_text = model.generate(
#                     input_ids=tokenizer.encode(prompt, return_tensors='pt'),
#                     max_length=500,  # Adjust the length as needed
#                     num_return_sequences=1,
#                     no_repeat_ngram_size=2,
#                     top_k=50,
#                     top_p=0.95,
#                 )
#                 generated_text = tokenizer.decode(generated_text[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
#                 document[section] = generated_text

#         # return json.dumps(document, indent=2)  # Return the document as a properly formatted JSON
        


#     except Exception as e:
#         return f"Error processing data: {e}"

# # Receive data from Node.js
# input_data = sys.stdin.read()

# try:
#     generated_document = generate_legal_document(input_data)
#     print(generated_document)

# except Exception as e:
#     print(f"Error generating document: {e}")





import sys
import json
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "C:/Users/DELL/Desktop/lexys/content/output_2"  # Path to the directory where your trained model is saved
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def generate_legal_document(data):
    try:
        document = json.loads(data)
        
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

        # Convert dictionary to a JSON-formatted string with ensure_ascii=False to prevent escaping characters
        generated_json = json.dumps(document, ensure_ascii=False, indent=2)

        # Replace unwanted escape sequences
        generated_json = generated_json.replace("\\", "").replace("\n", "").replace("\r", "").replace("\\", "")

        return generated_json

    except Exception as e:
        return f"Error processing data: {e}"

# Receive data from Node.js
input_data = sys.stdin.read()

try:
    generated_document = generate_legal_document(input_data)
    print(generated_document)

except Exception as e:
    print(f"Error generating document: {e}")
