import kue from 'kue';

const queue = kue.createQueue();

const blacklistedNumbers = ['4153518780', '4153518781'];

/**
 * Send notification function
 * @param {string} phoneNumber - The phone number to send notification to
 * @param {string} message - The message to send
 * @param {object} job - The Kue job object
 * @param {function} done - Callback to call when job is complete
 */
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
