// 8-api/api.js
// Import the required modules

const express = require('express');
const app = express();
const port = 7865;

// Define the index route
app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// Define the cart route
app.get('/cart/:id', (req, res) => {
  const id = req.params.id;

  if (!/^\d+$/.test(id)) {
    return res.status(404).send(`Cannot GET /cart/${id}`);
    }

    res.send(`Payment methods for cart ${id}`);
});

// Start the server
app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

// Export the app for testing purposes
module.exports = app;
