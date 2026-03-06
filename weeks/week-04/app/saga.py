NEW = "NEW"
PAID = "PAID"
DONE = "DONE"
CANCELLED = "CANCELLED"


def next_state(state, event):
    transitions = {
        ("NEW", "PAY_OK"): "PAID",
        ("NEW", "PAY_FAIL"): "CANCELLED",
        ("PAID", "FINISH"): "DONE",
    }

    return transitions.get((state, event), state)


def compensate_reservation():
    import time

    retries = 0

    while retries < 5:
        try:
            print("Cancelling reservation...")
            return True
        except Exception:
            retries += 1
            time.sleep(1)

    raise Exception("Failed to cancel reservation")