from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = {"MainService": MainService, "SecondaryService": SecondaryService}
    VALID_ROBOTS = {"FemaleRobot": FemaleRobot, "MaleRobot": MaleRobot}

    def __init__(self) -> None:
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def __str__(self) -> str:
        return "\n".join(s.details() for s in self.services)

    def add_service(self, service_type: str, name: str) -> str or Exception:
        if self.VALID_SERVICES.get(service_type):
            service_object = self.VALID_SERVICES[service_type](name)
            self.services.append(service_object)
            return f"{service_type} is successfully added."
        raise Exception("Invalid service type!")

    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str or Exception:
        if self.VALID_ROBOTS.get(robot_type):
            robot_object = self.VALID_ROBOTS[robot_type](name, kind, price)
            self.robots.append(robot_object)
            return f"{robot_type} is successfully added."
        raise Exception("Invalid robot type!")

    def add_robot_to_service(self, robot_name: str, service_name: str) -> str or Exception:
        robot = next((r for r in self.robots if r.name == robot_name), None)
        service = next((s for s in self.services if s.name == service_name), None)

        if isinstance(robot, MaleRobot) and not isinstance(service, MainService):
            return "Unsuitable service."
        if isinstance(robot, FemaleRobot) and not isinstance(service, SecondaryService):
            return "Unsuitable service."

        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str) -> str or Exception:
        service = next((s for s in self.services if s.name == service_name), None)
        robot = next((r for r in service.robots if r.name == robot_name), None)

        if robot is None:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str) -> str:
        service = next((s for s in self.services if s.name == service_name), None)
        [r.eating() for r in service.robots]
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str) -> str:
        service = next((s for s in self.services if s.name == service_name), None)
        total_robots_price = sum(r.price for r in service.robots)
        return f"The value of service {service_name} is {total_robots_price:.2f}."
