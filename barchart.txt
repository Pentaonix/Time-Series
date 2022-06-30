#barchart
#set limit to vertical axis
figure, axis = plt.subplots()
axis.set_ylim(0,100)

#list from 0-11 -> get name
y_pos = np.arange(len(subjects))

#plot the barchart using 2 list(name,value)
plt.bar(y_pos, dont_take_exam_percentage, align='center', alpha=0.5)

#change horizontal category name
plt.xticks(y_pos, subjects)

#labeling for vertical axis
plt.ylabel('Percentage(%)')

#barchart's name
plt.title('Exams_not_taken')

#set labels for columns
rects = axis.patches
for rect, label in zip(rects, dont_take_exam):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 1, label,
            ha='center', va='bottom')

plt.show()