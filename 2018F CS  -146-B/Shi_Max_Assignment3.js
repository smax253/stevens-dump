const display = document.querySelector("#output");
var buffer = 0;
var result = 0;
var currentOp = "";
const maxLength = 9;
var hasResult = false;
var error = false;
const maxValue = 999999999
const minValue = -999999999
/**
 * Resets the state of the calculator and the display
 */
function resetCalc() {
    buffer = 0;
    result = 0;
    op = -1;
    display.innerHTML = "0";
    hasResult = false;
    error = false;
}

/**
 * Sets the inner text of the div with id="output"
 * @param {String} str the string to set the inner text to
 */
function setDisplay(str) {
   display.innerHTML = str;
}

/**
 * Returns the current result of the calculator
 * Hint: you can use a global variable for the result
 */
function getResult() {
    /*
    console.log('buffer: '+buffer);
    console.log('result: '+result);
    console.log('op: '+currentOp);
    */
    if(!hasResult){
        let answer = 0;
        switch(currentOp){
            case '+':
                answer = buffer+result;
                break;
            case '-':
                answer = buffer-result;
                break;
            case '*':
                answer = buffer*result;
                break;
            case '/':
                if (result == 0) {
                    answer = 0;
                    error = true;
                }
                else answer = Math.floor(buffer/result);
                break;
        }
        if (answer>maxValue) answer = maxValue;
        else if (answer<minValue) answer = minValue;
        //console.log(answer);
        return answer;
    }
    else return buffer;

}

/**
 * Update the calculator state with the next number and sets the display
 * @param {Number} num the number that was pressed
 */
function pressNum(num) {
    if(!hasResult){
        if(display.innerHTML.length<maxLength){
            if(display.innerHTML == "0") display.innerHTML = "";
            display.innerHTML += num;
            //if (display.innerHTML.length>maxLength) display.innerHTML = maxValue;
        }
        else{
            display.innerHTML="999999999";
        }
    }else{
        resetCalc();
        pressNum(num);
    }
}

/**
 * Operation is pressed, move the current result value to a temporary buffer and
 * set the current result to zero.
 * @param {String} op the operation pressed, either: +,-,*,/
 */
function pressOp(op) {
    hasResult = false;
    if(display.innerHTML!='0'){
        currentOp = op;
        buffer = parseInt(display.innerHTML);
        display.innerHTML = "0";
    }else{
        currentOp = op;
    }
}

/**
 * Should compute the current operation with the buffer value and current
 * result value based on the current operation. If there is no current
 * operation, do nothing.
 */
function pressEquals() {
    if(!hasResult)
    result = parseInt(display.innerHTML);
    hasResult = false;
    buffer = getResult();
    if(!error) setDisplay(buffer);
    else setDisplay("ERROR");
    error = false;
    hasResult= true;
    //console.log(buffer);
}
resetCalc();
