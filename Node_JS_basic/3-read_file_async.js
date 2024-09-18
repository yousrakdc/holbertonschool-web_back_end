const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.trim().split('\n');
    
    console.log('Raw lines:', lines);

    if (lines.length <= 1) {
      throw new Error('No students found in the database');
    }

    const fields = {};
    const students = [];
    const header = lines.shift();
    
    console.log('Header:', header);

    for (const line of lines) {
      if (line.trim() === '') {
        continue;
      }

      console.log('Processing line:', line);

      const student = line.split(',');
      
      if (student.length < 4) {
        console.log('Skipping malformed line:', line);
        continue;
      }

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


    console.log('Students:', students);
    console.log('Fields:', fields);

    let output = `Number of students: ${students.length}\n`;

    for (const field in fields) {
      const { count, names } = fields[field];
      output += `Number of students in ${field}: ${count}. List: ${names.join(', ')}\n`;
    }

    return output.trim();
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
