def decide_action(predicted_rul, drift_detected, mae, 
                  rul_threshold=40, mae_threshold=35):
    """
    Rule-based decision engine.
    """

    if predicted_rul < rul_threshold and mae < mae_threshold:
        return "SCHEDULE_MAINTENANCE"

    if drift_detected and mae >= mae_threshold:
        return "TRIGGER_RETRAINING"

    if drift_detected:
        return "MONITOR_CLOSELY"

    return "NORMAL_OPERATION"
