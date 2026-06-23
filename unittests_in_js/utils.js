function calculateNumber(type, a, b) {
    const x = Math.round(a);
    const y = Math.round(b);
  
    switch (type) {
      case "SUM":
        return x + y;
      case "SUBTRACT":
        return x - y;
      case "DIVIDE":
        return y === 0 ? "Error" : x / y;
      default:
        throw new Error("Calcul not found.");
    }
  }
  
  module.exports = { calculateNumber };
