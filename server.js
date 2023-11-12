//Jai Shree Ram
const main = require('./routes/main')
const register = require('./routes/register')
const login = require('./routes/login')
const dashboard = require('./routes/dashboard')
const form = require('./routes/form')
require('./config/db')

const express = require('express')
const mongoose = require('mongoose')
const path = require('path');
const { spawn } = require('child_process');
const bodyParser = require('body-parser');
const session = require('express-session')
const app = express()

app.use(session({
    secret: 'lexmachinamachinalex',
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false }
  }))

 


app.use(express.static(__dirname + '/public/'))
app.set('view engine', 'ejs')
app.set('views' ,path.join(__dirname, 'views'))
app.use(bodyParser.urlencoded({ extended: true }));

app.use('/', main)
app.use('/register', register)
app.use('/login' , login)
app.use('/dashboard' , dashboard)
app.use('/form' , form)


app.listen(3000, ()=>{
    console.log('Server listening')
})