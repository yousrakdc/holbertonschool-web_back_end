const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function() {
  it('should return a successful response when success is true', function(done) {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        // Verify the response structure
        expect(response).to.be.an('object');
        expect(response).to.have.property('data');
        expect(response.data).to.equal('Successful response from the API');
        done();
      })
      .catch((error) => {
        // If there's an error, pass it to done()
        done(error);
      });
  });
});
