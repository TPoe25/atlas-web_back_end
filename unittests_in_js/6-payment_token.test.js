// 6-payment_token.test.js

const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function () {
    it('should resolve with data when success is true', function (done) {
        getPaymentTokenFromAPI(true)
            .then((response) => {
                expect(response).to.deep.equal({ data: 'Successful response from the API' });
                done();
            })
            .catch(done);
    });

    it('should reject success is false', function (done) {
        getPaymentTokenFromAPI(false)
            .then(() => done(new Error('Promise should not resolve')))
            .catch((error) => {
                expect(error).to.be.an('error');
                done();
            });
    });
});
