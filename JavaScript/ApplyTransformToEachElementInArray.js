/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let newArr = [];
    for(let i = 0; i < arr.length; i++){
        newArr.push(fn(arr[i], i));
    }
    return newArr;
}; // To apply a function to each element, just iterate to each element and apply the function to each element and push to a new array