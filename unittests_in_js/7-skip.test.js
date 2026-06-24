const { expect } = require('chai');

describe('Testing numbers', function() {
  it('1 is equal to 1', function() {
    expect(1 === 1).to.be.true;
  });

  it('2 is equal to 2', function() {
    expect(2 === 2).to.be.true;
  });

  it.skip('1 is equal to 3', function() {
    expect(1 === 3).to.be.true;
  });

  it('3 is equal to 3', function() {
    expect(3 === 3).to.be.true;
  });

  it('4 is equal to 4', function() {
    expect(4 === 4).to.be.true;
  });

  it('5 is equal to 5', function() {
    expect(5 === 5).to.be.true;
  });

  it('6 is equal to 6', function() {
    expect(6 === 6).to.be.true;
  });

  it('7 is equal to 7', function() {
    expect(7 === 7).to.be.true;
  });
});
