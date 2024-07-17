/* eslint-disable */
import Currency from './3-currency.js';

export default class Pricing {
    constructor(amount, currency) {
        // Type verification
        if (typeof amount !== 'number') {
            throw new TypeError('Amount must be a number');
        }
        if (!(currency instanceof Currency)) {
            throw new TypeError('Currency must be an instance of Currency');
        }

        // Attribute assignment
        this._amount = amount;
        this._currency = currency;
    }

    // Getter and setter for amount
    get amount() {
        return this._amount;
    }

    set amount(newAmount) {
        if (typeof newAmount !== 'number') {
            throw new TypeError('Amount must be a number');
        }
        this._amount = newAmount;
    }

    // Getter and setter for currency
    get currency() {
        return this._currency;
    }

    set currency(newCurrency) {
        if (!(newCurrency instanceof Currency)) {
            throw new TypeError('Currency must be an instance of Currency');
        }
        this._currency = newCurrency;
    }

    // Method to display full price information
    displayFullPrice() {
        return `${this._amount} ${this._currency.name} (${this._currency.code})`;
    }

    // Static method to convert price based on conversion rate
    static convertPrice(amount, conversionRate) {
        if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
            throw new TypeError('Both amount and conversionRate must be numbers');
        }
        return amount * conversionRate;
    }
}