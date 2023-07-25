import rclpy
from rclpy.node import Node

class BugTest(Node):
    def __init__(self):
        super().__init__('bugtest')

        from rclpy.parameter import Parameter
        from rcl_interfaces.msg import ParameterDescriptor

        self.declare_parameter(
            name='test_param',
            value=None,
            ignore_override=False,
            descriptor=ParameterDescriptor(
                description = "URL to connect to GSC",
                type = Parameter.Type.STRING
            )
        )

def main(args=None):
    rclpy.init(args=args)
    bugtest = BugTest()
    rclpy.spin(bugtest)

    bugtest.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
