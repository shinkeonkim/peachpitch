import billboard

# chart들
l = billboard.charts()

#hot-100 chart 가져오기
s = billboard.ChartData('hot-100')

chart_list = []
for i in range(100):
    chart_list.append((s[i].title,s[i].artist))
print(chart_list)