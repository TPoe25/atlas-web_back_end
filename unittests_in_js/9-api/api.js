// 8-api/api.js
// Import the required modules

const express = require('express');
const app = express();

// Define the index route
app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// Define the cart route
app.get('/cart/:id', (req, res) => {
  const { id } = req.params.id;
  res.send(`Payment methods for cart ${id}`);
});

if (require.main === module) {
  app.listen(7865, () => {
    console.log('API available on localhost port 7865');
  });
}

// Export the app for testing purposes
module.exports = app;
