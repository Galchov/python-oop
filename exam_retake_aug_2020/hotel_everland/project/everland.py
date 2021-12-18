from project.rooms.room import Room
from project.people.child import Child


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost
        return f"Monthly consumptions: {total_consumption:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            total_cost = room.expenses + room.room_cost
            if room.budget >= total_cost:
                room.budget -= total_cost
                result.append(f'{room.family_name} paid {total_cost:.2f}$ and have {room.budget:.2f}$ left.')
            else:
                self.rooms.remove(room)
                result.append(f'{room.family_name} does not have enough budget and must leave the hotel.')

        return '\n'.join(result)

    def status(self):
        result = ''

        result += f'Total population: {sum([r.members_count for r in self.rooms])}\n'
        for room in self.rooms:
            result += f'{room.family_name} with {room.members_count} members. ' \
                      f'Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n'
            if room.children:
                counter = 0
                for child in room.children:
                    counter += 1
                    result += f'--- Child {counter} monthly cost: {(child.cost * 30):.2f}$\n'
            if hasattr(room, 'appliances'):
                total_expenses = 0
                for app in room.appliances:
                    total_expenses += app.get_monthly_expense()
                result += f'--- Appliances monthly cost: {total_expenses:.2f}$\n'

        return result
