const sinon = require("sinon");
const sendPaymentRequestToApi = require("./4-payment");
const Utils = require("./utils");
const assert = require("assert");

describe("Send payment Request to Api", function () {
  it("should stub Utils.calculateNumber and spy on console.log", function () {
    const stub = sinon.stub(Utils, "calculateNumber").returns(10);

    const spy = sinon.spy(console, "log");

    sendPaymentRequestToApi(100, 20);

    assert(stub.calledOnceWithExactly("SUM", 100, 20));

    assert(spy.calledOnceWithExactly("The total is: 10"));

    stub.restore();

    spy.restore();
  });
});
