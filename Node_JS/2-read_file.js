// read-file.js
const fs = require('fs');

function countStudents(path) {
    let data;
    try {
        data = fs.readFileSync(path, 'utf8');
    } catch (err) {
        throw new Error('Cannot load the database');
    }

    // Remove header and empty lines from data
    const lines = data.split('\n').filter(line => line.trim() !== '');
    if (lines.length === 0) {
        console.log('Number of students: 0');
        return;
    }

    // Extract header and student records
    const headers = lines[0].split(',');
    const students = lines.slice(1);

    console.log(`Number of students: ${students.length}`);

    // Group students by field
    const studentsByField = {};

    // Process each student record
    students.forEach((line) => {
        const record = line.split(',');
        if (record.length < 4) return;
        const firstName = record[0].trim();
        const field = record[3].trim();

        if (!studentsByField[field]) {
            studentsByField[field] = [];
        }
        studentsByField[field].push(firstName);
    });

    // Print number of students in each field and their names
    for (const [field, names] of Object.entries(studentsByField)) {
        console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
}

module.exports = countStudents;
