import kue from 'kue';

const queue = kue.createQueue();

/**
 * Send notification function
 * @param {string} phoneNumber - The phone number to send notification to
 * @param {string} message - The message to send notification to
 */
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
