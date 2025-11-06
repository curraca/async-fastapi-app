import Foundation

// MARK: - Issue 1: Short type name (< 3 chars)
class AB {
    var x: Int = 0
}

// MARK: - Issue 2 & 3: Force unwrapping and force try
class DataManager {
    func loadData() {
        let url = URL(string: "https://api.example.com/data")!  // Force unwrap!
        let data = try! Data(contentsOf: url)  // Force try!
        let unwrappedData = data  // This will trigger issues above
    }
    
    // MARK: - Issue 4: Line too long (> 120 characters)
    func processVeryLongFunctionNameWithMultipleParametersThatExceedsTheLineLength(parameter1: String, parameter2: Int, parameter3: Bool) -> String {
        return "This line is intentionally very very very very very very very very very very very very very long to exceed 120 characters"
    }
    
    // MARK: - Issue 5: Function body too long & cyclomatic complexity
    func complexFunction(value: Int) -> String {
        if value > 100 {
            if value > 200 {
                if value > 300 {
                    return "Very high"
                } else {
                    return "High"
                }
            } else {
                if value > 150 {
                    return "Medium-high"
                } else {
                    return "Medium"
                }
            }
        } else {
            if value > 50 {
                if value > 75 {
                    return "Low-medium"
                } else {
                    return "Low"
                }
            } else {
                if value > 25 {
                    return "Very low"
                } else {
                    return "Extremely low"
                }
            }
        }
    }
}

// MARK: - Issue 6: Poor identifier naming
class UserService {
    var x = 0  // Too short
    var y = ""  // Too short
    
    func a() {}  // Too short
    
    // MARK: - Issue 7: Empty count instead of isEmpty
    func checkIfEmpty(items: [String]) -> Bool {
        return items.count == 0  // Should use isEmpty
    }
}

// MARK: - Issue 8: Trailing whitespace (add spaces at end of these lines)
let unused = "test"     
let another = "value"    

// MARK: - Issue 9: Multiple force unwraps in one function
func dangerousFunction() {
    let optional1: String? = "test"
    let optional2: Int? = 42
    let optional3: Bool? = true
    
    let value1 = optional1!  // Force unwrap
    let value2 = optional2!  // Force unwrap
    let value3 = optional3!  // Force unwrap
    
    print("\(value1) \(value2) \(value3)")
}

// MARK: - Issue 10: Force try in multiple places
func multipleForceT

ries() {
    let url1 = URL(string: "https://example.com")!
    let data1 = try! Data(contentsOf: url1)
    
    let url2 = URL(string: "https://example2.com")!
    let data2 = try! Data(contentsOf: url2)
    
    print("\(data1.count) \(data2.count)")
}

// MARK: - Issue 11: Long type name
class VeryVeryVeryVeryLongClassNameThatExceedsTheMaximumRecommendedLength {
    var property = 0
}

// MARK: - Issue 12: Nested complexity
func superComplexFunction(a: Int, b: Int, c: Int) -> Int {
    var result = 0
    
    for i in 0..<a {
        for j in 0..<b {
            for k in 0..<c {
                if i > j {
                    if j > k {
                        if k > 0 {
                            result += i + j + k
                        } else {
                            result += i + j
                        }
                    } else {
                        result += i
                    }
                } else {
                    result += 1
                }
            }
        }
    }
    
    return result
}

// MARK: - Issue 13: Explicit init (redundant)
struct Point {
    var x: Int
    var y: Int
    
    init(x: Int, y: Int) {
        self.x = x
        self.y = y
    }
}

let point = Point.init(x: 0, y: 0)  // Redundant .init

// MARK: - Issue 14: Unused optional binding
func processOptional(_ value: String?) {
    if let unwrapped = value {
        // Variable 'unwrapped' bound but never used
        print("Has value")
    }
}