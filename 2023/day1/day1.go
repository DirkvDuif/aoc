package main

import (
	"fmt"
	"os"
	"regexp"
	"sort"
	"strconv"
	"strings"
	"time"
	"unicode"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

var stringNumbers = map[string]string{
	"one":   "1",
	"two":   "2",
	"three": "3",
	"four":  "4",
	"five":  "5",
	"six":   "6",
	"seven": "7",
	"eight": "8",
	"nine":  "9",
}

func main() {
	data, err := os.ReadFile("input.txt")
	check(err)

	var lines []string = strings.Split(string(data), "\n")

	start := time.Now()

	// Compile regular expressions once outside the loop
	regexps := make(map[string]*regexp.Regexp)
	for k := range stringNumbers {
		regexps[k] = regexp.MustCompile(k)
	}

	var total int64 = 0
	posNumbers := make(map[int]string)
	positions := make([]int, 0, len(lines))

	for _, line := range lines {
		// Clear maps and slices for reuse
		for k := range posNumbers {
			delete(posNumbers, k)
		}
		positions = positions[:0]

		for k, v := range stringNumbers {
			matches := regexps[k].FindAllIndex([]byte(line), -1)
			for _, match := range matches {
				posNumbers[match[0]] = v
			}
		}

		for idx, c := range line {
			if unicode.IsDigit(c) {
				posNumbers[idx] = string(c)
			}
		}

		for k := range posNumbers {
			positions = append(positions, k)
		}

		sort.Ints(positions)

		fst := posNumbers[positions[0]]
		lst := posNumbers[positions[len(positions)-1]]

		numberString := fst + lst
		number, _ := strconv.ParseInt(numberString, 10, 32)
		// handle err
		total += number
	}

	fmt.Println("Total:", total)
	fmt.Println("Time:", time.Since(start))
}
