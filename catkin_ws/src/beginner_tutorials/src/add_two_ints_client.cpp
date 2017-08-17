#include "ros/ros.h"
#include "beginner_tutorials/AddTwoInts.h"
#include <cstdlib>

int verify_me(ros::ServiceClient client, beginner_tutorials::AddTwoInts srv) {

  if (client.call(srv)) {
    ROS_INFO("Sum: %ld", (long int)srv.response.sum);
    return 0;
  }
  else {
    ROS_ERROR("Failed to call service add_two_ints");
    return 1;
  }
}  


// main function
int main(int argc, char *argv[])
{
  // number of inputs
  int num_inputs = argc-1;
  
  // initialize ros
  ros::init(argc, argv, "add_two_ints_client");

  // declare service variable
  beginner_tutorials::AddTwoInts srv;

  // initiaize node
  ros::NodeHandle node;
  ros::ServiceClient client = node.serviceClient<beginner_tutorials::AddTwoInts>("add_two_ints");
  
  // return index
  int ret_ind = 0;
  
  // call on server depending on number of inputs
  if (num_inputs == 2) {
    srv.request.a = atoi(argv[1]);
    srv.request.b = atoi(argv[2]);
    ret_ind = verify_me(client, srv);
  }
  else if (num_inputs == 0) {
    int x,y;
    x = -100; y = -100;
    ros::Rate loop_rate(1);
    while (ros::ok()) {
      x++; y++;
      srv.request.a = x;
      srv.request.b = y;
      loop_rate.sleep();
      ret_ind = verify_me(client, srv);
    }
  }
  else {
    ROS_INFO("usage: 2 inputs will run client once, no inputs will run it indefinitely");
    return 1;
  }

  return ret_ind;
}
