# EDIT THE FILE WITH YOUR SOLUTION

import itertools
import numpy as np


class PolygonsError(Exception):
    pass


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    def __lt__(self, other: "Point") -> bool:
        return self.x < other.x or (self.x == other.x and self.y < other.y)

    def __eq__(self, other: "Point") -> bool:
        return self.x == other.x and self.y == other.y

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


class Distance:
    def __init__(self, mul_1: float, mul_r2: float) -> None:
        self.mul_1: float = mul_1
        self.mul_r2: float = mul_r2

    def __add__(self, other: "Distance") -> "Distance":
        return Distance(self.mul_1 + other.mul_1, self.mul_r2 + other.mul_r2)


def point_distance(point_a: Point, point_b: Point) -> Distance:
    distance_x = abs(point_a.x - point_b.x)
    distance_y = abs(point_a.y - point_b.y)
    return Distance(abs(distance_x - distance_y), min(distance_x, distance_y))


def calc_perimeter(points: list[Point]) -> Distance:
    distance = Distance(0, 0)
    for point_a, point_b in zip(points, [*points[1:], points[0]]):
        distance += point_distance(point_a, point_b)
    return distance


def calc_area(points: list[Point]) -> float:
    x_list = [p.x for p in points]
    y_list = [p.y for p in points]
    return 0.5 * abs(
        sum([x * y for x, y in zip(x_list, [*y_list[1:], y_list[0]])])
        - sum([x * y for x, y in zip([*x_list[1:], x_list[0]], y_list)])
    )


def judge_convex(points: list[Point]) -> bool:
    directions = [pa - pb for pa, pb in zip(points, [*points[1:], points[0]])]
    cross_result_list = [
        da.x * db.y - da.y * db.x
        for da, db in zip(directions, [*directions[1:], directions[0]])
    ]
    direction_list = [
        cross_result > 0 for cross_result in cross_result_list if cross_result != 0
    ]
    return all(direction_list) or not any(direction_list)


def calc_number_of_invariant_rotations(points: list[Point]) -> int:
    center = Point(
        sum([p.x for p in points]) / len(points),
        sum([p.y for p in points]) / len(points),
    )
    points_recenter = {p - center for p in points}
    rotate_90 = {Point(-p.y, p.x) for p in points_recenter}
    rotate_180 = {Point(-p.x, -p.y) for p in points_recenter}
    is_rotate_90_invariant = len(rotate_90 - points_recenter) == 0
    is_rotate_180_invariant = len(rotate_180 - points_recenter) == 0
    if is_rotate_90_invariant and is_rotate_180_invariant:
        return 4
    elif not is_rotate_90_invariant and is_rotate_180_invariant:
        return 2
    elif is_rotate_90_invariant and not is_rotate_180_invariant:
        raise RuntimeError("impossible")
    else:
        return 1


def is_neighbor_4(point_a: Point, point_b: Point):
    distance = point_distance(point_a, point_b)
    return distance.mul_1 == 1 and distance.mul_r2 == 0


def is_neighbor_8(point_a: Point, point_b: Point):
    distance = point_distance(point_a, point_b)
    return (distance.mul_1 == 1 and distance.mul_r2 == 0) or (
        distance.mul_1 == 0 and distance.mul_r2 == 1
    )


def is_collinear(*points: Point) -> bool:
    directions = [pa - pb for pa, pb in zip(points, [*points[1:], points[0]])]
    return all(
        [
            da.x * db.y - da.y * db.x == 0
            for da, db in zip(directions, [*directions[1:], directions[0]])
        ]
    )


class Polygon:
    def __init__(self, points: list[Point], depth: int) -> None:
        self.points: list[Point] = points
        self.perimeter: Distance = calc_perimeter(self.points)
        self.area: float = calc_area(self.points)
        self.convex: bool = judge_convex(self.points)
        self.number_of_invariant_rotations: int = calc_number_of_invariant_rotations(
            self.points
        )
        self.depth: int = depth

    def __lt__(self, other: "Polygon") -> bool:
        return self.points < other.points

    def output(self, unit: float) -> dict[str, str]:
        return {
            "perimeter": " + ".join(
                filter(
                    lambda e: e,
                    (
                        f"{self.perimeter.mul_1 * unit:.1f}"
                        if self.perimeter.mul_1
                        else "",
                        f"{self.perimeter.mul_r2}*sqrt({f'{2 * unit * unit:g}'.lstrip('0')})"
                        if self.perimeter.mul_r2
                        else "",
                    ),
                )
            ),
            "area": f"{self.area * unit * unit:.2f}",
            "convex": f"{'yes' if self.convex else 'no'}",
            "number_of_invariant_rotations": f"{self.number_of_invariant_rotations}",
            "depth": f"{self.depth}",
        }


def read_data(filename: str):
    file_input = open(filename)
    data = []
    for line in file_input.readlines():
        row = []
        for c in line.strip():
            if c == "0":
                row.append(0)
            elif c == "1":
                row.append(1)
            elif c == " ":
                continue
            else:
                raise PolygonsError("Incorrect input.")
        if not row:
            continue
        if len(data) == 0:
            data.append(row)
        else:
            if len(row) == len(data[-1]):
                data.append(row)
            else:
                PolygonsError("Incorrect input.")
    data = np.array(data, dtype=np.uint8)
    if not 2 <= data.shape[0] <= 50 or not 2 <= data.shape[1] <= 50:
        raise PolygonsError("Incorrect input.")
    return data


