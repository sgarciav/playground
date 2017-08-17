#include "ros/ros.h"
#include "beginner_tutorials/AddTwoInts.h"

// Note that the req and res variables are defined in the *.srv file we created earlier
bool add(beginner_tutorials::AddTwoInts::Request &req,
	 beginner_tutorials::AddTwoInts::Response &res)
{
  res.sum = req.a + req.b;
  ROS_INFO("you gave me: x=%ld, y=%ld", (long int)req.a, (long int)req.b);
  ROS_INFO("I give you: [%ld]", (long int)res.sum);
  return true;
}

// ----------------------------------------------

int main(int argc, char *argv[])
{
  // initialize ros
  ros::init(argc, argv, "add_two_ints_server");

  // initialize node
  ros::NodeHandle node;

  // advertise to ROS master that this node will be publishing info
  ros::ServiceServer service = node.advertiseService("add_two_ints", add);
  ROS_INFO("Ready to add two ints... just give me two numbers:");
  ros::spin();
  
  return 0;
}
