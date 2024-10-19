package main

import (
    "fmt"
    "os"
    "bufio"
    "strings"
    "strconv"
)


func main() {
    filename := os.Args[1]

    f, err := os.Open(filename)
    if err != nil {
        panic(err)
    }
    
    expects := map[string]int {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    var possGames []string
    var powGames []int
    scanner := bufio.NewScanner(f)
    for scanner.Scan() {
        line := scanner.Text()
        fmt.Println(string(line))

        minPoss := map[string]int {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        
        isImpossible := false
        // split by colon to get (Game ID, Game Played)
        gParts := strings.Split(string(line), ": ")
        gameId, game := gParts[0], gParts[1]

        sets := strings.Split(game, "; ")
        for i:=0; i < len(sets); i++ {
            set := sets[i]
            
            cubes := strings.Split(set, ", ")
            for j:=0; j < len(cubes); j++ {
                cubeParts := strings.Split(cubes[j], " ")
                
                numCube, err := strconv.Atoi(cubeParts[0])
                if err != nil {
                    fmt.Println(cubeParts[0])
                    panic(err)
                }

                colorCube := cubeParts[1]
                if expects[colorCube] < numCube {
                    isImpossible = true
                }

                if minPoss[colorCube] < numCube {
                    minPoss[colorCube] = numCube
                }

            }

        }

        if !isImpossible {
            id := strings.Replace(gameId, "Game ", "", 1)
            possGames = append(possGames, id)
        }
        
        powGames = append(powGames, minPoss["red"]*minPoss["green"]*minPoss["blue"])
        
    }

    sum := 0
    for i:= 0; i < len(possGames); i++ {
        id, err := strconv.Atoi(possGames[i])
        if err != nil {
            panic(err)
        }
        sum += id
    }

    sumPower := 0
    for i:=0; i<len(powGames); i++ {
        sumPower += powGames[i]
    }

    fmt.Println("Sum: ", sum)
    fmt.Println("Sum Power: ", sumPower)
}
