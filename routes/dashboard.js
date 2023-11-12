const router = require('express').Router();
const Auth = require('../scripts/auth');
const dataModel = require('../models/data');

router.get('/',Auth , async (req, res) => {
  const email = req.query.email;
  console.log(email);

  try {
    // const outputData = await dataModel.find({ email });
    const outputData= req.session.data
    console.log(outputData);

    // Remove unnecessary characters and escape sequences from the string
    let cleanedData = outputData.replace(/(\w+)_and_(\w+)/g, '$1_$2')
    .replace(/n{2,}/g, '}, {')
    .replace(/n{2,}/g, '}, {')
    .replace(/n{2,}/g, '}, {')
    .replace(/(\w+)_{2,}/g, '$1":"')
    .replace(/_{2,}/g, '":"')
    .replace(/"(\w+)_":/g, '"$1":')
    .replace(/n+/g, '')
    .replace(/"\s*:\s*"/g, '": "');
  
  console.log(cleanedData);
    // Add any other necessary cleaning steps...

    // Attempt to parse the cleaned string into a JavaScript object
    // let parsedData;
    try {
      // parsedData = JSON.parse(cleanData);
      // res.render(cleanedData)
      const start = Math.floor(Math.random() * cleanedData.length)
      const end = Math.floor(Math.random() * (cleanedData.length - start)) + start
      const accidentString = cleanedData.substring(start ,end)

      const start3 = Math.floor(Math.random() * cleanedData.length)
      const end3 = Math.floor(Math.random() * (cleanedData.length - start3)) + start3*start
      const impactString = cleanedData.substring(start3 ,end3)


      const start2 = Math.floor(Math.random() * cleanedData.length)
      const end2 = Math.floor(Math.random() * (cleanedData.length - start2)) + start2*start
      const compensationString = cleanedData.substring(start2 ,end2)
      res.render('document' ,{input: req.session.input, accidentDetails: accidentString ,impact:impactString, compensation: compensationString})
    } 
    catch (error) {
      console.error("Error parsing JSON:", error);
      res.status(500).send("Error parsing JSON data");
      
    }

    // Accessing a specific field (Title_Information in this case)
  //   if (parsedData && parsedData.Title_Information) {
  //     res.send(parsedData.Title_Information);
  //   } else {
  //     res.status(404).send('Title_Information not found');
  //   }
  } catch (err) {
    console.log(err);
    res.status(500).send('Internal Server Error');
  }
});

module.exports = router;
