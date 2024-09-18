const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.trim().split('\n');

    if (lines.length <= 1) {
      throw new Error('No students found in the database');
    }

    lines.shift();

    const fields = {};
    let totalStudents = 0;

    lines.forEach((line) => {
      if (line.trim() !== '') {
        const student = line.split(',');
        const firstName = student[0];
        const field = student[3];

        if (!fields[field]) {
          fields[field] = {
            count: 0,
            names: [],
          };
        }

        fields[field].count += 1;
        fields[field].names.push(firstName);
        totalStudents += 1;
      }
    });

    console.log(`Number of students: ${totalStudents}`);

    for (const field in fields) {
      if (Object.hasOwn(fields, field)) {
        const { count, names } = fields[field];
        console.log(`Number of students in ${field}: ${count}. List: ${names.join(', ')}`);
      }
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
