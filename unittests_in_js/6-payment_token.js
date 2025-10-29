// 6-payment_token.js
function generatePaymentTokenFromAPI(success) {
    if (success) {
        return Promise.resolve({ data: 'Successful response from the API' });
    }
    return Promise.reject(new Error('Failed to get token'));
}

module.exports = generatePaymentTokenFromAPI;
