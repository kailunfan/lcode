package main

import "fmt"
import "sort"

func findRelativeRanks(score []int) []int {
	sortedScore := append([]int{}, score...)
	sort.Slice(sortedScore, func(i, j int) bool { return sortedScore[i] > sortedScore[j] })
	return sortedScore
}

func main(){
	fmt.Println(findRelativeRanks([]int{6,5,1,2,3}))
}
