/* eslint-disable */
export default function createInt8TypeArray(length, postion, value) {
  // Create a new ArrayBuffer with the given length
  const buffer = new ArrayBuffer(length);

  // Create a new Int8Array view of the buffer
  const int8Array = new Int8Array(buffer);

  // Check if the position is within the range of the buffer
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // Set the value at the specified position
  int8Array[position] = value;

  // Return the ArrayBuffer
  return buffer;
}