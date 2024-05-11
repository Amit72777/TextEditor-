import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser, messagebox, filedialog
import os
import googletrans
from googletrans import Translator

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title(" Python text editor ")


# ++++++++++++++++++++++++++++++++++++++translator functionality +++++++++++++++++++++++++


def translate_text(event=None):
    try:
        src = source_var.get()
        dest = dect_var.get()
        text = text_editor.get(1.0, tk.END)

        translator = Translator()
        translated = translator.translate(text, src=src, dest=dest)

        text_editor.delete(1.0, tk.END)
        text_editor.insert(tk.END, translated.text)

        tarns_frame.destroy()

    except Exception as e:
        messagebox.showwarning("Warning", "Translation Error: "+str(e))


def translate_data(event=None):
    global source_var, dect_var, tarns_frame
    tarns_frame = tk.Toplevel()
    source_var = tk.StringVar()
    dect_var = tk.StringVar()
    tarns_frame.geometry('450x250+500+200')
    tarns_frame.title('Google Translation')
    tarns_frame.resizable(0, 0)

    trans_label = ttk.LabelFrame(tarns_frame, text='Google  translator ')
    trans_label.pack()

    Laang = list(googletrans.LANGUAGES.values())
    # label
    source_text_label = tk.Label(trans_label, text='Enter the Source language', font=('bold', 10))
    target_text_label = tk.Label(trans_label, text='Enter the Target  language', font=('bold', 10))

    #  combobox
    source_text = ttk.Combobox(trans_label, textvariable=source_var, width=20)
    source_text['values'] = Laang
    source_text.current(Laang.index('english'))

    dict_text = ttk.Combobox(trans_label, textvariable=dect_var, width=20)
    dict_text['values'] = Laang
    dict_text.current(Laang.index('hindi'))

    # pack labels
    source_text_label.pack(pady=10)
    source_text.pack(pady=5)
    target_text_label.pack(pady=10, )
    dict_text.pack(padx=5, pady=5)

    submit_btn = ttk.Button(tarns_frame, text='Submit', command=translate_text)
    submit_btn.pack(padx=10, pady=10)


# ++++++++++++++++++++++++++++++++++++++   Main Menu  +++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++   End Menu   +++++++++++++++++++++++++++++++++++++++++++++++++++++

main_menu = tk.Menu()
# file icons

new_icon = tk.PhotoImage(file=r'icons2/new.png')
open_icon = tk.PhotoImage(file=r'icons2/open.png')
save_icon = tk.PhotoImage(file=r'icons2/save.png')
save_as_icon = tk.PhotoImage(file=r'icons2/save_as.png')
exit_icon = tk.PhotoImage(file=r'icons2/exit.png')

file = tk.Menu(main_menu, tearoff=False)

# ****edit
# edit icons
copy_icon = tk.PhotoImage(file=r'icons2/copy.png')
paste_icon = tk.PhotoImage(file=r'icons2/paste.png')
cut_icon = tk.PhotoImage(file=r'icons2/cut.png')
clear_icon = tk.PhotoImage(file=r'icons2/clear_all.png')
find_icon = tk.PhotoImage(file=r'icons2/find.png')

edit = tk.Menu(main_menu, tearoff=False)

# ******view icons
tool_bar_icons = tk.PhotoImage(file=r'icons2/tool_bar.png')
status_bar_icons = tk.PhotoImage(file=r'icons2/status_bar.png')

view = tk.Menu(main_menu, tearoff=False)

# ********Color theme

