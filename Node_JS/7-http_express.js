// 7-http_express.js
// Create an Express server that serves student information from a CSV file

const express = require("express");
const fs = require("fs");

const app = express();

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, "utf-8", (err, data) => {
      if (err) {
        reject(new Error("Cannot load the database"));
        return;
      }

      const lines = data.trim().split("\n");
      if (lines.length <= 1) {
        resolve("Number of students: 0");
        return;
      }

      const students = lines
        .slice(1)
        .filter((line) => line.trim().length > 0)
        .map((line) => line.split(","));

      const fields = {};
      for (const student of students) {
        const field = student[3];
        if (!fields[field]) fields[field] = [];
        fields[field].push(student[0]);
      }

      let output = `Number of students: ${students.length}`;
      for (const [field, names] of Object.entries(fields)) {
        output += `\nNumber of students in ${field}: ${
          names.length
        }. List: ${names.join(", ")}`;
      }

      resolve(output);
    });
  });
}

app.get("/", (req, res) => {
  res.send("Hello Holberton School!");
});

app.get("/students", (req, res) => {
  const dbPath = process.argv[2];
  if (!dbPath) {
    res.send("This is the list of our students\nCannot load the database");
    return;
  }

  countStudents(dbPath)
    .then((result) => {
      res.send(`This is the list of our students\n${result}`);
    })
    .catch(() => {
      res.send("This is the list of our students\nCannot load the database");
    });
});

app.listen(1245);

module.exports = app;
