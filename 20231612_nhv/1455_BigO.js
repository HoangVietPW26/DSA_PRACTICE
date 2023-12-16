```
Big O represent for how many steps an algorithm takes for N data elements
Ex: Linear Search, best case: O(1), worst case O(N)
```

```
O(1): step not increase no matter data element increase
O(N): step increase linearly with num of data element
O(logN): algo take as many steps to halve data elements until 1
O(1) < O(logN) < O(N)
```

// The grain problems
function chessboardSpace(numberOfGrains) {
    let chessboardSpaces = 1;
    let placedGrains = 1;
    while (placedGrains < numberOfGrains) {
        placedGrains *= 2;
        chessboardSpaces += 1;
    }
    return chessboardSpaces;
}
```
Assum M chessboard need for N grains, 2^M >= N
-> M = log2(N)
-> O(logN)
```


function selectAStrings(array) {
    let newArray = [];
    for(let i = 0; i < array.length; i++) {
        if (array[i].startsWith("a")) {
            newArray.push(array[i]);
        }
    }
    return newArray;
}
// O(N)

// Prob5: find med of ordered array
function median(array) {
    const middle = Math.floor(array.length / 2); // O(1)
    // If array has even amount of numbers:
    if (array.length % 2 === 0) {
        return (array[middle - 1] + array[middle]) / 2;
    } else { // If array has odd amount of numbers:
        return array[middle];
    }
}
// O(1)





