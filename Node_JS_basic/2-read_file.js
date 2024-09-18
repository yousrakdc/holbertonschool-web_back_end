const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.trim().split('\n');

    if (lines.length <= 1) {
      throw new Error('No students found in the database');
    }

    const header = lines.shift();

    const fields = {};

    for (const line of lines) {
      if (line.trim() === '') {
        continue;
      }

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
    }

    const totalStudents = lines.length;
    console.log(`Number of students: ${totalStudents}`);

    for (const field in fields) {
      const { count, names } = fields[field];
      console.log(`Number of students in ${field}: ${count}. List: ${names.join(', ')}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;