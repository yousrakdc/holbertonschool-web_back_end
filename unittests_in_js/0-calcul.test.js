const calculateNumber = require("./0-calcul");
const assert = require("assert");

describe("Sum two integers", function () {
  it("Must returns the sum of the two integers", function () {
    assert.strictEqual(calculateNumber(1, 1), 2);
  });
  it("muste return a rounded number", function () {
    assert.strictEqual(calculateNumber(1.1, 2.3), 3);
  });
  it("muste return a rounded number 2", function () {
    assert.strictEqual(calculateNumber(1.1, 2.1), 3);
  });
});