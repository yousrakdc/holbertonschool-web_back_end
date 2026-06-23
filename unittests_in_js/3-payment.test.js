const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function() {
  it('should call Utils.calculateNumber with SUM, 100, and 20', function() {
    // Create a spy on Utils.calculateNumber
    const spy = sinon.spy(Utils, 'calculateNumber');

    // Call the function we're testing
    sendPaymentRequestToApi(100, 20);

    // Verify the spy was called with the correct arguments
    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith('SUM', 100, 20)).to.be.true;

    // Restore the spy
    spy.restore();
  });

  it('should log the correct message to the console', function() {
    // Create a spy on console.log
    const consoleSpy = sinon.spy(console, 'log');

    // Call the function
    sendPaymentRequestToApi(100, 20);

    // Verify console.log was called with the correct message
    expect(consoleSpy.calledOnce).to.be.true;
    expect(consoleSpy.calledWith('The total is: 120')).to.be.true;

    // Restore the spy
    consoleSpy.restore();
  });

  it('should use the result from Utils.calculateNumber', function() {
    // Create a spy on Utils.calculateNumber
    const spy = sinon.spy(Utils, 'calculateNumber');

    // Call the function with different values
    sendPaymentRequestToApi(50, 30);

    // Verify the spy was called correctly
    expect(spy.calledOnce).to.be.true;
    expect(spy.returned(80)).to.be.true;

    // Restore the spy
    spy.restore();
  });
});
