
import argparse
import sys
from time import sleep
import uuid

import rclpy

from rmf_task_msgs.msg import Loop

def main(argv = sys.argv):
    rclpy.init(args=argv)

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start', help='Start waypoint')
    parser.add_argument('-f', '--finish', help='Finish waypoint')
    parser.add_argument('-n', '--num', help='Number of loops to perform', type=int, default=1)
    parser.add_argument('-i', '--task-id', help='Task ID', default='', type=str)
    parser.add_argument('-r', '--robot-type', help='Type of robot', default='mir')

    args = parser.parse_args(argv[1:])

    node = rclpy.create_node('loop_request_publisher')
    publisher = node.create_publisher(Loop, 'loop_requests', 10)

    sleep(0.5)

    request = Loop()
    request.robot_type = args.robot_type
    request.start_name = args.start
    request.finish_name = args.finish
    request.num_loops = args.num
    if args.task_id:
        request.task_id = args.task_id
    else:
        request.task_id = 'loop#' + str(uuid.uuid1())

    for _ in range(5):
        publisher.publish(request)
        sleep(0.5)

    rclpy.shutdown()


    print(f'I will submit a loop request!')

if __name__ == '__main__':
    main(sys.argv)
