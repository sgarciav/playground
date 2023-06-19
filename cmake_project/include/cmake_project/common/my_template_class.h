template<typename T>
class MyTemplateClass
{
public:
  MyTemplateClass() {}

  T getA()
    {
      return a;
    }

  void setA(T value)
    {
      a = value;
    }

private:
  T a;
};
