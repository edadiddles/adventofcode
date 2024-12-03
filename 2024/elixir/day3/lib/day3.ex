defmodule Day3 do
  def run(filename) do
    filename 
      |> File.read! 
      |> String.trim 
      |> String.split("\n")
      |> process
  end

  defp process(lines) do
    {r_process(lines, 0), 0}
  end

  defp r_process([], acc), do: acc
  defp r_process([line | tail], acc) do
    ln_sum = ~r/mul\([0-9]{1,3},[0-9]{1,3}\)/
      |> Regex.scan(line)
      |> Enum.map(fn x -> Enum.fetch!(x, 0) end)
      |> Enum.map(&extractTerms/1)
      |> Enum.sum

      r_process(tail, acc+ln_sum)
  end

  defp extractTerms(str) do
    str 
      |> String.replace("mul(", "") 
      |> String.replace(")", "") 
      |> String.split(",") 
      |> Enum.map(&String.to_integer/1)
      |> Enum.product
  end
end
