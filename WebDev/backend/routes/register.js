const router = require('express').Router()
const bcrypt = require('bcrypt')
const userModel = require('../models/user')


let saltRounds = 10

router.get('/' , (req,res)=>{
    res.render('register')
})

router.post('/' ,async (req,res)=>{
    try{
        const {name ,email,password} = req.body
       const newuser =  await userModel.findOne({email})
       if(newuser){
         return res.redirect('/register')
       }
       bcrypt.hash(password, saltRounds).then(async function (hash) {
        const newUser = new userModel({
          name: name,
          email: email,
          password: hash
        })
        await newUser.save()
        console.log('user saved')
        res.redirect('/login')
      })
       
      }
      catch(err){
        console.log(err)
      }
})

module.exports = router