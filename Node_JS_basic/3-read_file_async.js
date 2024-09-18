const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.trim().split('\n');

    if (lines.length <= 1) {
      throw new Error('No students found in the database');
    }

    const fields = {};
    const students = [];
    lines.shift();

    for (const line of lines) {
      const trimmedLine = line.trim();

      if (trimmedLine !== '') {
        const student = trimmedLine.split(',');

        if (student.length >= 4) {
          const firstName = student[0];
          const field = student[3];

          students.push(firstName);

          if (!fields[field]) {
            fields[field] = {
              count: 0,
              names: [],
            };
          }

          fields[field].count += 1;
          fields[field].names.push(firstName);
        }
      }
    }

    let output = `Number of students: ${students.length}\n`;

    for (const field in fields) {
      if (Object.hasOwn(fields, field)) {
        const { count, names } = fields[field];
        output += `Number of students in ${field}: ${count}. List: ${names.join(', ')}\n`;
      }
    }

    return output.trim();
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
