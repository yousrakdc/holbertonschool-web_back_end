const express = require('express');

const app = express();
const PORT = 7865;

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// Route with regex validation: :id must be only digits
app.get('/cart/:id(\\d+)', (req, res) => {
  const { id } = req.params;
  res.send(`Payment methods for cart ${id}`);
});

app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`);
});

module.exports = app;
