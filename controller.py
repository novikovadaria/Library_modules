import view
import db_work
import log


def button_click():
    title, number_of_pages, first_name, last_name = view.get_value()
    log.logwrite("User wants to insert new data")
    db_work.add_book(title, number_of_pages, first_name, last_name)
    log.logwrite("Database is updated succesfully")
    view.output()
