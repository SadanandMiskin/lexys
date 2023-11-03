const Auth = (req,res,next) =>{
    if(req.session.allow){
        next()
    }
    res.redirect('/login')
}

module.exports = Auth