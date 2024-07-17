/* eslint-disable */
export default class Airport {
    constructor(name, code) {
        if (typeof name !== 'string' || typeof code !== 'string') {
            throw new TypeError('Name and code must be strings');
        }

        this._name = name;
        this._code = code;
    }

    // Getter for name
    get name() {
        return this._name;
    }

    // Getter for code
    get code() {
        return this._code;
    }

    // Custom toString method
    toString() {
        return this._code;
    }

    // Customizing the toStringTag property
    get [Symbol.toStringTag]() {
        return this._code;
    }
}