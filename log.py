from datetime import datetime as dt

log_file = open('log_file.txt', 'a')
operation_time = dt.now().strftime('%H:%M')


def logwrite(message_text):
    log_file.write(operation_time + ' ' + message_text + '\n')
