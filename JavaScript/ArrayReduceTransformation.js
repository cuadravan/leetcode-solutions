/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let original = init;
    let accum = init;
    let newArr = [];
    for(let i = 0; i<nums.length; i++){
        newArr.push(fn(accum, nums[i]));
        accum = newArr[i];
    }
    if(newArr.length === 0){
        return original;
    }
    else{
        return accum;
    }
}; // To apply reduce to an array, we iterate through the array and apply the function to each element and the accum
// Note that for each loop, we apply the previous element that we just calculated (accum = newArr[i])
// This accum has an initial value
// But if new array has a length zero, just return the init
// Otherwise, return the accum