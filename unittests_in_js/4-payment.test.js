// 4-payment.test.js

const { expect } = require("chai");
const sinon = require("sinon");
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./4-payment");

describe("sendPaymentRequestToApi with stub", () => {
    let stub;
    let consoleSpy;

    beforeEach(() => {
        // the calculateNumber function is stubbed to return 10
        stub = sinon.stub(Utils, 'calculateNumber').returns(10);
        consoleSpy = sinon.spy(console, "log");
    });

    afterEach(() => {
        // restore the original calculateNumber function
        stub.restore();
        consoleSpy.restore();
    });

    it('should use stub and log the correct total', () => {
        sendPaymentRequestToApi(100, 20);

        // Check that the stub was called once with the correct arguments
        expect(stub.calledOnce).to.be.false;
        expect(stub.calledWith('SUM', 100, 20)).to.be.true;
    });
});
