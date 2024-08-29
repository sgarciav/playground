#include <opencv2/opencv.hpp>
#include <opencv2/aruco.hpp>
#include <opencv2/aruco/charuco.hpp>

// inline static bool readCameraParameters(const std::string& filename, cv::Mat &camMatrix, cv::Mat &distCoeffs) {
//     cv::FileStorage fs(filename, cv::FileStorage::READ);
//     if (!fs.isOpened())
//         return false;
//     fs["camera_matrix"] >> camMatrix;
//     fs["distortion_coefficients"] >> distCoeffs;
//     return true;
// }


int main(int argc, char** argv) {
  cv::VideoCapture inputVideo;
  inputVideo.open(0);
  cv::Mat cameraMatrix, distCoeffs;
  std::string filename = "calib.txt";

  // bool readOk = readCameraParameters(filename, cameraMatrix, distCoeffs);

  cv::Ptr<cv::aruco::Dictionary> dictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_5X5_250);
  cv::Ptr<cv::aruco::CharucoBoard> board = cv::aruco::CharucoBoard::create(5, 7, 0.035f, 0.026f, dictionary);
  cv::Ptr<cv::aruco::DetectorParameters> params = cv::aruco::DetectorParameters::create();
  while (inputVideo.grab()) {
    cv::Mat image;
    cv::Mat imageCopy;
    inputVideo.retrieve(image);
    image.copyTo(imageCopy);
    std::vector<int> markerIds;
    std::vector<std::vector<cv::Point2f> > markerCorners;
    cv::aruco::detectMarkers(image, board->dictionary, markerCorners, markerIds, params);
    // if at least one marker detected
    if (markerIds.size() > 0)
    {
      cv::aruco::drawDetectedMarkers(imageCopy, markerCorners, markerIds);
      std::vector<cv::Point2f> charucoCorners;
      std::vector<int> charucoIds;
      cv::aruco::interpolateCornersCharuco(markerCorners, markerIds, image, board, charucoCorners, charucoIds, cameraMatrix, distCoeffs);
      // if at least one charuco corner detected
      if (charucoIds.size() > 0)
      {
        cv::Scalar color = cv::Scalar(255, 0, 0);
        cv::aruco::drawDetectedCornersCharuco(imageCopy, charucoCorners, charucoIds, color);
        cv::Vec3d rvec, tvec;
        bool valid = cv::aruco::estimatePoseCharucoBoard(charucoCorners, charucoIds, board, cameraMatrix, distCoeffs, rvec, tvec);
        // if charuco pose is valid
        if (valid)
          cv::drawFrameAxes(imageCopy, cameraMatrix, distCoeffs, rvec, tvec, 0.1f);
      }
    }
    cv::imshow("out", imageCopy);
    char key = (char)cv::waitKey(30);
    if (key == 27)
    {
      break;
    }
  }
}
