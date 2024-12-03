defmodule Day3 do
  def run(filename) do
    filename 
      |> File.read! 
      |> String.trim 
      |> process
  end

  defp process(input) do
    {p1_cnt, p2_cnt, _} = ~r/mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)/
      |> Regex.scan(input)
      |> Enum.map(fn x -> Enum.fetch!(x, 0) end)
      |> r_process({0, 0, 1})

    {p1_cnt, p2_cnt}
  end

  defp r_process([], acc), do: acc
  defp r_process([cmd | tail], {p1_cnt, p2_cnt, state_flg}) do
    cond do
      cmd == "don't()" -> r_process(tail, {p1_cnt, p2_cnt, 0})
      cmd == "do()" -> r_process(tail, {p1_cnt, p2_cnt, 1})
      state_flg == 0 -> s = cmd |> extractTerms

            r_process(tail, {p1_cnt+s, p2_cnt, state_flg})
      state_flg == 1 -> s = cmd |> extractTerms

            r_process(tail, {p1_cnt+s, p2_cnt+s, state_flg})
    end
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
