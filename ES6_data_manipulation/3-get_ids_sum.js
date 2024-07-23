/* eslint-disable */
export default function getStudentsIdsSum(students) {
    if (!Array.isArray(students)) {
        return 0; // Return 0 if the input is not an array
    }

    // Takes a callback function that adds the id of the current student to the accumulating sum, starting from an initial value of 0.
    return students.reduce((sum, student) => sum + student.id, 0);
}