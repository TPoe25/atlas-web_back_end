// 5-payment.test.js

const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi with hooks', () => {
    let consoleSpy;

    beforeEach(() => {
        // spy.console.log before each test
        consoleSpy = sinon.spy(console, 'log');
    });

    afterEach(() => {
        // restore console.log after each test
        consoleSpy.restore();
    });

    it('should log the total for 100 + 20', () => {
        sendPaymentRequestToApi(100, 20);
        expect(consoleSpy.called).to.be.true;
        expect(consoleSpy.calledWith('The total is: 120')).to.be.true;
    });

    it('should log the total for 10 + 10', () => {
        sendPaymentRequestToApi(10, 10);
        expect(consoleSpy.called).to.be.true;
        expect(consoleSpy.calledWith('The total is: 20')).to.be.true;
    });
});
