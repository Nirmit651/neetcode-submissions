class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let profit = 0;

        for(let i = 0;i<=prices.length-1;i++) {
            let currentProfit = 0;
            for(let j = i+1;j<=prices.length;j++) {
                if(prices[j]-prices[i] > profit) {
                    profit = prices[j]-prices[i]
                }
            }
        }

        return profit;
    }
}
