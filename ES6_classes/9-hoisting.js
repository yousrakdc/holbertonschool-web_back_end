/* eslint-disable */
export class StudentHolberton {
    constructor(firstName, lastName, holbertonClass) {
      this._firstName = firstName;
      this._lastName = lastName;
      this._holbertonClass = holbertonClass;
    }
  
    get fullName() {
      return `${this._firstName} ${this._lastName}`;
    }
  
    get holbertonClass() {
      return this._holbertonClass;
    }
  
    get fullStudentDescription() {
      return `${this._firstName} ${this._lastName} - ${this._holbertonClass.year} - ${this._holbertonClass.location}`;
    }
  }