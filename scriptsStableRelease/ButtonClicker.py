from clicker import Application
#
#
# class Building:
#     def __init__(self, floors):
#         self._floors = floors
#
#     def __setitem__(self, atrName, data):
#         setattr(self, atrName, data)
#
#     def __getitem__(self,key):
#         print ("Inside `__getitem__` method!")
#         return getattr(self,key)
#
#
# building = Building("test")  # Construct a building with 4 floors
# building['_floors'] = 'changed'
# print(building['_floors'])

sylentapp = Application()
sylentapp.start()
