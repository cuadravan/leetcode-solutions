/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let called = 0;
    return function(...args){
        ++called;
        if(called > 1){
            return undefined;
        }
        return fn(...args);
    }
};

// once is a function factory that creates a function which accepts a function, it retains reference to how many times it is called
// Every time it is invoked, we increment the called variable for that function
// If we already called it more than one time, we return undefined, otherwise, let it run the function 

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */