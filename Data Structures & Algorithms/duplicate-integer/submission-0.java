class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<Integer>();
        for(int val : nums){
            if(!(seen.add(val))){
                return true;
            }
        }
        return false;
    }
}