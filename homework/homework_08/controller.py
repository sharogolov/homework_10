
import operations as o
import view as v


def button_click():
    while True:
        action = v.get_work()
        if action == 1:
            o.write_cvs()
        elif action == 2:
            o.search()
        elif action == 3:
            o.get_rewrite()
        elif action == 4:
            o.get_remove()
        elif action == 5:
            o.read_csv()
        elif action == 6:
            print('Работа с базой завершена.')
            break
        
    
