/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cachedResults = new Map(); // the dictionary of cached results (map arguments to result)
    return function(...args) { // memoize returns a function that executes the inputted function but has checks for efficiency purpose
        const key = JSON.stringify(args); // This one is crucial, args is an array, so it must be converted to a string so it is only one value so it can be a key
        if(cachedResults.has(key)){ // We check if we already have the key in the map/dictionary
            return cachedResults.get(key); // If so just return that
        }
        let result = fn(...args); // Otherwise, execute it
        cachedResults.set(key, result); // Then store it in dictionary
        return result; // And return the result
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */