#!/usr/bin/env node
'use strict';

const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber using Chai', () => {
    it('should round and SUM', function() {
        expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('should SUBTRACK work', () => {
        expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('should DIVIDE work', () => {
        expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.be.closeTo(0.2, 0.01);
    });

    it('should DIVIDE by 0 return Error', () => {
        expect(calculateNumber('DIVIDE', 1.4, 0,)).to.equal('Error');
    });
});
