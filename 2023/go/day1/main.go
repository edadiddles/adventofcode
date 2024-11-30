package main

import(
    "fmt"
    "os"
    "bufio"
    "log"
    "strings"
    "strconv"
)

func main() {
    f, err := os.Open("data.in")
    if err != nil {
        panic(err)
    }
    defer f.Close()

    resSlice := make([]int, 100)
    scanner := bufio.NewScanner(f)
    for scanner.Scan() {
        line := scanner.Text()
        bottom := 0
        top := len(line)-1
        // find first instance
        bottomNum := -1
        for ; bottom < len(line); bottom++ {
            currChar := string(line[bottom])
            if strings.ContainsAny(currChar, "1234567890") {
                bottomNum, err = strconv.Atoi(currChar)
                if err != nil {
                    panic(err)
                }
                bottomNum *= 10
                break
            } else if strings.Contains(currChar, "o") {
                if bottom+3 <= len(line) && strings.Contains(string(line[bottom:bottom+3]), "one") {
                    bottomNum = 1*10
                    break
                }
            } else if strings.Contains(currChar, "t") { 
                if bottom+3 <= len(line) && strings.Contains(string(line[bottom:bottom+3]), "two") {
                    bottomNum = 2*10
                    break
                } else if bottom+5 <= len(line) && strings.Contains(string(line[bottom:bottom+5]), "three") {
                    bottomNum = 3*10
                    break
                }
            } else if strings.Contains(currChar, "f") {
                if bottom+4 <= len(line) && strings.Contains(string(line[bottom:bottom+4]), "four") {
                    bottomNum = 4*10
                    break
                } else if bottom+4 <= len(line) && strings.Contains(string(line[bottom:bottom+4]), "five") {
                    bottomNum = 5*10
                    break
                }
            } else if strings.Contains(currChar, "s") {
                if bottom+3 <= len(line) && strings.Contains(string(line[bottom:bottom+3]), "six") {
                    bottomNum = 6*10
                    break
                } else if bottom+5 <= len(line) && strings.Contains(string(line[bottom:bottom+5]), "seven") {
                    bottomNum = 7*10
                    break
                }
            } else if strings.Contains(currChar, "e") {
                if bottom+5 <= len(line) && strings.Contains(string(line[bottom:bottom+5]), "eight") {
                    bottomNum = 8*10
                    break
                }
            } else if strings.Contains(currChar, "n") {
                if bottom+4 <= len(line) && strings.Contains(string(line[bottom:bottom+4]), "nine") {
                    bottomNum = 9*10
                    break
                }
            }

        }

        // find last instance
        topNum:= -1
        for ; top >= bottom; top-- {
            currChar := string(line[top])
            if strings.ContainsAny(currChar, "1234567890") {
                topNum, err = strconv.Atoi(currChar)
                if err != nil {
                    panic(err) 
                }
                break
            } else if strings.Contains(currChar, "e") {
                if top-2 > 0 && strings.Contains(string(line[top-2:top+1]), "one") {
                    topNum = 1
                    break
                } else if top-4 > 0 && strings.Contains(string(line[top-4:top+1]), "three") {
                    topNum = 3
                    break
                } else if top-3 > 0 && strings.Contains(string(line[top-3:top+1]), "five") {
                    topNum = 5
                    break
                } else if top-3 > 0 && strings.Contains(string(line[top-3:top+1]), "nine") {
                    topNum = 9
                    break
                }
            } else if strings.Contains(currChar, "o") { 
                if top-2 > 0 && strings.Contains(string(line[top-2:top+1]), "two") {
                    topNum = 2
                    break
                }
            } else if strings.Contains(currChar, "r") {
                if top-3 > 0 && strings.Contains(string(line[top-3:top+1]), "four") {
                    topNum = 4
                    break
                }
            } else if strings.Contains(currChar, "x") {
                if top-2 > 0 && strings.Contains(string(line[top-2:top+1]), "six") {
                    topNum = 6
                    break
                }
            } else if strings.Contains(currChar, "t") {
                if top-4 > 0 && strings.Contains(string(line[top-4:top+1]), "eight") {
                    topNum = 8
                    break
                }
            } else if strings.Contains(currChar, "n") {
                if top-4 > 0 && strings.Contains(string(line[top-4:top+1]), "seven") {
                    topNum = 7
                    break
                }
            }
        }
        fmt.Println(bottomNum+topNum)
        if bottomNum == -1 || topNum == -1 {
            panic("number not found in line")
        }
        resSlice = append(resSlice, bottomNum+topNum)
    }
    
    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

    sum := 0
    for i:=0; i < len(resSlice); i++ {
        sum+= resSlice[i]
    }

    fmt.Println("Sum: ", sum)
}
