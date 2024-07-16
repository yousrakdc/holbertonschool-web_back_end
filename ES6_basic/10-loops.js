/* eslint-disable */
export default function appendToEachArrayValue(array, appendString) {
    // Use the for...of loop to iterate over the array with index and value
    for (let [index, value] of array.entries()) {
      // Append the appendString to the current value and update the array element
      array[index] = appendString + value;
    }
    // Return the modified array
    return array;
  }  