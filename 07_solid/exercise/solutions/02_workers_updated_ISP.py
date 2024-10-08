from abc import ABC, abstractmethod
import time


class AbstractWorker(ABC):
    # __metaclass__ = ABCMeta
    @staticmethod
    @abstractmethod
    def work():
        pass

    # @abstractmethod
    # def eat(self):
    #     pass


class Workable(AbstractWorker):

    @staticmethod
    def work():
        pass


class Eatable(AbstractWorker):

    @staticmethod
    @abstractmethod
    def eat():
        pass


class Worker(Workable, Eatable):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Workable, Eatable):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(Workable):

    def work(self):
        print("I'm a robot. I'm working....")

    # def eat(self):
    #     print("I don't need to eat....")


class Manager(ABC):

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, AbstractWorker), "`worker` must be of type {}".format(AbstractWorker)

        self.worker = worker

    # def manage(self):
    #     self.worker.work()

    # def lunch_break(self):
    #     self.worker.eat()


class WorkManager(Manager):
    def manage(self):
        self.worker.work()


class BreakManager(Manager):
    def lunch_break(self):
        self.worker.eat()


# manager = Manager()
# manager.set_worker(Worker())
# manager.manage()
# manager.lunch_break()
#
# manager.set_worker(SuperWorker())
# manager.manage()
# manager.lunch_break()
#
# manager.set_worker(Robot())
# manager.manage()
# manager.lunch_break()

work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass
