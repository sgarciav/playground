#include "ros/ros.h"
#include "std_msgs/String.h"
#include "beginner_tutorials/AddTwoInts.h"
#include <sstream>
#include <cstdlib>

// This tutorial demonstrates simple sending of messages over the ROS system.
// I think this code will be considered as the Publisher section of a node.

int main (int argc, char **argv)
{
  // initialize ROS. Third argument is the name of the node.
  ros::init(argc, argv, "talker");

  /*
    NodeHandle is the main access point to communications with the ROS system.
    This first call will fully initialize this node, and the last
    call will close down the node.
  */
  ros::NodeHandle node;

  /*
    The advertise() function is how you tell ROS that you want to publish
    on a given topic name. This invokes a call to the ROS master node, 
    which keeps a registry of who is publishing and who is subscribing.

    After this call is made, the master node will notify anyone who is trying
    to subscribe to this topic name, and they will negotiate with the node 
    publishing to the created topic.
  */
  ros::Publisher chatter_pub = node.advertise<std_msgs::String>("chatter", 1000);
  ros::Rate loop_rate(2);

  // let's try to get this talker to access the add_two_ints server
  beginner_tutorials::AddTwoInts srv;
  ros::ServiceClient client = node.serviceClient<beginner_tutorials::AddTwoInts>("add_two_ints");

  // placeholder | count how many messages have been sent
  int count = 1;
  int addme = 0;

  // while ROS is running I think
  while (ros::ok()) {

    // stuff this message object with data, and then publish it
    std_msgs::String msg;
    std::stringstream ss;
    ss << "Hello World: " << count;
    msg.data = ss.str();
    ROS_INFO("[Talker] I published: %s", msg.data.c_str());

    // if count is a multiplier of 10, ask the add_two_ints server to add 2 numbers
    if (count % 10 == 0) {
      addme++;
      srv.request.a = addme;
      srv.request.b = addme;

      if (client.call(srv)) {
	ROS_INFO("Sum: %ld", (long int)srv.response.sum);
	ss << "\nI asked the server to add " << addme << " with itself: " << srv.response.sum;
	msg.data = ss.str();
      }
      else {
	ROS_ERROR("Failed to call service add_two_ints");
	return 1;
      }
    }
    
    // send the message via ROS
    chatter_pub.publish(msg);

    // need to add this in case we add a subscription to this application
    ros::spinOnce();

    // keep track of the frequency rate we specified outside the loop (10Hz)
    loop_rate.sleep();
    ++count;
  }

  return 0;
}
