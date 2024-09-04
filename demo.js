// converting numsarrray to string array
// nums = [1,2,3,4,5]
// console.log(nums.map(String))

// Number to String
let num = 456;
console.log(String(num)); // "456"
console.log(num.toString()); // "456"
console.log(`${num}`); // "456"
console.log(num + ""); // "456"

// String to Number
let strInt = "789";
let strFloat = "123.45";
console.log(Number(strInt)); // 789
console.log(parseInt(strInt, 10)); // 789
console.log(parseFloat(strFloat)); // 123.45
console.log(+strInt); // 789

console.log("//////////////////");

val = "1";
console.log(Number.isInteger(val));
let char = "5";
if (/^\d$/.test(char)) {
  console.log("It's a digit.");
}

// //////////////////////////////////
console.log("1111" + 1); // 11111
console.log("1111" - 1); // 1110
console.log(typeof null); // object
console.log(typeof NaN); // number
console.log(0 === []); // false
console.log(0 == []); // true
console.log([] + 1); // 1    => [].toString() => "" => 0  <=> 0 + 1 => 1
console.log([] + "1"); // 1
console.log([] - 1) // -1
console.log([] - '1') // -1
console.log({} + [])  // 0
console.log([] === {}) // false
console.log([] == {}) // false


