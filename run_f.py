from src import one_plot as op
from src import all_plot as ap
from src import best_plot as bp


#이미지를 저장하고 싶으면 첫번째 문자에 T 입력
#이미지를 보고싶으면 두번째 문자에 T 입력
op.oneplot('T','T') #하나씩 plot 해주는 코드


# 하나의 소자를 여러개 측정한 것을 한번에 plot 해주는 코드
for x in (200,300):
    for y in (300,500):
        for z in (30,60):
            for i in range(1,6):
                ap.allplot('T','T','%d %d %d %d'%(x,y,z,i))


# 여러개의 소자 중 best인것을 한번에 plot 해주는 코드
bp.bestplot('T','T','200 300 30 1 4','200 300 60 1 2','200 500 30 1 3','200 500 60 1 5','300 300 30 1 3','300 300 60 1 5','300 500 30 1 1','300 500 60 1 4')