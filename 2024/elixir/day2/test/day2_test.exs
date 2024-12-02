defmodule Day2Test do
  use ExUnit.Case
  doctest Day2

  test "check solution against input0 (test) data" do
    {part1_soln, part2_soln} = Day2.run("input0.txt")
    assert {part1_soln, part2_soln} == {2, 0}
  end

   test "check solution against input1 (submission) data" do
    {part1_soln, part2_soln} = Day2.run("input1.txt")
    assert {part1_soln, part2_soln} == {402, 0}
  end
end
