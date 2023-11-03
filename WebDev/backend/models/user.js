const mongoose = require('mongoose')

const userSchema = mongoose.Schema({
    username: String,
    email: String,
    password: String,
   
},
{ collection: 'lexysUsers' })

const userModel = mongoose.model('userSchema' , userSchema)
module.exports = userModel