light_default_icon = tk.PhotoImage(file=r'icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file=r'icons2/light_plus.png')
dark_icon = tk.PhotoImage(file=r'icons2/dark.png')
red_icon = tk.PhotoImage(file=r'icons2/red.png')
monokai_icon = tk.PhotoImage(file=r'icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file=r'icons2/night_blue.png')
color_theme = tk.Menu(main_menu, tearoff=False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)
color_dict = {
    'Light Default': ('#000000', '#ffffff'),
    'Light Plus': ('#474747', '#e0e0e0'),
    'Dark': ('#c4c4c4', '#2d2d2d'),
    'Red': ('#2d2d2d', '#ffe8e8'),
    'MonoKai': ('#d3b774', '#474747'),
    'Night Blue': ('#ededed', '#6b9dc2')
}

# translate the code
transa = tk.Menu(main_menu, tearoff=False)

google_translation_icon = tk.PhotoImage(file=r"icons2\Google.png")

# cascade
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit ', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color theme ', menu=color_theme)
main_menu.add_cascade(label='Translate', menu=transa)

# ++++++++++++++++++++++++++++++++++++++ tool Bar +++++++++++++++++++++++++++++++++++++++++++++++++++++

tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

font_tuple = tk.font.families()
font_family = tk.StringVar()

font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))

font_box.grid(row=0, column=0, padx=5)

#   *** size box
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable=size_var, state='readonly')
font_size['values'] = tuple(range(8, 81))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)

