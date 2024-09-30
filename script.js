// script.js

// Function to add two numbers
function add(a, b) {
    return a + b;
}

// Function to subtract two numbers
function subtract(a, b) {
    return a - b;
}

// Function to multiply two numbers
function multiply(a, b) {
    return a * b;
}

// Function to divide two numbers
function divide(a, b) {
    if (b === 0) {
        return 'Error: Division by zero';
    }
    return a / b;
}

// Function to find the modulus of two numbers
function modulus(a, b) {
    return a % b;
}

// Function to exponentiate two numbers
function exponentiate(a, b) {
    return a ** b;
}

// Function to handle the calculation based on user input
function calculate() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const operator = document.getElementById('operator').value;
    let result;

    if (isNaN(num1) || isNaN(num2)) {
        result = 'Error: Invalid input';
    } else {
        switch (operator) {
            case '+':
                result = add(num1, num2);
                break;
            case '-':
                result = subtract(num1, num2);
                break;
            case '*':
                result = multiply(num1, num2);
                break;
            case '/':
                result = divide(num1, num2);
                break;
            case '%':
                result = modulus(num1, num2);
                break;
            case '**':
                result = exponentiate(num1, num2);
                break;
            default:
                result = 'Invalid operator';
        }
    }

    document.getElementById('result').innerText = `Result: ${result}`;
}

// Add event listener to the calculate button
document.getElementById('calculateBtn').addEventListener('click', calculate);