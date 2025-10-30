#!/usr/bin/env node
// 5-publisher.js
// Async operations using Promises with Redis

import pkg from 'redis';
const { createClient } = pkg;

// Create publisher client
const publisher = createClient();

publisher.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

await publisher.connect();

const CHANNEL = 'holberton school channel';

function publishMessage(message, time) {
  setTimeout(async () => {
    console.log('About to send', message);
    await publisher.publish(CHANNEL, message);
  }, time);
}

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
