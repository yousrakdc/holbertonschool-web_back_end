/* eslint-disable */
export default function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
        // Simulate an API call with a timeout
        setTimeout(() => {
            // Assume the API call is successful and we get a response
            const success = true;

            if (success) {
                resolve("API response received successfully!");
            } else {
                reject("Failed to receive API response.");
            }
        }, 1000); // Simulate a delay of 1 second
    });
}