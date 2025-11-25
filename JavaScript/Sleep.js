/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    return new Promise((resolve)=>{
        setTimeout(()=>resolve()
        ,millis);
    });
}

// sleep is simply a function that takes in a time then  returns a Promise that always resolves, but only after the setTimeout is done with the given time

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */