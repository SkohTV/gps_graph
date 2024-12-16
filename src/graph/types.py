from typing import TypeAlias


# MODULARITY

Key: TypeAlias = int

Position: TypeAlias = tuple[float, float]
MaxSpeed: TypeAlias = tuple[int, int, int]
Distance: TypeAlias = float
Direction: TypeAlias = float

EdgeWay: TypeAlias = tuple[Key, MaxSpeed, Distance, Direction]
NodeWay: TypeAlias = tuple[Position, list[EdgeWay]]



Tags: TypeAlias = dict[str, str]
ClosestNode: TypeAlias = Key

Item: TypeAlias = tuple[Position, ClosestNode, Tags]
