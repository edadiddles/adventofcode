defmodule Day4Test do
  use ExUnit.Case
  doctest Day4
  
  @tag task_id: 1
  test "example input 1" do
    assert Day4.run("data_ex.in") == {18, 9}
  end

  @tag task_id: 2
  test "puzzle input" do
    assert Day4.run("data.in") == {2344, 1815}
  end
end
