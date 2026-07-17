import { createClient, print } from 'redis';

const client = createClient();

/**
 * Set a new value in Redis for a given key
 * @param {string} schoolName - The key name to set
 * @param {string} value
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

/**
 * Display the value for a given key from Redis
 * @param {string} schoolName - The key name to retrieve
 */

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    console.log(reply);
  });
}

client.on('connect', () => {
    console.log('Redis client connected to the server');
  });
  
  client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
  });

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
