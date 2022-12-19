import functions
import PySimpleGUI as sg

sg.theme('DarkAmber')

label = sg.Text("Type in a To-Do here")

input_box = sg.InputText(tooltip="Enter a To-Do", key='todo')

add_button = sg.Button("add")

list_box = sg.Listbox(values=functions.get_todos(), key='todos.txt',
                      enable_events=True, size=(46, 10))
edit_button = sg.Button('edit')
complete_button = sg.Button("complete")
end_button = sg.Button("end")

window = sg.Window('My To-Do app',
                   layout=[[label], [input_box, add_button], [list_box, edit_button],
                           [complete_button, end_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos.txt'])

    match event:
        case 'add':
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos.txt'].update(values=todos)
        case 'edit':
            todo_to_edit = values['todos.txt'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos.txt'].update(values=todos)
        case 'complete':
            todo_to_complete = values['todos.txt'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos.txt'].update(values=todos)
        case 'end':
            break
        case('todos.txt'):
            window['todo'].update(value=values['todos.txt'][0])
        case sg.WINDOW_CLOSED:
            break
window.close()
