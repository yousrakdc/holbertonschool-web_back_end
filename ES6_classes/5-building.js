/* eslint-disable */
export default class Building {
    constructor(sqft) {
        if (new.target === Building) {
            throw new TypeError('Abstract class "Building" cannot be instantiated directly');
        }

        if (typeof sqft !== 'number') {
            throw new TypeError('Sqft must be a number');
        }

        this._sqft = sqft;
    }

    // Getter for sqft
    get sqft() {
        return this._sqft;
    }

    // Abstract method that must be implemented by subclasses
    evacuationWarningMessage() {
        throw new Error('Class extending Building must override evacuationWarningMessage');
    }
}