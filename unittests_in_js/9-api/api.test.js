const request = require('request');
const { expect } = require('chai');

describe('Index page', function() {
  const baseUrl = 'http://localhost:7865';

  it('should return status code 200', function(done) {
    request.get(baseUrl, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct message', function(done) {
    request.get(baseUrl, (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('should have correct content-type', function(done) {
    request.get(baseUrl, (error, response, body) => {
      expect(response.headers['content-type']).to.include('text/html');
      done();
    });
  });
});

describe('Cart page', function() {
  const baseUrl = 'http://localhost:7865';

  it('should return status code 200 when :id is a number', function(done) {
    request.get(`${baseUrl}/cart/12`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct message when :id is a number', function(done) {
    request.get(`${baseUrl}/cart/12`, (error, response, body) => {
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('should return status code 404 when :id is NOT a number', function(done) {
    request.get(`${baseUrl}/cart/hello`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should return status code 200 for different valid cart ids', function(done) {
    request.get(`${baseUrl}/cart/123`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 123');
      done();
    });
  });

  it('should return status code 200 for single digit id', function(done) {
    request.get(`${baseUrl}/cart/5`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 5');
      done();
    });
  });

  it('should return status code 404 when :id contains letters', function(done) {
    request.get(`${baseUrl}/cart/abc`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should return status code 404 when :id is alphanumeric', function(done) {
    request.get(`${baseUrl}/cart/12ab`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should return status code 404 when :id contains special characters', function(done) {
    request.get(`${baseUrl}/cart/12-34`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should return status code 404 when :id is a string', function(done) {
    request.get(`${baseUrl}/cart/test`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should handle large cart ids', function(done) {
    request.get(`${baseUrl}/cart/999999`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 999999');
      done();
    });
  });

  it('should return correct message format for any valid id', function(done) {
    request.get(`${baseUrl}/cart/42`, (error, response, body) => {
      expect(body).to.match(/^Payment methods for cart \d+$/);
      done();
    });
  });

  it('should have correct content-type for cart endpoint', function(done) {
    request.get(`${baseUrl}/cart/12`, (error, response, body) => {
      expect(response.headers['content-type']).to.include('text/html');
      done();
    });
  });

  it('should not accept negative numbers as id', function(done) {
    request.get(`${baseUrl}/cart/-12`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should not accept decimal numbers as id', function(done) {
    request.get(`${baseUrl}/cart/12.5`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should handle zero as cart id', function(done) {
    request.get(`${baseUrl}/cart/0`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 0');
      done();
    });
  });
});