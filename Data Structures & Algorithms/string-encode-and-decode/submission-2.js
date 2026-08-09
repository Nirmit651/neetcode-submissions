class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let encoded = ""
        strs.forEach((str) => {
            let length = String(str.length);
            encoded += length + "#" + str
        })
        console.log(encoded)
        return encoded;
        
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        const arr = [];
        let i = 0;

        while (i < str.length) {
            // Find the # separating the length from the string
            let hashIndex = i;

            while (str[hashIndex] !== "#") {
                hashIndex++;
            }

            // Everything from i to hashIndex is the length
            const length = Number(str.substring(i, hashIndex));

            // The actual string starts after #
            const start = hashIndex + 1;
            const end = start + length;

            arr.push(str.substring(start, end));

            // Move to the beginning of the next encoded string
            i = end;
        }
        return arr;
    }
}
