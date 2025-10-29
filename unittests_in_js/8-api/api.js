// 8-api/api.js
// Import the required modules

const express = require('express');

const app = express();

// Define the index route
app.get('/', (req, res) => {
  res.status(200).send('Welcome to the payment system');
});

app.listen(7865, () => {
  console.log('API available on localhost port 7865');
});

module.exports = app;
