const fs = require('fs').promises;

function countStudents(path) {
    return fs.readFile(path, 'utf8')
       .then(data => {
            // Remove header and empty lines from data
            const lines = data.split('\n').filter(line => line.trim()!== '');
            if (lines.length === 0) {
                console.log('Nummber of students: 0');
                return;
            }

            const students = lines.slice(1);
            console.log(`Number of students: ${students.length}`);

            // Group students by field
            const studentsByField = {};

            // Process each student record
            students.forEach(line => {
        const record = line.split(',');
        if (record.length < 4) return; // skip invalid lines
        const firstName = record[0].trim();
        const field = record[3].trim();

        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }
        studentsByField[field].push(firstName);
      });

      for (const [field, names] of Object.entries(studentsByField)) {
        console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      }
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
