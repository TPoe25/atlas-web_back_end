// 6-http_express.js

const express = require('express');

const app = express();
const port = 1245;

// Define the root route (/)
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Start the server
app.listen(port);

// Export the Express app for use in other files
module.exports = app;
