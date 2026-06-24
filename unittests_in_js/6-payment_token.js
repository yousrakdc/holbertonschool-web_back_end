function getPaymentTokenFromAPI(success) {
    if (success) {
      return Promise.resolve({ data: 'Successful response from the API' });
    }
    // When success is false, do nothing (no return)
  }
  
  module.exports = getPaymentTokenFromAPI;
