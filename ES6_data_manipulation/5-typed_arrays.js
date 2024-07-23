/* eslint-disable */
export default function createInt8TypeArray(length, postion, value) {
    if (postion < 0 || postion >= length) {
        throw new Error('Position outside range');
    }

    const buffer = new ArrayBuffer(length);
    const int8View = new Int8Array(buffer);
    int8View[postion] = value;
    return buffer;
}