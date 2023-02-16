function cocktailSort(arr) {
    let tmp = 0
    for(let i = 0; i < arr.length/2; i++) {
        // 从左往右
        let isSorted = true
        for(let j = i; j < arr.length - i - 1; j++) {
            if (arr[j] > arr[j+1]) {
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
                isSorted = false
            }
        }
        if (isSorted) {
            break
        }
        // 从右往左
        isSorted = true
        for(let j = arr.length - i - 1; j > i; j--) {
            if (arr[j] < arr[j-1]) {
                tmp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = tmp
                isSorted = false
            }
        }
        if (isSorted) {
            break
        }
    }
    return arr
}

// test case
console.log(cocktailSort([2,3,4,5,6,7,8,1,0]))