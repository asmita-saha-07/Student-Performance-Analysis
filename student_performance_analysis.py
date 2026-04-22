import matplotlib.pyplot as plt

#sample data
hours_studied_per_day = [1, 2, 3, 4, 5, 6, 7]
marks_scored=[60, 70, 78, 82, 85, 92, 98]
free_hours_per_day=[7, 6, 5, 4, 3, 2, 1]
sleep_hours_per_day=[8, 7.5, 7, 6.5, 6, 5.5, 5]
screentime=[6, 5.5, 5, 4.5, 4, 3, 2]

#creating subplots
sub1=plt.subplot(2,2,1)
sub2=plt.subplot(2,2,2)
sub3=plt.subplot(2,2,3)
sub4=plt.subplot(2,2,4)

#comparison between marks scored and hours studied
sub1.plot(hours_studied_per_day, marks_scored, color='red', marker='o', linestyle="-")
sub1.set_title("Marks Scored \n VS \n Hours Studied Per Day")
sub1.set_xlabel("Hours Studied Per Day")
sub1.set_ylabel("Marks Scored")

#comparison between free time and hours studied
sub2.plot(hours_studied_per_day, free_hours_per_day, color='blue', marker='s', linestyle='--')
sub2.set_title("Free Time Per Day (in hours) \n VS \n Hours Studied Per Day")
sub2.set_xlabel("Hours Studied Per Day")
sub2.set_ylabel("Free Time Per Day (in hours)")

#comparison between sleep hours and hours studied
sub3.plot(hours_studied_per_day, sleep_hours_per_day, color='green', linestyle=':', marker='d')
sub3.set_title("Sleep Per Day (in hours) \n VS \n Hours Studied Per Day")
sub3.set_xlabel("Hours Studied Per Day")
sub3.set_ylabel("Hours of Sleep Per Day")

#comparison between screentime and hours studied
sub4.plot(hours_studied_per_day, screentime, color='orange', linestyle='-.', marker='^')
sub4.set_title(" Average Screentime (in hours) \n VS \n Hours Studied Per Day")
sub4.set_xlabel("Hours Studied Per Day")
sub4.set_ylabel("Average Screentime Per Day (in hours)")


plt.suptitle("Student Performance Analysis", fontsize=14)
plt.tight_layout()
plt.show()