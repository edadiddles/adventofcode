defmodule Day1Test do
  use ExUnit.Case
  doctest Day1

  test "runs sample file and validates part 1 (distance)" do
    {part1_soln, _} = Day1.run("input0.txt")
    assert part1_soln == 11
  end

  test "runs sample file and validates part 2 (similarity)" do
    {_, part2_soln} = Day1.run("input0.txt")
    assert part2_soln == 31
  end
end
