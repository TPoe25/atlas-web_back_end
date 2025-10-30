#!/usr/bin/env node
import { createClient } from 'redis';

async function main() {
  const client = createClient();

  client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err.message);
  });

  await client.connect();

  console.log('Redis client connected to the server');

  await client.set('Holberton', 'School');
  const value = await client.get('Holberton');
  console.log('Value of Holberton:', value);

  await client.quit();
}

main();
