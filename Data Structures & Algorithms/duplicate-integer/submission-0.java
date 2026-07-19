class Solution {
    public boolean hasDuplicate(int[] nums) {
        //data structure to hold the integer array 

        //iterate through the values with a loop 

        //check for duplicates by

        //if arr[i] = arr[i-1]{return true}
        for(int i = 0; i < nums.length; i++){
            for(int j = 0; j < nums.length; j++){
                if(i != j && nums[i] == nums[j]){
                    return true;
                }
            }
        }
        return false;
    }
}
