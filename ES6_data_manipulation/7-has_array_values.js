/* eslint-disable */
export default function hasValueFromArray(set, array) {
    return array.every(element => set.has(element)); //function uses the every method to check if all elements in the array pass the provided test
    //Return boolean
}