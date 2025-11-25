/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    return arguments.length;
};
// This one is self explanatory
/**
 * argumentsLength(1, 2, 3); // 3
 */