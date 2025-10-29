// 4-payment.test.js

const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi with stub', () => {
  it('should use stub and log the correct total', function () {
    // Stub calculateNumber to always return 10
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
    // Spy on console.log
    const logSpy = sinon.spy(console, 'log');

    // Call the function being tested
    sendPaymentRequestToApi(5, 5);

    // Assert the stub was called once with correct args
    expect(stub.calledOnceWithExactly('SUM', 5, 5)).to.be.true;
    // Assert console.log was called with the stubbed result
    expect(logSpy.calledOnceWithExactly('The total is: 10')).to.be.true;

    // Restore stub and spy
    stub.restore();
    logSpy.restore();
  });
});
