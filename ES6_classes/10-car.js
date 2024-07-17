/* eslint-disable */
export default class Car {
    constructor(brand, motor, color) {
        this._brand = brand;
        this._motor = motor;
        this._color = color;
    }

    cloneCar() {
        // Create a new instance using the class of the current instance
        return new this.constructor(this._brand, this._motor, this._color);
    }
}