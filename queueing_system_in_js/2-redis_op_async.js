#!/usr/bin/env node
// 2-redis_op_async.js
// Async operations using Promises with Redis

import pkg from 'redis';
import { promisify } from 'util';
const { createClient } = pkg;

// Create client
const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

await client.connect();

const getAsync = promisify(client.get).bind(client);

async function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.log('Error setting key:', err.message);
    } else {
      console.log('Reply:', reply);
    }
  });
}

// Function to get a value
async function displaySchoolValue(schoolName) {
  try {
    const value = await client.get(schoolName);
    console.log(value);
  } catch (err) {
    console.log('Error getting key:', err.message);
  }
}

// Example usage
await displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
await displaySchoolValue('HolbertonSanFrancisco');

// Close the client
await client.quit();
