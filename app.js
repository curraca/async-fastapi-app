// ESLint violation test file
// Contains intentional violations to test ESLint detection

// Violation 1: no-unused-vars (unused variable)
const unusedVariable = 123

// Violation 2: no-console (console statement)
console.log("Debug message")

// Violation 3: semi (missing semicolons)
const foo = "bar"
const baz = "qux"

// Violation 4: quotes (wrong quote style - should be single quotes)
const message = "hello world"

// Violation 5: indent (wrong indentation - should be 2 spaces)
function badIndent() {
    const x = 1  // 4 spaces instead of 2
     const y = 2  // 3 spaces
  return x + y
}

// Violation 6: no-undef (undefined variable)
result = undefinedVariable + 1

// Violation 7: comma-dangle (trailing comma - we configured it as error, never)
const obj = {
  a: 1,
  b: 2,
}

// Violation 8: no-trailing-spaces (trailing spaces at end of lines)
const test = "value"    

// Violation 9: space-before-function-paren (should be no space)
function badSpacing () {
  return true
}

// Violation 10: prefer-const (should use const instead of let)
let neverReassigned = "value"
console.log(neverReassigned)

// Violation 11: no-var (should use let/const)
var oldStyle = 456

// Violation 12: no-eval (security issue)
eval("console.log('dangerous')")

// Violation 13: eol-last (missing newline at end of file)
export default badIndent