// 9-api/api.js
// Import the required modules

const express = require('express');
const app = express();

// Define the index route
app.get("/", (req, res) => {
  res.send("Welcome to the payment system");
});

// Define the cart route
app.get("/cart/:id", (req, res) => {
  // const id = req.params.id;
  res.send(`Payment methods for cart ${req.params.id}`);
});

// Returns payment methods
app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false,
    },
  });
});

app.post('/login', (req, res) => {
    res.json
    const userName = req.body.userName;
    // console.log(`testing ${req.body}`);
    res.json(`Welcome ${req.body.userName}`);
});

if (require.main === module) {
  app.listen(7865, () => {
    console.log("API available on localhost port 7865");
  });
}

// Export the app for testing purposes
module.exports = app;
