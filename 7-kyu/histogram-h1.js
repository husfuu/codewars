function histogram(results){
    let res = ""
    let i = 1
    for (const freq of results) {
        const hashNum = "#".repeat(freq)
        if (freq == 0) {
            const formatedStr = `${i}|${hashNum}\n`
            res = formatedStr.concat("", res)
        } else {
            const formatedStr = `${i}|${hashNum} ${freq}\n`
            res = formatedStr.concat("", res)
        }
        i += 1
    }
    return res

const Test = require('@codewars/test-compat');

describe("Basic Tests", function(){
  it("Example", function(){
var expected=
`6|##### 5
5|
4|# 1
3|########## 10
2|### 3
1|####### 7
`
    var hist = histogram([7,3,10,1,0,5]);
    console.log(hist)
    Test.assertSimilar(hist, expected)
  });
});}
