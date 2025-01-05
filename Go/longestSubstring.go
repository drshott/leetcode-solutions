func lengthOfLongestSubstring(s string) int {
    myMap := make(map[byte]int)
	maxLen := 0
	lptr := 0
	rptr := 0
	for rptr < len(s) {
		if index, exists := myMap[s[rptr]]; exists {
			lptr = max(lptr, index+1)
		}
		myMap[s[rptr]] = rptr
		maxLen = max(maxLen, rptr-lptr+1)
		rptr++
	}
	return maxLen
}