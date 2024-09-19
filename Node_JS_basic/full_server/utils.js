import fs from 'fs/promises';

export default async function readDatabase(filePath) {
  try {
    const data = await fs.readFile(filePath, 'utf8');
    const lines = data.trim().split('\n');

    if (lines.length <= 1) {
      return {};
    }

    const fields = {};
    lines.shift();

    for (const line of lines) {
      const trimmedLine = line.trim();

      if (trimmedLine !== '') {
        const [firstName, , , field] = trimmedLine.split(',');

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      }
    }

    return fields;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}
