// JavaScript Security Vulnerabilities Test File
// This file contains intentional security issues that eslint-plugin-security should detect
// Upload this to your repository to test the security plugin

// ========================================
// Violation 1: security/detect-eval-with-expression
// Dangerous eval() usage with user input
// ========================================
const userInput = getUserInput();
eval(userInput);  // SECURITY ISSUE: Code injection vulnerability

// ========================================
// Violation 2: security/detect-non-literal-regexp
// Regular expression from user input (ReDoS vulnerability)
// ========================================
const pattern = getUserPattern();
const regex = new RegExp(pattern);  // SECURITY ISSUE: ReDoS attack possible

// ========================================
// Violation 3: security/detect-unsafe-regex
// Catastrophic backtracking regex
// ========================================
const unsafeRegex = /(a+)+$/;  // SECURITY ISSUE: Can cause exponential time complexity

// ========================================
// Violation 4: security/detect-non-literal-require
// Dynamic require with user input
// ========================================
const moduleName = getModuleName();
const module = require(moduleName);  // SECURITY ISSUE: Arbitrary module loading

// ========================================
// Violation 5: security/detect-child-process
// Executing shell commands with user input
// ========================================
const exec = require('child_process').exec;
const command = getUserCommand();
exec(command);  // SECURITY ISSUE: Command injection vulnerability

// ========================================
// Violation 6: security/detect-non-literal-fs-filename
// File system operations with user input
// ========================================
const fs = require('fs');
const filename = getUserFilename();
fs.readFile(filename, (err, data) => {  // SECURITY ISSUE: Path traversal
  console.log(data);
});

// ========================================
// Violation 7: security/detect-object-injection
// Object property access with user input
// ========================================
const userData = getUserData();
const obj = {};
const value = obj[userData];  // SECURITY ISSUE: Prototype pollution possible

// ========================================
// Violation 8: security/detect-new-buffer
// Old Buffer constructor (deprecated, unsafe)
// ========================================
const buf = new Buffer(100);  // SECURITY ISSUE: Use Buffer.alloc() instead

// ========================================
// Violation 9: security/detect-pseudoRandomBytes
// Weak random number generation for security purposes
// ========================================
const crypto = require('crypto');
const weakRandom = crypto.pseudoRandomBytes(16);  // SECURITY ISSUE: Not cryptographically secure

// ========================================
// Violation 10: security/detect-possible-timing-attacks
// String comparison vulnerable to timing attacks
// ========================================
function authenticateUser(password) {
  const secret = 'mySecretPassword';
  if (password === secret) {  // SECURITY ISSUE: Timing attack possible
    return true;
  }
  return false;
}

// ========================================
// Additional style violations (from basic ESLint)
// ========================================

// Missing semicolons
const foo = 'bar'
const baz = 'qux'

// Wrong quotes
const message = "should be single quotes"

// Unused variables
const unused = 123

// No const
let neverReassigned = 'value'

// Helper functions (for context)
function getUserInput() {
  return 'malicious code';
}

function getUserPattern() {
  return '.*';
}

function getModuleName() {
  return '../../../etc/passwd';
}

function getUserCommand() {
  return 'rm -rf /';
}

function getUserFilename() {
  return '../../etc/passwd';
}

function getUserData() {
  return '__proto__';
}

export default authenticateUser

