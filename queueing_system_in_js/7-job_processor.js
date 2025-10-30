#!/usr/bin/env node

import kue from "kue";

const queue = kue.createQueue();
const blacklisted = ['4153518780', '4153518781'];

/**
 * send notification function
 * @param {string} phoneNumber - Phone number to send notification to
 * @param {string} message - Message to send
 * @param {object} job
 * @param {function} done - Callback function to indicate job completion
 */
function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100);

    if (blacklisted.includes(phoneNumber)) {
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}: with message: ${message}`);
    done();
}

// Process jobs from the queue
queue.process("push_notification_code_2", (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});

