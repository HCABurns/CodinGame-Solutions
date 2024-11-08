a,b,x,y=gets.split.map{|x|x.to_i}
loop{puts ["","S","N"][b<=>y]+["","E","W"][a<=>x]
x+=1if a>x
y+=1if b>y}
