#include <Eigen/Dense>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <memory>

#include "opencv2/highgui.hpp"

#include "cmake_project/common/my_template_class.h"

int main(int argc, char *argv[]) {

  int img_num = 0;
  std::cout << "OpenCV Example Node. Saving image: " << img_num << std::endl << std::flush;

  // Create dummy image
  cv::Mat image(480, 640, CV_8UC3);
  std::string img_name = "Hello world " + std::to_string(img_num);
  cv::putText(image, img_name, cvPoint(320, 200),
              CV_FONT_HERSHEY_SIMPLEX, 1, cvScalar(255, 0, 0));

  // Create image file name with a time tag
  std::string base_save_dir = "/home/sergio/ros2/robotic_tray_processor/data/images";
  std::string images_dir = base_save_dir + "/classification_images";
  std::filesystem::create_directories(images_dir);

  // Save the image to file
  auto t = std::time(nullptr);
  auto tm = *std::localtime(&t);
  std::ostringstream oss;
  oss << std::put_time(&tm, "%Y-%m-%d_%H-%M-%S");
  auto time_str = oss.str();
  std::string image_path = images_dir + "/" + time_str + "_" + count + "_classification.bmp";
  cv::imwrite(image_path, *image);

  return 0;
}
