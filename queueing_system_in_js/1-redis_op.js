#!/usr/bin/env node
// 1-redis_op.js
// Import the redis module

import pkg from "redis";
const { createClient } = pkg;

// Create client
const client = createClient();

client.on("error", (err) => {
  console.log("Redis client not connected to the server:", err.message);
});

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

await client.connect();

async function setNewSchool(schoolName, value) {
  try {
    const reply = await client.set(schoolName, value);
    console.log("Reply:", reply); // prints "OK"
  } catch (err) {
    console.log("Error setting key:", err.message);
  }
}

// Function to get a value
async function displaySchoolValue(schoolName) {
  try {
    const value = await client.get(schoolName);
    console.log(value);
  } catch (err) {
    console.log("Error getting key:", err.message);
  }
}

// Example usage
await displaySchoolValue("Holberton");
await setNewSchool("HolbertonSanFrancisco", "100");
await displaySchoolValue("HolbertonSanFrancisco");

// Close the client
await client.quit();
