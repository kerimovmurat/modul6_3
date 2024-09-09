class Horse ():
    """ класс описывающий лошадь """

    x_distance = 0
    _sound = "Frrr"

    def run(self, dx):
        self.x_distance += dx


class Eagle ():
    ''' rкласс описывающий орла'''
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus ( Horse, Eagle ):
    '''класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
Объект такого класса должен обладать атрибутами классов родителей в порядке наследования.'''

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


p1 = Pegasus ()

print ( p1.get_pos () )
p1.move ( 10, 15 )
print ( p1.get_pos () )
p1.move ( -5, 20 )
print ( p1.get_pos () )

p1.voice ()

horse = Horse()
horse.run(5)
print(horse.run(5))
# p1 = Pegasus
#
# # print ( p1.get_pos () )
# p1.move ( 10, 15)
# print ( p1.get_pos () )
# p1.move ( -5, 20 )
# print ( p1.get_pos () )
#
# p1.voice ()

