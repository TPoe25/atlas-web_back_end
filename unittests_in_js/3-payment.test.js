// 3-payment.test.js

const sinon = require("sinon");
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./3-payment");

describe('sendPaymentRequestToApi', function () {
  it('logs the correct message', function () {
    // Spy on Utils.calculateNumber
    const logSpy = sinon.spy(console, 'log');

    // Call the function being tested
    sendPaymentRequestToApi(100, 20);

    // Check that the spy was called with the correct args
    if (!logSpy.calledWithExactly('The total is: 120')) {
        console.log('Expected console log did not match');
    }

    // Restore the spy
    logSpy.restore();
  });
});
