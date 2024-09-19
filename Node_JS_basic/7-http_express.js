const express = require('express');

const countStudents = require('./3-read_file_async');
const database = process.argv[2];

const app = express();

app.get('/', (req, res) => {
  res.type('text').send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.type('text');

  try {
    const output = await countStudents(database);
    res.send(`This is the list of our students\n${output}`);
  } catch (err) {
    res.status(500).send(err.message);
  }
});

const port = 1245;
app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

module.exports = app;
