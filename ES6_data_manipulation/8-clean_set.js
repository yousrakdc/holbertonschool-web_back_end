/* eslint-disable */
export default function cleanSet(set, startString) {
    if (typeof startString !== 'string' || startString.length === 0) {
      return '';
    }
  
    let result = '';
  
    for (const value of set) {
      if (value.startsWith(startString)) {
        result += (result ? '-' : '') + value.slice(startString.length);
      }
    }
  
    return result;
  }