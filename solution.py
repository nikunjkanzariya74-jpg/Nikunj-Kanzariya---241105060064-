print("Doctor Feedback")
doctors = ["Dr A","Dr B","Dr C"]
feedbacks = []

for i in range(3):
    fb = input("Enter feedback: ")
    feedbacks.append(fb)

print("Feedbacks:", feedbacks)

if len(feedbacks) > 0:
    print("Recorded")
else:
    print("No feedback")

for i in range(2):
    print("Done")

print("End")