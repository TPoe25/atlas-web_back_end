// 3-read_file_async.js

const fs = require("fs").promises;

// Read and count students from a CSV file asynchronously
function countStudents(path) {
  return fs
    .readFile(path, "utf8")
    .then((data) => {
      const lines = data.split("\n").filter((line) => line.trim() !== "");
      if (lines.length <= 1) {
        console.log("Number of students: 0");
        return {};
      }

      // Extract header and student records
      const students = lines.slice(1);
      console.log(`Number of students: ${students.length}`);

      const studentsByField = {};

      // Group students by field of study
      students.forEach((line) => {
        const [firstName, , , field] = line.split(",");
        if (!field || !firstName) return;
        if (!studentsByField[field]) studentsByField[field] = [];
        studentsByField[field].push(firstName.trim());
      });

      // Print number of students in each field and their names
      for (const [field, names] of Object.entries(studentsByField)) {
        console.log(
          `Number of students in ${field}: ${names.length}. List: ${names.join(
            ", "
          )}`
        );
      }

      // Return the grouped students by field
      return studentsByField;
    })
    .catch(() => {
      throw new Error("Cannot load the database");
    });
}

module.exports = countStudents;
