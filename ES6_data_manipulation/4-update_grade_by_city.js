/* eslint-disable */
export default function updatesStudentGradeByCity(students, city, newGrades) {
    if (!Array.isArray(students) || typeofcity !== 'string' || !Array.isArray(newGrades)) {
        return [];
    }

    return students
        .filter(student => student.location === city)
        .map(student => {
            const gradeObj = newGrades.find(grade => grade.studentId === student.id);
            return {
                ...student,
                grade: gradeObj ? gradeObj.grade : 'N/A',
            };
        });
}