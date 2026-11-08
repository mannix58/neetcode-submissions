class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMaxConsecutiveOnes(nums) {
        let res = 0;
        let cnt = 0;
        
        for (const num of nums) {
            cnt = num === 1 ? cnt + 1 : 0;
            res = Math.max(res, cnt);
        }
        return res;
    }
}