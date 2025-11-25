/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {    
    let value = init;
    let original = init;
    return {
        increment(){
            return ++value;
        },
        reset(){
            value = original;
            return value;
        },
        decrement(){
            return --value;
        }
    };
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */

// createCounter is an object factor which returns an object with 3 methods, value and original are variables wrapped around it through a closure