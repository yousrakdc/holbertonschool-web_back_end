import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;

const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

/**
 * Get item by ID from listProducts
 * @param {number} id - The item ID
 * @returns {object|null} The item object or null if not found
 */
function getItemById(id) {
  return listProducts.find(item => item.id === id);
}

/**
 * Reserve stock for an item in Redis
 * @param {number} itemId - The item ID
 * @param {number} stock - The stock quantity to reserve
 */
function reserveStockById(itemId, stock) {
  setAsync(`item.${itemId}`, stock);
}

/**
 * Get current reserved stock for an item from Redis
 * @param {number} itemId - The item ID
 * @returns {Promise<number>} The reserved stock quantity
 */
async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock, 10) : 0;
}

app.get('/list_products', (req, res) => {
  const products = listProducts.map(item => ({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock
  }));
  res.json(products);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = item.stock - reservedStock;

  res.json({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity: currentQuantity
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = item.stock - reservedStock;

  if (currentQuantity <= 0) {
    return res.json({ status: 'Not enough stock available', itemId: itemId });
  }

  reserveStockById(itemId, reservedStock + 1);

  res.json({ status: 'Reservation confirmed', itemId: itemId });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
