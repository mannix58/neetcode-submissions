class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let sorted = nums.sort();
        for (let i = 1; i < sorted.length; i++) {
            if (sorted[i] === sorted[i-1] ) return true
        } return false
    }
}
