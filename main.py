import time, model, view, controller

while True:
    time.sleep(1 / 60)
    controller.event_type()
    model.drive()
    view.draw()
