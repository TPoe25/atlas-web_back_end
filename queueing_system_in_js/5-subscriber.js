#!/usr/bin/env node
// 5-subscriber.js
// Async operations using Promises with Redis

import pkg from 'redis';
const { createClient } = pkg;

// Create subscriber client
const subscriber = createClient();

subscriber.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

await subscriber.connect();

const CHANNEL = 'holberton school channel';

await subscriber.subscribe(CHANNEL, (message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe(CHANNEL)
        .then(() => subscriber.quit());
  }
});
