import turtle as t

t.speed(0)
t.setup(width=400, height=400) #크기설정
t.screensize( 10,10 ,'#959C9C') # 바탕색 

def move(x,y): #원하는 위치로 이동
    t.pu()
    t.home()
    t.goto(x,y)
    t.pd()
    return

def ellipse(rad,a):
    t.seth(-45)
    for i in range(2):
        t.circle(rad,90)
        t.circle(rad//a,90)

#얼굴 윤곽 그리기
move(0,-180)
t.pensize(10)
t.color('white')
t.fillcolor('brown')
t.begin_fill()
t.circle(180)
t.end_fill()

#오른쪽눈그리기
move(50,30)
t.color('black')
t.fillcolor('blue')
t.begin_fill()
ellipse(40,2)
t.end_fill()
#왼쪽눈그리기
move(-100,30)
t.pensize(1)
t.fillcolor('skyblue')
t.begin_fill()
ellipse(50,6)
t.end_fill()
#코그리기
move(0,-20)
t.color('orange')
t.fillcolor('orange')
t.begin_fill()
t.circle(20)
t.end_fill()
#입그리기
move(-60,-100)
t.color('red')
t.fillcolor('red')
t.begin_fill()
ellipse(90,5)
t.end_fill()

move(-60,-90)
t.color('brown')
t.fillcolor('brown')
t.begin_fill()
ellipse(90,5)
t.end_fill()

t.done()