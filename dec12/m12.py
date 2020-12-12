class Ship():

    def __init__(self):
        self.direction = 90  # 0 = North, 90 = East
        self.position = [0, 0]

    def move(self, instr: str):
        cmd, value = instr[0], int(instr[1:])
        if cmd == 'L':
            self.direction = (self.direction - value) % 360
        elif cmd == 'R':
            self.direction = (self.direction + value) % 360
        elif cmd == 'F':
            if self.direction == 0:
                self.position[1] += value
            elif self.direction == 90:
                self.position[0] += value
            elif self.direction == 180:
                self.position[1] -= value
            elif self.direction == 270:
                self.position[0] -= value
            else:
                raise ValueError("Bad direction %d", self.direction)
        elif cmd == "N":
            self.position[1] += value
        elif cmd == "E":
            self.position[0] += value
        elif cmd == "S":
            self.position[1] -= value
        elif cmd == "W":
            self.position[0] -= value
        else:
            raise ValueError("Unknown cmd %s" % cmd)


class ShipWithWaypoint():

    def __init__(self):
        self.position = [0, 0]
        self.waypoint = [10, 1]

    def move(self, instr: str):
        cmd, value = instr[0], int(instr[1:])
        if cmd == 'L':
            angle = (360 - value)
            self.rotate_waypoint(angle)
        elif cmd == 'R':
            self.rotate_waypoint(value)
        elif cmd == 'F':
            self.position[0] += value * self.waypoint[0]
            self.position[1] += value * self.waypoint[1]
        elif cmd == "N":
            self.waypoint[1] += value
        elif cmd == "E":
            self.waypoint[0] += value
        elif cmd == "S":
            self.waypoint[1] -= value
        elif cmd == "W":
            self.waypoint[0] -= value
        else:
            raise ValueError("Unknown cmd %s" % cmd)

    def rotate_waypoint(self, angle: int):
        rotaded_waypoint = [0, 0]
        if angle == 90:
            rotaded_waypoint[0] = self.waypoint[1]
            rotaded_waypoint[1] = -self.waypoint[0]
        elif angle == 180:
            rotaded_waypoint[0] = -self.waypoint[0]
            rotaded_waypoint[1] = -self.waypoint[1]
        elif angle == 270:
            rotaded_waypoint[0] = -self.waypoint[1]
            rotaded_waypoint[1] = self.waypoint[0]
        self.waypoint = rotaded_waypoint


def main():
    with open('input.txt') as ifh:
        steps = ifh.read().splitlines()
    ship = Ship()
    for step in steps:
        ship.move(step)
        # print(ship.position)
    end_pos = ship.position
    m_dist = abs(end_pos[0]) + abs(end_pos[1])
    print(f"First Manhattan distance is {m_dist}\n")
    ship = ShipWithWaypoint()
    for step in steps:
        ship.move(step)
        # print(ship.position)
    end_pos = ship.position
    m_dist = abs(end_pos[0]) + abs(end_pos[1])
    print(f"Second Manhattan distance is {m_dist}\n")


if __name__ == "__main__":
    main()
