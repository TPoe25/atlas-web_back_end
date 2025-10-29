// 3-payment.test.js

const sinon = require("sinon");
const { expect } = require("chai");
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./3-payment");

describe('sendPaymentRequestToApi', function () {
  it('should call Utils.calculateNumber with correct arguments', function () {
    // Spy on Utils.calculateNumber
    const spy = sinon.spy(Utils, 'calculateNumber');

    // Call the function being tested
    sendPaymentRequestToApi(100, 20);

    // Check that the spy was called with the correct args
    expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;

    // Restore the spy
    spy.restore();
  });
});