#   ****bold button
bold_icon = tk.PhotoImage(file=r'icons2/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

# **itallic btton
italic_icon = tk.PhotoImage(file=r'icons2/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

underlin_icon = tk.PhotoImage(file=r'icons2/underline.png')
underlin_btn = ttk.Button(tool_bar, image=underlin_icon)
underlin_btn.grid(row=0, column=4, padx=5)

# font color button
font_icon = tk.PhotoImage(file=r'icons2/font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_icon)
font_color_btn.grid(row=0, column=5, padx=5)

#  align left
align_left_icon = tk.PhotoImage(file=r'icons2/align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

align_right_icon = tk.PhotoImage(file=r'icons2/align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)

align_center_icon = tk.PhotoImage(file=r'icons2/align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)
# ++++++++++++++++++++++++++++++++++++++ &&&&&& End tool Bar &&&&&& ++++++++++++++++++++++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++++++++ text editor  +++++++++++++++++++++++++++++++++++++++++++++++++++++
text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.focus_set()
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)

text_editor.config(yscrollcommand=scroll_bar.set)

# font family
current_font_family = 'Arial'
current_font_size = 12


def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))


def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))


font_box.bind('<<ComboboxSelected>>', change_font)
font_size.bind('<<ComboboxSelected>>', change_fontsize)


# ********************8    Button Functionality
# ***** Bold Button functionality

def change_bold():
    text_property = tk.font.Font(font=text_editor['font']).actual()
    if text_property['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))


bold_btn.configure(command=change_bold)


# ittalic function
def change_italic():
    text_property = tk.font.Font(font=text_editor['font']).actual()
    if text_property['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))


italic_btn.configure(command=change_italic)


#  underline functionality
def change_underline():
    text_property = tk.font.Font(font=text_editor['font']).actual()
    if text_property['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))


underlin_btn.configure(command=change_underline)


#    font color functionality
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


font_color_btn.configure(command=change_font_color)


# aligh functionality
def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_configure('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')


align_left_btn.configure(command=align_left)


def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_configure('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')


align_center_btn.configure(command=align_center)


def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_configure('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')


align_right_btn.configure(command=align_right)

text_editor.configure(font=('Arial', 12))

# ++++++++++++++++++++++++++++++++++++++ &&&&&end text editior &&&&&&  ++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ Status Bar +++++++++++++++++++++++++++++++++++++++++++++++++++++
status_bar = ttk.Label(main_application, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)
text_changed = False


def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        charactors = len(text_editor.get(1.0, 'end-1c'))

        status_bar.configure(text=f'( Characters : {charactors} worlds : {words}')
    text_editor.edit_modified(False)


text_editor.bind("<<Modified>>", changed)

# ++++++++++++++++++++++++++++++++++++++ &&&&&End Status Bar&&&&&&  +++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++ main Menu Functionality  +++++++++++++++++++++++++++++++++++++++++++++++++++++

#  variable


url = ''


# ***new funcionality
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)


# ***file command
file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl + N', command=new_file)


# ***opne functionallity
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select file',
                                     filetypes=(('text file', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except Exception as e:
        messagebox.showwarning("Error", "An error occurred while exiting: " + str(e))
        return

    main_application.title(os.path.basename(url))


file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Ctrl + O', command=open_file)


# ***save file

def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                           filetypes=(('text file', '*.txt'), ('All files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except Exception as e:
        messagebox.showwarning("Error", "An error occurred while exiting: " + str(e))
        return


file.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl + S', command=save_file)


#  ***save as functionality***
def save_as(even=None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                       filetypes=(('text file', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except Exception as e:
        messagebox.showwarning("Error", "An error occurred while exiting: " + str(e))
        return


file.add_command(label='Save as', image=save_as_icon, compound=tk.LEFT, accelerator='Ctrl + Alt +s', command=save_as)


#  ***exit functionality
def exit_fuc(even=None):
    global url
    try:
        if text_changed:
            inbox = messagebox.askyesnocancel('Warning ', ' Do you want to save the file ?')
            if inbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                                   filetypes=(('text file', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif inbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except Exception as e:
        messagebox.showwarning("Error", "An error occurred while exiting: " + str(e))


file.add_command(label='EXit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl + Q', command=exit_fuc)

# ***edit command
edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl +C',
                 command=lambda: text_editor.event_generate('<<Copy>>'))
edit.add_command(label='paste', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl +V',
                 command=lambda: text_editor.event_generate('<<Paste>>'))
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl +X',
                 command=lambda: text_editor.event_generate('<<Cut>>'))
edit.add_command(label='Clear All', image=clear_icon, compound=tk.LEFT, accelerator='Ctrl + Alt +X',
                 command=lambda: text_editor.delete(1.0, tk.END))


# find functionality

def find_func(event=None):
    def Find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'

            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos} + {len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                if matches != 1:
                    start_pos = end_pos
                    text_editor.tag_configure('match', foreground='red', background='yellow')

    def Replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0, 0)

    # frame
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    # labels
    text_find_label = ttk.Label(find_frame, text='Find :')
    text_replace_label = ttk.Label(find_frame, text='replace ')

    # enry
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    # button
    find_button = ttk.Button(find_frame, text='Find', command=Find)
    replace_button = ttk.Button(find_frame, text='Replace', command=Replace)

    # label grid
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    #  entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    # button grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()


edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl +F', command=find_func)

# *****View command******

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)


def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True


view.add_checkbutton(label='Tool Bar', onvalue=True, offvalue=0, variable=show_toolbar, image=tool_bar_icons,
                     compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label='Status Bar', onvalue=1, offvalue=False, variable=show_statusbar, image=status_bar_icons,
                     compound=tk.LEFT, command=hide_statusbar)

transa.add_command(label='Translate English to hindi ', image=google_translation_icon, compound=tk.LEFT,
                   accelerator='Control - Enter ', command=translate_data)

main_application.bind('<Control-Return>', translate_data)


# color theam

def change_theam():
    choice_theam = theme_choice.get()
    color_tuple = color_dict.get(choice_theam)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.configure(background=bg_color, fg=fg_color)


count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT,
                                command=change_theam)
    count += 1

# ++++++++++++++++++++++++++++++ &&&&&&&End main manu Functionality&&&&&&&&   ++++++++++++++++++++++++++++++++++++++++++

# Configuring bindings
main_application.bind('<Control-n>', new_file)
main_application.bind('<Control-o>', open_file)
main_application.bind('<Control-s>', save_file)
main_application.bind('<Control-Alt-s>', save_as)
main_application.bind('<Control-q>', exit_fuc)
main_application.bind('<Control-f>', find_func)

main_application.config(menu=main_menu)
main_application.mainloop()
