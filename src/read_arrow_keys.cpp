#include <ncurses.h>
#include <iostream>
#include <string.h>

using namespace std;

int main (int argc, char *argv[])
{
  printf("this is a test... \n");
  
  // initialization
  initscr();
  cbreak();
  noecho();
  keypad(stdscr, TRUE);
  
  // declare variables
  int c = 0;
  printw("Enter a key... %d\n", c);
  while(1) {
    
    // read input
    c = getch();

    // do something depending on input key
    switch(c) {
    case KEY_UP:
      printw("Up\n");
      break;
    case KEY_DOWN:
      printw("Down\n");
      break;
    case KEY_LEFT:
      printw("Left\n");
      break;
    case KEY_RIGHT:
      printw("Right\n");
      break;
    default:
      printw("not an arrow\n");
      break;
    }
  }

  return 0;
}
