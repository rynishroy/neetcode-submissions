class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for(int num:nums){
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        List<List<Integer>> buckets = new ArrayList<>();
        for(int i=0;i<=nums.length; i++){
            buckets.add(new ArrayList<>());
        }

        for(int num: freq.keySet()){
            int count = freq.get(num);
            buckets.get(count).add(num);
        }

        List<Integer> result = new ArrayList<>();
        for(int i= buckets.size()-1; i>=0 && result.size()<k; i--){
            for(int num:buckets.get(i)){
                result.add(num);
                if(result.size() == k) break;
            }
        }
        int[] resultArray = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            resultArray[i] = result.get(i);
        }
        return resultArray;
    }
}
