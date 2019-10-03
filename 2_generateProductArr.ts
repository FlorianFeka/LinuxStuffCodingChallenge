function prodArr(arr: number[]) {
    const result: number[] = [];
    arr.forEach(i => {
        result.push(arr.reduce((accumulator, currentValue, index) => {
            if(index === i-1)
                return accumulator;
            return accumulator * currentValue;
        }));
    });
    return result;
}