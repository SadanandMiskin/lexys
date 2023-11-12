# LEXYS 
## Document Genneration for legal assistance using GenAI using Python and NodeJS

## Getting Started
* Download the required folder `content` which is a AI model - https://drive.google.com/drive/folders/1pTb6E8dQie36k7yZ_KkWPU7hYgMMezza?usp=sharing
- The project is divided in two parts
* Web - For frontend and server side rendering.
* AIModel - For processing and documenting the data

## Working
![workflow](https://github.com/SadanandMiskin/lexys/assets/119523972/c0123166-58a7-4ac7-a62f-39301cf2b551)



## AI model

### Text Generation
- `git clone https://github.com/SadanandMiskin/lexys`
-  cd `AI_NLP_Model` folder
-  paste the downloaded `content` folder to `root` directory
-  `npm i` and `pip install torch torchvision torchaudio`
-  create `.env` file and add `MONGO_URI` variable with value
- `python generate_legal_document.py `(requires AI model from `content/output_2` folder)
- `nodemon server.js`
- Run the Application on `http://localhost:3000`

### Chat Bot
- cd `AI_NLP_Model` 
- `python Chatbot_gui.py` -> IN `JUPYTER NOTEBOOK` OR  `GOOGLE COLAB` (requires `content/output_2` model)

### Web
- Backend - `Nodejs , MongoDB`
- Frontend - `html, css, js`

### Features
- GPT2 - for generating texts
- nodejs - server for ensuring data flow
- mongodb - for storing data
