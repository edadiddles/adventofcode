defmodule Day4 do
  def run(filename) do
    filename
      |> File.read!
      |> String.trim
      |> String.split("\n")
      |> mapLines
      |> checks
  end

  def mapLines(lines) do
    {letter_map, _} = r_mapLines(lines, {%{x: [], m: [], a: [], s: []}, 0})
    letter_map
  end

  defp r_mapLines([], acc), do: acc
  defp r_mapLines([line | tail], {letter_map, line_num}) do
    {new_letter_map, _, _} = line
      |> String.trim
      |> String.split("")
      |> r_mapLetters({letter_map, line_num, 0})
    
    r_mapLines(tail, {new_letter_map, line_num+1})
  end

  defp r_mapLetters([], acc), do: acc
  defp r_mapLetters([letter | tail], {letter_map, line_num, letter_num}) do
    case letter do
      "X" -> r_mapLetters(tail, {%{letter_map | x: [{letter_num, line_num} | Map.fetch!(letter_map, :x)]}, line_num, letter_num + 1})
      "M" -> r_mapLetters(tail, {%{letter_map | m: [{letter_num, line_num} | Map.fetch!(letter_map, :m)]}, line_num, letter_num + 1})
      "A" -> r_mapLetters(tail, {%{letter_map | a: [{letter_num, line_num} | Map.fetch!(letter_map, :a)]}, line_num, letter_num + 1})
      "S" -> r_mapLetters(tail, {%{letter_map | s: [{letter_num, line_num} | Map.fetch!(letter_map, :s)]}, line_num, letter_num + 1})
      _ -> r_mapLetters(tail, {letter_map, line_num, letter_num+1})
    end
  end

  defp checks(letter_map) do
    p1_sol = checkXMAS(letter_map)
    p2_sol = checkCrossMAS(letter_map)
    {p1_sol, p2_sol}
  end

  defp checkXMAS(letter_map) do
    r_checkXMAS(letter_map, {:x, nil, nil})
  end

  defp r_checkXMAS(letter_map, {_, nil, nil}) do
    letter_map 
      |> Map.fetch!(:x) 
      |> Enum.reduce(0, fn {x, y}, acc -> 
          directions()
            |> Enum.reduce(0, fn dir, acc -> r_checkXMAS(letter_map, {:x, {x, y}, dir}) + acc end)
            |> Kernel.+(acc)
        end)

  end
  defp r_checkXMAS(letter_map, {curr_letter, {x0, y0}, {xd, yd}}) do
    case curr_letter do
      :x -> letter_map 
              |> Map.fetch!(:m) 
              |> Enum.filter(fn {x, y} -> x0+xd == x and y0+yd == y end) 
              |> Enum.reduce(0, fn coord, acc -> r_checkXMAS(letter_map, {:m, coord, {xd, yd}}) + acc end) 
      :m -> letter_map
              |> Map.fetch!(:a) 
              |> Enum.filter(fn {x, y} -> x0+xd == x and y0+yd == y end) 
              |> Enum.reduce(0, fn coord, acc -> r_checkXMAS(letter_map, {:a, coord, {xd, yd}}) + acc end)
      :a -> letter_map
              |> Map.fetch!(:s) 
              |> Enum.filter(fn {x, y} -> x0+xd == x and y0+yd == y end) 
              |> Enum.reduce(0, fn coord, acc -> r_checkXMAS(letter_map, {:s, coord, {xd, yd}}) + acc end)

      :s -> 1
    end
  end

  defp checkCrossMAS(letter_map) do
    letter_map 
      |> Map.fetch!(:a)
      |> Enum.reduce(0, fn {x, y}, acc ->
          cnt = diaganols()
            |> Enum.reduce(0, fn {xd, yd}, acc -> r_checkXMAS(letter_map, {:x, {x+(-2*xd), y+(-2*yd)}, {xd, yd}}) + acc end)

          case cnt do
            2 -> 1 + acc
            _ -> acc
          end
        end)
  end

  defp directions do
    [{0, 1}, {0, -1}, {1, 0}, {-1, 0} | diaganols()]
  end

  defp diaganols do
    [{1, 1}, {-1, 1}, {1, -1}, {-1, -1}]
  end
end
