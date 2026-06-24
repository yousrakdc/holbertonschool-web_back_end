const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', function() {
  let consoleSpy;

  // Hook: executed before each test
  beforeEach(function() {
    // Create a spy on console.log before each test
    consoleSpy = sinon.spy(console, 'log');
  });

  // Hook: executed after each test
  afterEach(function() {
    // Restore the spy after each test
    consoleSpy.restore();
  });

  it('should log "The total is: 120" when called with 100 and 20', function() {
    // Call the function
    sendPaymentRequestToApi(100, 20);

    // Verify console.log was called once
    expect(consoleSpy.calledOnce).to.be.true;

    // Verify console.log was called with the correct message
    expect(consoleSpy.calledWith('The total is: 120')).to.be.true;
  });

  it('should log "The total is: 20" when called with 10 and 10', function() {
    // Call the function
    sendPaymentRequestToApi(10, 10);

    // Verify console.log was called once
    expect(consoleSpy.calledOnce).to.be.true;

    // Verify console.log was called with the correct message
    expect(consoleSpy.calledWith('The total is: 20')).to.be.true;
  });
});
