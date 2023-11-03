const router = require('express').Router()
const Auth = require('../scripts/auth')
router.get('/' , Auth , (req,res)=>{
res.json({hi: 'hi'})
})
module.exports = router