const mongoose = require('mongoose')

const dataSchema = mongoose.Schema({
   
    email: String,
    data: String
   
},
{ collection: 'lexysData' })

const dataModel = mongoose.model('dataSchema' , dataSchema)
module.exports = dataModel