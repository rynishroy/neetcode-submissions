class Solution {
    public int maxArea(int[] heights) {
        int left =0;
        int right = heights.length -1;
        int max_water =0;

        while(left<=right){
            int water = (right-left)* Math.min(heights[left], heights[right]);
            max_water = Math.max(water, max_water);
            if(heights[left]<heights[right]){
                left++;
            }else{
                right--;
            }

        }
        return max_water;
        
    }
}
