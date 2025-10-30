// 5-http.js

const http = require("http");
const countStudents = require("./3-read_file_async");

const database = process.argv[2];
const port = 1245;

const app = http.createServer((req, res) => {
  res.setHeader("Content-Type", "text/plain");

  if (req.url === "/") {
    res.statusCode = 200;
    res.end("Hello Holberton School!");
  } else if (req.url === "/students") {
    res.statusCode = 200;
    let output = "This is the list of our students\n";

    countStudents(database)
      .then((studentsByField) => {
        const total = Object.values(studentsByField).reduce(
          (sum, arr) => sum + arr.length,
          0
        );
        output += `Number of students: ${total}\n`;

        for (const [field, names] of Object.entries(studentsByField)) {
          output += `Number of students in ${field}: ${
            names.length
          }. List: ${names.join(", ")}\n`;
        }

        res.end(output.trim());
      })
      .catch(() => {
        res.statusCode = 500;
        res.end("Cannot load the database");
      });
  } else {
    res.statusCode = 404;
    res.end("Not found");
  }
});

app.listen(port);

module.exports = app;
