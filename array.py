tasks = ["Brush teeth", "Eat food", "Wash cloths","Sleep"]
print(tasks[0])
del tasks[0]#<<<<<<<
print(tasks[0])
tasks.remove("Eat food")#<<<<<
print(tasks[0])

tasks.append("Three")
print(tasks[2])
tasks.insert(2, "Two")
print(tasks[2])
print(tasks[3])

latest_task_accomplishted = tasks.pop(1)
print("latest_task_accomplishted is " + latest_task_accomplishted)
Task_accomplishted = [0]
Task_accomplishted.append(latest_task_accomplishted)
print("Task_accomplishted is " + Task_accomplishted[0])