class Polygons:
    def __init__(self, filename: str):
        self.name: str = filename.rsplit(".", 1)[0]
        self.data: np.ndarray = read_data(filename)
        self.polygons: list[Polygon] = self.initial()

    def initial(self) -> list[Polygon]:
        """
        0: empty
        1: point
        2: used
        """
        data = (
            np.ones((self.data.shape[0] + 2, self.data.shape[1] + 2), dtype=np.uint8)
            * 2
        )
        data[1:-1, 1:-1] = self.data
        polygons: list[Polygon] = []
        depth = 0
        while (data != 2).any():
            while True:
                has_modify = False
                for x, y in itertools.product(
                    range(1, data.shape[0] - 1), range(1, data.shape[1] - 1)
                ):
                    if data[x, y] == 0 and any(
                        [
                            data[_x, _y] == 2
                            for _x, _y in [
                                (x - 1, y),
                                (x, y + 1),
                                (x + 1, y),
                                (x, y - 1),
                            ]
                        ]
                    ):
                        data[x, y] = 2
                        has_modify = True
                if not has_modify:
                    break
            outer_points = {
                Point(x, y)
                for x, y in itertools.product(
                    range(1, data.shape[0] - 1), range(1, data.shape[1] - 1)
                )
                if data[x, y] == 1
                and any(
                    [
                        data[_x, _y] == 2
                        for _x, _y in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
                    ]
                )
            }
            while outer_points:
                curr_point = min(outer_points)
                last_point = Point(curr_point.x - 1, curr_point.y + 1)
                outer_points.remove(curr_point)
                choiced_points = [curr_point]
                while True:
                    neighbors = [
                        Point(curr_point.x, curr_point.y + 1),
                        Point(curr_point.x + 1, curr_point.y + 1),
                        Point(curr_point.x + 1, curr_point.y),
                        Point(curr_point.x + 1, curr_point.y - 1),
                        Point(curr_point.x, curr_point.y - 1),
                        Point(curr_point.x - 1, curr_point.y - 1),
                        Point(curr_point.x - 1, curr_point.y),
                        Point(curr_point.x - 1, curr_point.y + 1),
                    ]
                    start_cursor = neighbors.index(last_point)
                    for i in range(1, 8):
                        next_point = neighbors[(start_cursor + i) % 8]
                        if next_point in outer_points and (
                            data[int(curr_point.x), int(next_point.y)] != 2
                            or data[int(next_point.x), int(curr_point.y)] != 2
                        ):
                            last_point = curr_point
                            curr_point = next_point
                            outer_points.remove(next_point)
                            choiced_points.append(next_point)
                            break
                    else:
                        break
                if (
                    is_neighbor_8(choiced_points[0], choiced_points[-1])
                    and any(
                        (
                            data[int(choiced_points[0].x), int(choiced_points[-1].y)]
                            != 2,
                            data[int(choiced_points[-1].x), int(choiced_points[0].y)]
                            != 2,
                        )
                    )
                    and len(choiced_points) >= 3
                ):
                    for p in choiced_points:
                        data[int(p.x), int(p.y)] = 2
                    polygons.append(
                        Polygon(
                            [
                                Point(p.x - 1, p.y - 1)
                                for i, p in enumerate(choiced_points)
                                if not is_collinear(
                                    choiced_points[
                                        (i + len(choiced_points) - 1)
                                        % len(choiced_points)
                                    ],
                                    p,
                                    choiced_points[(i + 1) % len(choiced_points)],
                                )
                            ],
                            depth,
                        )
                    )
                else:
                    raise PolygonsError("Cannot get polygons as expected.")
            depth += 1
        return sorted(polygons)

    def analyse(self):
        for idx, polygon in enumerate(self.polygons, start=1):
            output = polygon.output(0.4)
            print(f"Polygon {idx}:")
            print(f"    Perimeter: {output['perimeter']}")
            print(f"    Area: {output['area']}")
            print(f"    Convex: {output['convex']}")
            print(
                f"    Nb of invariant rotations: {output['number_of_invariant_rotations']}"
            )
            print(f"    Depth: {output['depth']}")

    def display(self):
        with open(f"sol_{self.name}.tex", "w") as fout:
            fout.write("\\documentclass[10pt]{article}\n")
            fout.write("\\usepackage{tikz}\n")
            fout.write("\\usepackage[margin=0cm]{geometry}\n")
            fout.write("\\pagestyle{empty}\n")
            fout.write("\n")
            fout.write("\\begin{document}\n")
            fout.write("\n")
            fout.write("\\vspace*{\\fill}\n")
            fout.write("\\begin{center}\n")
            fout.write("\\begin{tikzpicture}[x=0.4cm, y=-0.4cm, thick, brown]\n")
            fout.write(
                f"\\draw[ultra thick] (0, 0) -- ({self.data.shape[1] - 1}, 0) -- ({self.data.shape[1] - 1}, {self.data.shape[0] - 1}) -- (0, {self.data.shape[0] - 1}) -- cycle;\n\n"
            )
            area_list = [polygon.area for polygon in self.polygons]
            max_area = max(area_list)
            min_area = min(area_list)
            diff_area = max_area - min_area
            last_depth = -1
            for polygon in sorted(
                self.polygons, key=lambda polygon: (polygon.depth, polygon.points)
            ):
                if polygon.depth != last_depth:
                    fout.write(f"% Depth {polygon.depth}\n")
                    last_depth = polygon.depth
                fout.write(
                    f"\\filldraw[fill=orange!{round((max_area - polygon.area) / diff_area * 100)}!yellow] {' -- '.join([f'({p.y}, {p.x})' for p in polygon.points])} -- cycle;\n"
                )
            fout.write("\\end{tikzpicture}\n")
            fout.write("\\end{center}\n")
            fout.write("\\vspace*{\\fill}\n")
            fout.write("\n")
            fout.write("\\end{document}\n")
