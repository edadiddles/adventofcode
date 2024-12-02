defmodule Day2 do
  def run(filename) do
    filename |> File.read! |> String.trim |> String.split("\n") |> checkReports({0, 0})
  end


  defp checkReports([], acc), do: acc
  defp checkReports([head | tail] = _reports, {part1_soln_acc, part2_soln_acc} = _acc) do
    checkReports(tail, {checkSafety(head |> String.trim) + part1_soln_acc, part2_soln_acc})
  end

  def checkSafety(report) do
    report 
      |> String.split(" ")
      |> Enum.map(fn x -> String.to_integer(x) end) 
      |> checkLevelsSorted 
      |> checkLevelsAdjacentDifference 
  end

  defp checkLevelsSorted(lvls) do
    cond do
      lvls == Enum.sort(lvls, :asc) -> lvls
      lvls == Enum.sort(lvls, :desc) -> lvls
      true -> []
    end
  end

  defp checkLevelsAdjacentDifference(lvls) do
    diff_list = calculateLevelsAdjacentDifference(lvls, [])
      
    diff_max = Enum.max(diff_list, &>=/2, fn -> 0 end)
    diff_min = Enum.min(diff_list, &<=/2, fn -> 0 end)

    if diff_max <= 3 and diff_min >= 1 do
      1
    else
      0
    end
  end

  defp calculateLevelsAdjacentDifference([], acc), do: acc
  defp calculateLevelsAdjacentDifference([_ | []], acc), do: acc
  defp calculateLevelsAdjacentDifference([lvl1, lvl2 | tail], acc) do 
    calculateLevelsAdjacentDifference([lvl2 | tail], [ abs(lvl1 - lvl2) | acc ])
  end
end
