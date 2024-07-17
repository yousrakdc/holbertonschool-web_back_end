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

    // Overriding the default string description
    toString() {
        return this._code;
    }
}