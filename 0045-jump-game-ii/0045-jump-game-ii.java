class Solution {
    public int jump(int[] nums) {
        int left = 0;
        int right = 0;
        int minJumps = 0;
        
        while(right < nums.length - 1){
            int furthest = 0;
            
            for(int i = left; i < right + 1; i++){
                furthest = Math.max(furthest, i + nums[i]);
                
            }
            left = right + 1;
            right = furthest;
            minJumps++;
        }
        return minJumps;
    }
}