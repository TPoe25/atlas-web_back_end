// 3-payment.js
// Function that simulates a payment request using Utils.calculateNumber

const Utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const total = Utils.calculateNumber('SUM', totalAmount, totalShipping);
  return `The total is: ${total}`;
}

module.exports = sendPaymentRequestToApi;
