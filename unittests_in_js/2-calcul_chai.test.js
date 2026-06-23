const calculateNumber = require("./1-calcul");
const chai = require("chai");
const expect = chai.expect;

describe("calculateNumber", function () {
    describe("SUM", function () {
      it("should return the sum of two rounded integers", function () {
        expect(calculateNumber('SUM', 1, 1)).to.equal(2);
      });
      it("should return the sum of two rounded decimals", function () {
        expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
      });
      it("should return the sum of two rounded decimals 2", function () {
        expect(calculateNumber('SUM', 1.1, 2.3)).to.equal(3);
      });
      it("should handle negative numbers", function () {
        expect(calculateNumber('SUM', -1.4, -2.3)).to.equal(-3);
      });
      it("should handle zero", function () {
        expect(calculateNumber('SUM', 0, 0)).to.equal(0);
      });
      it("should handle large numbers", function () {
        expect(calculateNumber('SUM', 1000.5, 2000.6)).to.equal(3002);
      });
    });
  
    describe("SUBTRACT", function () {
      it("should return the difference of two rounded integers", function () {
        expect(calculateNumber('SUBTRACT', 5, 2)).to.equal(3);
      });
      it("should return the difference of two rounded decimals", function () {
        expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
      });
      it("should handle negative result", function () {
        expect(calculateNumber('SUBTRACT', 2.1, 5.6)).to.equal(-4);
      });
      it("should handle zero", function () {
        expect(calculateNumber('SUBTRACT', 5.4, 5.4)).to.equal(0);
      });
      it("should handle negative numbers", function () {
        expect(calculateNumber('SUBTRACT', -1.4, -2.3)).to.equal(1);
      });
    });
  
    describe("DIVIDE", function () {
      it("should return the quotient of two rounded numbers", function () {
        expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
      });
      it("should return Error when divisor rounds to zero", function () {
        expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
      });
      it("should return Error when divisor rounds to zero (0.4)", function () {
        expect(calculateNumber('DIVIDE', 10, 0.4)).to.equal('Error');
      });
      it("should handle division of integers", function () {
        expect(calculateNumber('DIVIDE', 10, 2)).to.equal(5);
      });
      it("should handle decimal results", function () {
        expect(calculateNumber('DIVIDE', 10, 3)).to.equal(3.3333333333333335);
      });
      it("should handle negative numbers", function () {
        expect(calculateNumber('DIVIDE', -10, 2)).to.equal(-5);
      });
      it("should handle division by one", function () {
        expect(calculateNumber('DIVIDE', 5.6, 1.2)).to.equal(6);
      });
    });
  });
