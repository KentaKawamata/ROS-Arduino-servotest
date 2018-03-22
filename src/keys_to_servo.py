#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt16
from geometry_msgs.msg import Twist
#import Servo

key_mapping = { 'z': 0, 'x': 90, 'a': 180 }

def keys_cb(msg, twist_pub):

  if len(msg.data) == 0 or not key_mapping.has_key(msg.data):
    return # unknown key.

  vels = key_mapping[msg.data]

  t = UInt16()
  t = vels
  publisher.publish(t)

if __name__ == '__main__':

  rospy.init_node('keys_to_servo')
  publisher = rospy.Publisher('servo', UInt16, queue_size=1)
  rospy.Subscriber('keys', String, keys_cb, publisher)
  rospy.spin()
