// 8-api/api.test.js

const request = require("request");
const expect = require("chai");

describe('Index page', function () {
  it('should return status code 200 and correct message', function (done) {
    request.get('http://localhost:7865', function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});
