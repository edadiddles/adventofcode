defmodule Day3Test do
  use ExUnit.Case
  doctest Day3

  @tag task_id: 1
  test "testcase input" do
    assert Day3.run("input0.txt") == {161, 48}
  end

  @tag task_id: 2
  test "puzzle input" do
    assert Day3.run("input1.txt") == {170068701, -1}
  end
end
