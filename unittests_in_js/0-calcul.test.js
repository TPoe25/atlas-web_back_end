// 0-calcul.test.js
// using Node's built-in 'assert' module for testing
const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
    it('should return 4 when given (1, 3)', () => {
        assert.strictEqual(calculateNumber(1, 3), 4);
    });

    it('should round second number up and return 5 for (1, 3.7)', () => {
        assert.strictEqual(calculateNumber(1, 3.7), 5);
    });

    it('should round both numbers and return 5 for (1.2, 3.7)', () => {
        assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });

    it('should round both numbers up and return 6 for (1.5, 3.7)', () => {
        assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });
});
