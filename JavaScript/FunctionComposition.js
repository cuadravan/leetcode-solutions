/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        if(functions.length === 0){
            return x;
        }
        else{
            for(let i = functions.length - 1; i > -1; i--){
                x = functions[i](x);
            }
            return x;
        }
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */

// We create a function factory which returns a function that takes the array of functions it is given and run through each if executed with x
// If functions given is empty (length of zero), let the created function return x
// Also note we execute from right to left