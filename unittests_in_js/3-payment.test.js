// 3-payment.test.js

const sinon = require("sinon");
const { expect } = require("chai");
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./3-payment");

describe('sendPaymentRequestToApi', function () {
  it('should call Utils.calculateNumber with correct arguments', function () {
    const spy = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;

    spy.restore();
  });

  it('logs the correct message', function () {
    const logSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    expect(logSpy.calledOnceWithExactly("The total is: 120")).to.be.true;

    logSpy.restore();
  });
});
