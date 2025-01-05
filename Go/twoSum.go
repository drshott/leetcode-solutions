func twoSum(nums []int, target int) []int {
    myMap := make(map[int]int)
	for i, num := range nums {
		complement := target - num
		if index, exists := myMap[complement]; exists {
            return []int{index, i}
		}
		myMap[num] = i
    }
    return nil
}