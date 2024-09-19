import fs from 'fs/promises';

export async function readDatabase(filePath) {
  try {
    const data = await fs.readFile(filePath, 'utf8');
    const lines = data.trim().split('\n');

    if (lines.length <= 1) {
      return {};
    }

    const fields = {};
    lines.shift();

    for (const line of lines) {
      if (line.trim() === '') continue;

      const [firstName, , , field] = line.split(',');

      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstName);
    }

    return fields;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}
