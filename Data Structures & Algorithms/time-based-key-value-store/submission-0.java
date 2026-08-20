class TimeMap {

    private static class Entry{
        int timestamp;
        String value;

        Entry(int timestamp, String value){
            this.timestamp = timestamp;
            this.value = value;
        }
    }
     
    private final Map<String, List<Entry>> map;
    public TimeMap() {
        map = new HashMap();
        
    }
    
    public void set(String key, String value, int timestamp) {
        map.computeIfAbsent(key, k-> new ArrayList()).add(new Entry(timestamp, value));
        
    }
    
    public String get(String key, int timestamp) {
        List<Entry> entries = map.get(key);

        if(entries == null){
            return "";
        }

        int left =0;
        int right = entries.size() -1;
        String result ="";
        while(left<=right){
            int mid = (left +right)/2;

            if(entries.get(mid).timestamp<=timestamp){
                result = entries.get(mid).value;
                left =mid+1;
            }else{
                right =mid-1;
            }
        }
        return result;
    }
}
