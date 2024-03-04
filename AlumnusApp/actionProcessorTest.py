# Test for ActionProcessor
from ActionProcessor.ActionProcessor import ActionProcessor
from User.User import User

actionProcessor = ActionProcessor()
roomList = actionProcessor.getRooms()
print(roomList)

actionProcessor.deleteRoom('45')

actionProcessor.addRoom({'roomid': '45', 'roomdesc': 'Room 45'})