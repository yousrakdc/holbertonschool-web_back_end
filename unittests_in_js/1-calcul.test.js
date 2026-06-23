const calculateNumber = require("./1-calcul");
const assert = require("assert");

describe("calculateNumber", function () {
  describe("SUM", function () {
    it("should return the sum of two rounded integers", function () {
      assert.strictEqual(calculateNumber('SUM', 1, 1), 2);
    });
    it("should return the sum of two rounded decimals", function () {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });
    it("should return the sum of two rounded decimals 2", function () {
      assert.strictEqual(calculateNumber('SUM', 1.1, 2.3), 3);
    });
    it("should handle negative numbers", function () {
      assert.strictEqual(calculateNumber('SUM', -1.4, -2.3), -3);
    });
    it("should handle zero", function () {
      assert.strictEqual(calculateNumber('SUM', 0, 0), 0);
    });
    it("should handle large numbers", function () {
      assert.strictEqual(calculateNumber('SUM', 1000.5, 2000.6), 3002);
    });
  });

  describe("SUBTRACT", function () {
    it("should return the difference of two rounded integers", function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 5, 2), 3);
    });
    it("should return the difference of two rounded decimals", function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
    it("should handle negative result", function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 2.1, 5.6), -4);
    });
    it("should handle zero", function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 5.4, 5.4), 0);
    });
    it("should handle negative numbers", function () {
      assert.strictEqual(calculateNumber('SUBTRACT', -1.4, -2.3), 1);
    });
  });

  describe("DIVIDE", function () {
    it("should return the quotient of two rounded numbers", function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });
    it("should return Error when divisor rounds to zero", function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
    it("should return Error when divisor rounds to zero (0.4)", function () {
      assert.strictEqual(calculateNumber('DIVIDE', 10, 0.4), 'Error');
    });
    it("should handle division of integers", function () {
      assert.strictEqual(calculateNumber('DIVIDE', 10, 2), 5);
    });
    it("should handle decimal results", function () {
      assert.strictEqual(calculateNumber('DIVIDE', 10, 3), 3.3333333333333335);
    });
    it("should handle negative numbers", function () {
      assert.strictEqual(calculateNumber('DIVIDE', -10, 2), -5);
    });
    it("should handle division by one", function () {
      assert.strictEqual(calculateNumber('DIVIDE', 5.6, 1.2), 6);
    });
  });
});
