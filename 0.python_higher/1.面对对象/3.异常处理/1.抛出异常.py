class EvenOnly(list):
    def append(self,integer):
        if not isinstance(integer,int):
            raise TypeError("Only integers can be added!")
        if integer%2:
            raise ValueError("Only Even numbers can be added!")
        super().append(integer)

if __name__ == '__main__':
    e=EvenOnly()
    try:
        try:
            e.append(2)
            e.append(4.6)

        except TypeError as err:
            print(err) #exception 也可以抛异常！   异常会被上一层接收,但是finally的错误会被首先捕捉
            e.append(5)
        finally:
            e.append(5) #finally 出异常 也会向外层抛异常
    except ValueError as err:
        print(err)
    except TypeError as err:
        print(err)