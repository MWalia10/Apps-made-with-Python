import cv2, pandas
from datetime import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

first_frame = None
status_list = [None, None]
times = []
df = pandas.DataFrame(columns = ["Start", "End"])

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    if first_frame is None:
        first_frame = gray
        continue
    
    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)
    
    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for countour in cnts:
        if cv2.contourArea(countour) < 10000:
            continue
        status = 1
        (x, y, z, h) = cv2.boundingRect(countour)
        cv2.rectangle(frame, (x, y), (x+z, y+h), (0, 255, 0), 3)
    status_list.append(status)
    
    status_list = status_list[-2:]
    
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())
        
    cv2.imshow("Grey frame", gray)
    cv2.imshow("Delta frame", delta_frame)
    cv2.imshow("Threshold frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)
    
    if key == ord("q"):
        if status == 1:
            times.append(datetime.now())
        break
    
print(status_list)
print(times)

for i in range(0, len(times), 2):
    df = df.append({"Start":times[i], "End": times[i+1]}, ignore_index = True)

df["Start"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

p = figure(x_axis_type = "datetime", height = 100, width = 500, title = "Motion Graph")
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips = [("Start","@Start"),("End","@End")])
p.add_tools(hover)

q = p.quad(left = "Start", right = "End", bottom = 0, top = 1, color = "green", source = cds)


output_file("Motion Graph.html")
show(p)
video.release()
cv2.destroyAllWindows()

df.to_csv("Times.csv")