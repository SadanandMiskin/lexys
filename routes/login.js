const router = require('express').Router()
const bcrypt = require('bcrypt')
const userModel = require('../models/user')


router.get('/' ,(req,res)=>{
    res.render('login')
})

router.post('/' ,async (req,res)=>{
    try{
        const {email ,password} = req.body
        const finduser = await userModel.findOne({email})
        if(finduser){
          
          const passwordMatch = await bcrypt.compare(password, finduser.password)
          if(passwordMatch){
            req.session.allow = true
         return res.redirect(`/form?email=${email}`)
          }
          else{
            return res.redirect('/login')
          }
        }
        else{
         return res.redirect('/login')
        }
  
  
      }
    catch(err){
      console.log(err)
    }
})


module.exports = router