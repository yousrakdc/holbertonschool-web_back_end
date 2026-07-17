import { createClient, print } from 'redis';
import { promisify } from 'util';

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

async function displaySchoolValue(schoolName) {
    const get = promisify(client.get).bind(client);
    const AsyncGet = async (schoolName) => {
        return await get(schoolName);
    }
    const reply = await AsyncGet(schoolName);
    console.log(reply);
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
