/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let newArr = [];
    for(let i = 0; i < arr.length; i++){
        if(Boolean(fn(arr[i],i)) === true){
            newArr.push(arr[i]);
        }
    }
    return newArr;
};

// Loop through every element of the array and check if applying the function to the element yields true, then we push the element