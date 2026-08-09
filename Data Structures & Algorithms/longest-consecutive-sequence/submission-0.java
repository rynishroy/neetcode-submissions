class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        int longestLength=0;
        for(int num: nums){
            seen.add(num);
        }
        for(int num:nums){
            //check if its begining of sequence
            if (!(seen.contains(num-1))){
                int currentLength =0;
                while(seen.contains(num +currentLength) ){
                    currentLength++;
                }
                longestLength = Math.max(longestLength, currentLength);
            }
        }
        return longestLength;
        
    }
}
