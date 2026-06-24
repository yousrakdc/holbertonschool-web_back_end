const express = require("express");

const app = express();
const PORT = 7865;

app.use(express.json());

app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`);
});

app.get("/", (req, res) => {
  res.send("Welcome to the payment system");
});

app.get("/cart/:id", (req, res) => {
  const { id } = req.params;

  if (/^\d+$/.test(id)) {
    res.send(`Payment methods for cart ${id}`);
  } else {
    res.status(404).send("Id not found");
  }
});

app.get("/available_payments", (req, res) => {
  res.json({ payment_methods: { credit_cards: true, paypal: false } });
});

app.post("/login", (req, res) => {
  const username = req.body.userName;
  res.send(`Welcome ${username}`);
});

module.exports = app;
