import time, model, view, controller

while True:
    time.sleep(1 / 60)
    print(model.live)
    controller.event_type()
    model.drive()
    view.draw()
