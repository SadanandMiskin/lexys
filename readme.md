# *LEXYS*
## Document Generation for legal assistance powered by GenAI using Python and NodeJS
*(Currently supports only accident related qureies and document generation)*
 
## Getting Started
- Download the required `content` folder -
 https://drive.google.com/drive/folders/1pTb6E8dQie36k7yZ_KkWPU7hYgMMezza?usp=sharing
- The project is divided in two parts
* Web - For web interfaces and server side rendering
* AIModel - For processing and documenting the data
........
## Working
![workflow](https://github.com/SadanandMiskin/lexys/assets/119523972/e06a4d07-af3c-434a-b755-2d6f1f4e7dde)



## AI model

### Doc Generation (*Getting Start*)
- `git clone https://github.com/SadanandMiskin/lexys`
-  paste the downloaded `/content` folder to `root` directory
-  Install All dependencies - `npm install` and `pip install torch torchvision torchaudio`
-  Create a `.env` file and add value for connecting to mongoDB
- Run the Application - `nodemon server.js`
- Open the application on `http://localhost:3000`
- Login and fill details and wait for some time for some magic.

### Chat Bot
- cd `AI_NLP_Model` 
- `python Chatbot_gui.py` only in `Google Colab` or `Jupyter Notebook` (requires `/content/output_2` model)

### Web
- Backend - `Nodejs , MongoDB, sessions`
- Frontend - `Html, Css, JavaScript`

### Features
- GPT2 - for generating texts
- nodejs - server for flow of data
- mongodb - database for storage

## Collaborators

- [Vaibhav V Vernekar](https://github.com/VaibahvVernekar27)
- [Sadanand Miskin](https://github.com/SadanandMiskin)
- [Apoorva](https://github.com/ApoorvaAppu12)
- [Kaushal S Boralkar](https://github.com/boralkarkaushal)
