const router = require('express').Router()
const path = require('path');
const { spawn } = require('child_process');
const bodyParser = require('body-parser');
const session = require('express-session')
const dataModel = require('../models/data')


const Auth = require('../scripts/auth')

let em= ''
router.get('/'  , (req,res)=>{
em = req.query.email
res.render('form' ,{em: em})
})


router.post('/', (req, res) => {
  const {
    Enter_title_information,
    Enter_petitioner_information,
    respondent_information,
    Enter_accident_detai,
    Enter_Description_of_deceased_and_accident_impact,
    Enter_Loss_and_compensation_claim
  } = req.body;

  const pythonProcess = spawn('python', ['generate_legal_document.py']);
  
  // Prepare the input data in JSON format
  const inputData = JSON.stringify({
    Title_Information: Enter_title_information,
    Petitioner_Information: Enter_petitioner_information,
    Respondent_Information: respondent_information,
    Accident_detail: Enter_accident_detai,
    Description_of_deceased_and_accident_impact: Enter_Description_of_deceased_and_accident_impact,
    Loss_and_compensation_claim: Enter_Loss_and_compensation_claim
  });

  req.session.input = JSON.parse(inputData)
  console.log(JSON.parse(inputData))

  pythonProcess.stdin.write(inputData);
  pythonProcess.stdin.end();

  let outputData = '';

  pythonProcess.stdout.on('data', (data) => {
    outputData += data.toString();
  });

  pythonProcess.on('close',async () => {
    // res.send(outputData);
    // console.log(outputData)

    try{
        // const newData = new dataModel({
        //     email: em,
        //     data: outputData
        // })
        // await newData.save()
        req.session.data=outputData
        console.log(outputData)
        console.log(em)
        
        res.redirect(`/dashboard?email=${em}`)
    }
    catch(err){
        console.log(err)
    }
  });
});



module.exports = router



