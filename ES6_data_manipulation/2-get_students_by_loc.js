/* eslint-disable */
export default function getStudentsByLocation(students, city) {
    if (!Array.isArray(students)) { //Check if the input is an array
        return []; //Return an empty array if the input is not an array
    }

    return students.filter(student => student.location === city); //function uses the filter function to create a new array 
    //consisting of the student objects whose location property matches the specified city
}