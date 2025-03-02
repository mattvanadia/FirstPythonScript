from types import new_class

def spill(func):
    def wrapper(s):
        if s.state_of_matter == 'liquid':
            print('The liquid will spill!')
        func(s)
    return wrapper

class Object:

    def __init__(self, size = 0, sound = 'Thud', name='', state_of_matter = 'solid'):
        self.size = size
        self.sound = sound
        self.name = name
        self.state_of_matter = state_of_matter

    def does_it_destroy(self):
        print(f'The {self.name} hits the floor with a loud {self.sound}.')
        if self.size >= 400:
            print('The floor is destroyed!')
        elif 200 <= self.size < 400:
            print('The floor is cracked!')
        else:
            print('The floor avoided damage!')

    def does_it_spill(self):
        if self.state_of_matter == 'solid':
            print('The object is solid, so it does not spill.')
        elif self.state_of_matter == 'liquid':
            print('Oh no! The object is liquid so it spilled.')
        elif self.state_of_matter == 'gas':
            print('The substance fills the room rapidly as it\'s container breaks open')
        else:
            print('Something went wrong. Try again.')


class BowlingBall(Object):

    def __init__(self, size = 0, sound = 'Clunk', name = 'Bowling Ball', state_of_matter = 'solid'):
        super().__init__(size=size, sound=sound, name=name, state_of_matter=state_of_matter)

    def set_size(self, t):
        self.size += t

class Marble(Object):

    def __init__(self, size = 0, sound = 'Ding', name = 'Marble', state_of_matter = 'solid'):
        super().__init__(size=size, sound=sound, name=name, state_of_matter=state_of_matter)

    def set_size(self, t):
        self.size += t

class Feather(Object):

    def __init__(self, size = 0, sound = 'Woosh', name = 'Feather', state_of_matter = 'solid'):
        super().__init__(size=size, sound=sound, name=name, state_of_matter=state_of_matter)

    def set_size(self, t):
        self.size += t

class Coffee(Object):

    def __init__(self, size = 0, sound = 'Crash', name = 'Cup of Coffee', state_of_matter = 'liquid'):
        super().__init__(size=size, sound=sound, name=name, state_of_matter=state_of_matter)

    def set_size(self, t):
        self.size += t

    @spill
    def spilled_coffee(self):
        return self.does_it_spill()


class UserSet(Object):

    def __init__(self, size = 0, sound = '', name = '', state_of_matter = ''):
        super().__init__(size=size, sound=sound, name=name, state_of_matter=state_of_matter)

    def set_size(self, t):
        self.size += t

    def set_sound(self, t):
        self.sound += t

    def set_name(self, t):
        self.name += t

    def set_state_of_matter(self, t):
        self.state_of_matter += t

    @spill
    def spilled_liquid(self):
        return self.does_it_spill()


object_bb = BowlingBall()
object_m = Marble()
object_f = Feather()
object_c = Coffee()
object_u = UserSet()


while True:

    n = input("Is your object a bowling ball, marble, feather, a cup of coffee, or something else?: ")
    t = int(input("How heavy is your object in pounds?: "))

    if n == 'bowling ball':
        object_bb.set_size(t)
        object_bb.does_it_destroy()
        object_bb.does_it_spill()
    elif n == 'marble':
        object_m.set_size(t)
        object_m.does_it_destroy()
        object_m.does_it_spill()
    elif n == 'feather':
        object_f.set_size(t)
        object_f.does_it_destroy()
        object_f.does_it_spill()
    elif n == 'cup of coffee':
        object_c.set_size(t)
        object_c.does_it_destroy()
        object_c.spilled_coffee()
    elif n == 'something else':
        a = input("What sound does your object make when it hits the floor?: ")
        b = input("What is your object?: ")
        c = input("Is your object a solid, liquid, or gas? Answer exactly as it is written here: ")
        object_u.set_size(t)
        object_u.set_sound(a)
        object_u.set_name(b)
        object_u.set_state_of_matter(c)
        object_u.does_it_destroy()
        object_u.spilled_liquid()
    else:
        print("You did not enter the word correctly.")
