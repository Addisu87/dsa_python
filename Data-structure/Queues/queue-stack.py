# Stack-based queues

class Queue:
   def __init__(self):
      self.Stack1 = []
      self.Stack2 = []
      
   # enqueue operation
   def enqueue(self, data):
      self.Stack1.append(data)
      
   # dequeue operation
   def dequeue(self):
      # check it's not empty
      if not self.Stack2:
         # if it is empty, all elements of Stack1 are moved to Stack2:
         while self.Stack1:
            self.Stack2.append(self.Stack1.pop())
      if not self.Stack2:
         print("No element to dequeue")
         return 
      return self.Stack2.pop()
      
# queue = Queue()
# queue.enqueue(23)
# queue.enqueue(13)
# queue.enqueue(11)
# print(queue.Stack1)


# queue.dequeue()
# print(queue.Stack2)


# Application of queues
from random import randint
import time

class Track:
   def __init__(self, title=None):
      self.title = title
      self.length = randint(5, 10)
   
      
      
# inheritance
class MediaPlayerQueue(Queue):
   def add_track(self, track):
      self.enqueue(track)
      self.count = 0
       
   def play(self):
      while self.count > 0:
         current_track_node = self.dequeue()
         print("Now playing {}".format(current_track_node.data.title))
         time.sleep(current_track_node.data.length)
      
track1 = Track("white whistle")
track2 = Track("butter butter")
track3 = Track("oh black star")
track4 = Track("Watch that chicken")
track5 = Track("Don't go")

print(track1.length)
print(track2.length)

media_player = MediaPlayerQueue()
media_player.add_track(track1)
media_player.add_track(track2)
media_player.add_track(track3)
media_player.add_track(track4)
media_player.add_track(track5)
media_player.play()
      

         
   