defmodule Day1 do
  def run(filename) do
    {_, contents} = filename |> File.read
    
    {sorted_list1, sorted_list2} = contents 
      |> String.trim 
      |> String.split("\n")
      |> Enum.reduce({[], []}, fn row, {l1, l2} = _acc ->
          [c1, c2 | []] = row |> String.split("   ")
          {[String.to_integer(c1) | l1], [String.to_integer(c2) | l2]}
        end)
      |> sort_lists_simultaneously
      

    part1_soln = r_difference_between_lists({sorted_list1, sorted_list2}, [])
      |> Enum.reduce(0, fn x, acc ->
          x+acc
        end)


    part2_soln = r_calculate_similarity(sorted_list1, sorted_list2, 0)

    {part1_soln, part2_soln}
  end


  defp sort_lists_simultaneously({list1, list2} = _list_tuple) do
    {Enum.sort(list1), Enum.sort(list2)}
  end

  defp r_difference_between_lists({[], []} = _list_tuple, acc), do: acc
  defp r_difference_between_lists({[head1 | tail1] = _list1, [head2 | tail2] = _list2} = _list_tuple, acc) do
    r_difference_between_lists({tail1, tail2}, [abs(head1 - head2) | acc])
  end

  defp r_calculate_similarity([], _, acc), do: acc
  defp r_calculate_similarity([head1| tail1], list2, acc) do
    num_repeats = Enum.reduce(list2, 0, fn item, acc ->
        if item == head1 do
          acc + 1
        else
          acc
        end
      end)

    r_calculate_similarity(tail1, list2, acc+(head1*num_repeats))
  end
end
