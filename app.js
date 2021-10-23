const express = require('express')
const path = require('path')
const app = express()
const port = process.env.PORT || 4005
app.get(['/', 'index.html'], function (req, res) {
  res.sendFile(path.resolve('index.html'))
})

app.post('/verify', function (req, res) {

})

app.get(['/account.html', '/account'], function (req, res) {
  res.sendFile(path.resolve('account.html'))
})

app.use(express.static(__dirname))

app.listen(port, function () {
  console.log('App listening on port:', port)
})
