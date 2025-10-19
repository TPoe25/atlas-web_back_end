// 1-stdin.js

// Print the welcome message
console.log("Welcome to Holberton School, what is your name?");

// Listen for user input
process.stdin.on("data", (input) => {
  const name = input.toString().trim();
  console.log(`Your name is: ${name}`);
});

// When input ends (Ctrl+D or piped input)
process.stdin.on("end", () => {
  console.log("This important software is now closing");
});

// When user presses Ctrl+C
process.on("SIGINT", () => {
  console.log("\nThis important software is now closing");
  process.exit();
});

// Start reading from stdin
process.stdin.resume();
