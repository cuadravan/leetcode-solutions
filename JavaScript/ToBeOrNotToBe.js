/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    let object = new Object();
    object.toBe = function(arg){
        if(val === arg){
            return(true);
        }
        else{
            throw new Error("Not Equal");
        }
    }
    object.notToBe = function(arg){
        if(val !== arg){
            return(true);
        }
        else{
            throw new Error("Equal");
        }        
    }
    return object;
};

// expect is an object factor that takes a value, and returns an object with 2 function
// toBe is a function that takes in a value, and if it is same as our stored value then return true
// notToBe is the opposite of toBe

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */