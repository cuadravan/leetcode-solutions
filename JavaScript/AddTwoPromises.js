/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    return Promise.all([promise1, promise2]) // We return a promise that combines 2 promise, waits for both to resolve correctly, then propagated to another promise which adds them
    // If we do not return the outer promise, the inner promise inside the outer promise does get resolved but the function basically ends there, not returning anything
        .then((results)=>{
            return results[0] + results[1];
            // let num1 = results[0];
            // let num2 = results[1];
            // return new Promise((resolve,reject)=>{
            //     resolve(num1+num2);
            // });
        });
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */