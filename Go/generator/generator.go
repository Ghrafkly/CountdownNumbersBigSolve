package generator

import (
	"fmt"

	"gonum.org/v1/gonum/stat/combin"
)

func Generator() {
	list := combin.Combinations(3, 5)

	for i, v := range list {
		fmt.Println(i, v)
	}
}
