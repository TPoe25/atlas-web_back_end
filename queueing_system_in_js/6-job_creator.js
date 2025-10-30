#!/usr/bin/env node

import kue from "kue";

// Create the queue
const queue = kue.createQueue();

// Example job data
const jobData = {
  phoneNumber: "4153518780",
  message: "This is a test notification",
};

// Create a job in the queue
const job = queue.create("push_notification_code", jobData).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

// Listen for job events
job.on("complete", () => {
  console.log("Notification job completed");
});

job.on("failed", (err) => {
  console.log("Notification job failed:", err);
});
