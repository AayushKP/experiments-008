package main

import "fmt"

func main(){
	i:=1
	for i<=3{
		fmt.Println(i)
		i = i+1
	}
	fmt.Printf("\n")

	for j:=0;j<3;j++ {
		fmt.Println(j)
	}
	fmt.Printf("\n")

	for i:= range 3{
		fmt.Println(i)
	}
	fmt.Printf("\n")

	for {
		fmt.Println("loop")
		break
	}
	fmt.Printf("\n")

	for n:= range 6{
		if n%2 == 0 {
			continue
		}
		fmt.Println(n)
	}
}
