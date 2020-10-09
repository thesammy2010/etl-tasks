from typing import Any, Iterable, Optional, Union


class Ball(object):
    def __init__(
        self,
        position: float = 0,
        speed: float = 0,
        acceleration: float = 0,
        *args: Iterable[Any],
        **kwargs: Iterable[Any]
    ) -> None:

        # super().__init__(*args, **kwargs)

        if position < 0:
            raise Exception("Position cannot be negative")

        self.position = position
        self.speed = speed
        self.acceleration = acceleration

        self._position = position
        self._speed = speed
        self._acceleration = acceleration
        self.gravity: float = -9.81
        self.t: float = 0
        self.dt: float = 1

        while self.can_move():
            self.move()
            print(self)

    def __repr__(self) -> str:
        return "<Ball: Position {} m, Speed {} m/s, Acceleration {} m/s², Time {} s>".format(
            self._position, self._speed, self._acceleration, self.t
        )

    def can_move(self) -> bool:

        if self.position <= 0:
            print("Ball will not move")
            return False

        if self.acceleration + self.gravity >= 0:
            raise ValueError("Ball will never reach the ground")

        if self.speed > 3 * 10 ** 8:
            raise ValueError("Nothing can move faster that the speed of light")

        return True

    def move(self) -> None:

        # (s = ut + 1/2 at^2)
        self._position += 0.5 * (self.speed + self._speed) * self.dt
        self._speed += (self._acceleration + self.gravity) * self.dt
        self.t += self.dt

        self.position = self._position
        self.speed = self._speed
        self.acceleration = self._acceleration

    def is_moving(self) -> bool:
        if self._speed or self._acceleration:
            return True
        else:
            return False

    def set_position(self, position: Union[int, float]) -> None:
        setattr(self, "position", position)

    def set_speed(self, speed: Union[int, float]) -> None:
        setattr(self, "speed", speed)

    def set_acceleration(self, acceleration: Union[int, float]) -> None:
        setattr(self, "acceleration", acceleration)

    def get_position(self) -> Optional[float]:
        return self.position

    def get_speed(self) -> Optional[float]:
        return self.speed

    def get_acceleration(self) -> Optional[float]:
        return self.acceleration


def main() -> None:

    Ball(10)


if __name__ == "__main__":
    main()
