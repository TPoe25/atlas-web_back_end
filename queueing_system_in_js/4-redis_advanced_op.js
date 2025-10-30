#!/usr/bin/env node
// 4-redis_advanced_op.js
// Async operations using Promises with Redis

import { createClient } from "redis";

// Create client
const client = createClient();

client.on("error", (err) => {
  console.log("Redis client not connected to the server:", err.message);
});

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

client.connect();

client.del("HolbertonSchools");

// Function to print a message and result
function print(reply) {
  console.log("Reply:", reply);
}

async function main() {
  // Delete the hash to ensure new fields
  await client.del("HolbertonSchools");

  // Set fields and print results
  print(await client.hSet("HolbertonSchools", "Portland", "50"));
  print(await client.hSet("HolbertonSchools", "Seattle", "80"));
  print(await client.hSet("HolbertonSchools", "New York", "20"));
  print(await client.hSet("HolbertonSchools", "Bogota", "20"));
  print(await client.hSet("HolbertonSchools", "Cali", "40"));
  print(await client.hSet("HolbertonSchools", "Paris", "2"));

  // Display the hash
  const result = await client.hGetAll("HolbertonSchools");
  console.log(result);

  await client.quit();
}

main();
