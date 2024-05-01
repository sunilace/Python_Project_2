from Recommender import Recommender
import tkinter as tk
from tkinter import ttk
import time


class RecommenderGUI:
    def __init__(self):
        self.rec_obj = Recommender()
        self.main_window = tk.Tk()
        self.main_window.title("Media Recommender")
        self.main_window.geometry("1200x800")
        self.nb = ttk.Notebook(self.main_window)
        self.nb.pack(fill=tk.BOTH, expand=True)
        self.movie()
        self.showss()
        self.bookss()
        self.searchshows()
        self.searchbooks()
        self.recommendation()
        self.buttons()

    def movie(self):
        movie_tab = ttk.Frame(self.nb)
        self.nb.add(movie_tab, text='Movies')
        self.f_frame =tk.Frame(movie_tab)
        self.f_frame.pack(fill='both', expand=True)
        self.first_entry = tk.Text(self.f_frame, wrap='none')
        self.first_entry.pack(fill='both', side='left', expand=True, ipadx=10, ipady=10)
        self.scrollbar = tk.Scrollbar(self.f_frame, command=self.first_entry.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.first_entry.config(yscrollcommand=self.scrollbar.set)
        self.s_frame = tk.Frame(movie_tab)
        self.s_frame.pack(fill='both', expand=True)
        self.second_entry = tk.Text(self.s_frame)
        self.second_entry.pack(fill='both', expand=True, ipadx=10, ipady=10)
        self.first_entry.insert(1.0, '"No data has been loaded"')
        self.second_entry.insert(1.0, '"No data has been loaded"')
        self.first_entry.configure(state=tk.DISABLED)
        self.second_entry.configure(state=tk.DISABLED)


    def showss(self):
        tv_shows = ttk.Frame(self.nb)
        self.nb.add(tv_shows, text="TV Shows")
        self.fs_frame = tk.Frame(tv_shows)
        self.fs_frame.pack(fill='both', expand=True)
        self.firsts_entry = tk.Text(self.fs_frame, wrap='none')
        self.firsts_entry.pack(fill='both', side='left', expand=True, ipadx=10, ipady=10)
        self.scrollbar = tk.Scrollbar(self.fs_frame, command=self.firsts_entry.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.firsts_entry.config(yscrollcommand=self.scrollbar.set)
        self.ss_frame = tk.Frame(tv_shows)
        self.ss_frame.pack(fill='both', expand=True)
        self.seconds_entry = tk.Text(self.ss_frame)
        self.seconds_entry.pack(fill='both', expand=True, ipadx=10, ipady=10)
        self.firsts_entry.insert(1.0, '"No data has been loaded"')
        self.seconds_entry.insert(1.0, '"No data has been loaded"')
        self.firsts_entry.configure(state=tk.DISABLED)
        self.seconds_entry.configure(state=tk.DISABLED)


    def bookss(self):
        books = ttk.Frame(self.nb)
        self.nb.add(books, text="Books")
        self.fb_frame = tk.Frame(books)
        self.fb_frame.pack(fill='both', expand=True)
        self.firstb_entry = tk.Text(self.fb_frame, wrap='none')
        self.firstb_entry.pack(fill='both', side='left', expand=True, ipadx=10, ipady=10)
        self.scrollbar = tk.Scrollbar(self.fb_frame, command=self.firstb_entry.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.firstb_entry.config(yscrollcommand=self.scrollbar.set)
        self.sb_frame = tk.Frame(books)
        self.sb_frame.pack(fill='both', expand=True)
        self.secondb_entry = tk.Text(self.sb_frame)
        self.secondb_entry.pack(fill='both', expand=True, ipadx=10, ipady=10)
        self.firstb_entry.insert(1.0, '"No data has been loaded"')
        self.secondb_entry.insert(1.0, '"No data has been loaded"')
        self.firstb_entry.configure(state=tk.DISABLED)
        self.secondb_entry.configure(state=tk.DISABLED)


    def searchshows(self):
        movie_tv_shows = ttk.Frame(self.nb)
        self.nb.add(movie_tv_shows, text='Search Movies/TV')

        row_one = tk.Frame(movie_tv_shows)
        types = tk.Label(row_one, text='Type: ')
        types.pack(side='left', padx=2, pady=2)
        type_var = tk.StringVar()
        self.type_combobox = ttk.Combobox(row_one, textvariable=type_var, values=['Movie', 'TV Show'])
        self.type_combobox.pack(side='left', padx=2, pady=2)
        row_one.pack(anchor='w')

        row_two = tk.Frame(movie_tv_shows)
        title = tk.Label(row_two, text='Title: ')
        title.pack(side='left', padx=2, pady=2)
        self.title_entry = tk.Entry(row_two, width=40)
        self.title_entry.pack(side='left', padx=2, pady=2, fill='x')
        row_two.pack(anchor='w')

        row_three = tk.Frame(movie_tv_shows)
        director = tk.Label(row_three, text='Director: ')
        director.pack(side='left', padx=2, pady=2)
        self.director_entry = tk.Entry(row_three, width=40)
        self.director_entry.pack(side='left', padx=2, pady=2, fill='x')
        row_three.pack(anchor='w')

        row_four = tk.Frame(movie_tv_shows)
        actor = tk.Label(row_four, text='Actor: ')
        actor.pack(side='left', padx=2, pady=2)
        self.actor_entry = tk.Entry(row_four, width=40)
        self.actor_entry.pack(side='left', padx=2, pady=2, fill='x')
        row_four.pack(anchor='w')

        row_five = tk.Frame(movie_tv_shows)
        genre = tk.Label(row_five, text='Genre: ')
        genre.pack(side='left', padx=2, pady=2)
        self.genre_entry = tk.Entry(row_five, width=40)
        self.genre_entry.pack(side='left', padx=2, pady=2, fill='x')
        row_five.pack(anchor='w')

        row_six = tk.Frame(movie_tv_shows)
        self.search_show_button = tk.Button(row_six, text="Search")
        self.search_show_button.pack(side='left', padx=2, pady=2, fill='x')
        row_six.pack(anchor='w')

        self.search_results_text = tk.Text(movie_tv_shows)
        self.search_results_text.pack(side='left', fill='both', padx=5, pady=5, expand=True)
        self.search_results_text.insert(tk.END, '"Enter search condition and click on Search button"')
        self.search_results_text.config(state=tk.DISABLED)
        scrollbar = tk.Scrollbar(movie_tv_shows, command=self.search_results_text.yview)
        scrollbar.pack(side='right', fill='y')
        self.search_results_text.config(yscrollcommand=scrollbar.set)



    def searchbooks(self):
        search_books = ttk.Frame(self.nb)
        self.nb.add(search_books, text='Search Books')

        row_one = tk.Frame(search_books)
        title = tk.Label(row_one, text='Title: ')
        title.pack(side='left', padx=2, pady=2)
        self.title_entry_b = tk.Entry(row_one, width=40)
        self.title_entry_b.pack(side='left', padx=2, pady=2, fill='x')
        row_one.pack(anchor='w')

        row_two = tk.Frame(search_books)
        author = tk.Label(row_two, text='Author: ')
        author.pack(side='left', padx=2, pady=2)
        self.author_entry_b = tk.Entry(row_two, width=40)
        self.author_entry_b.pack(side='left', padx=2, pady=2, fill='x')
        row_two.pack(anchor='w')

        row_three = tk.Frame(search_books)
        publisher = tk.Label(row_three, text='Publisher: ')
        publisher.pack(side='left', padx=2, pady=2)
        self.publisher_entry_b = tk.Entry(row_three, width=40)
        self.publisher_entry_b.pack(side='left', padx=2, pady=2, fill='x')
        row_three.pack(anchor='w')

        row_four = tk.Frame(search_books)
        self.search_show_button_b = tk.Button(row_four, text="Search")
        self.search_show_button_b.pack(side='left', padx=2, pady=2, fill='x')
        row_four.pack(anchor='w')

        self.search_results_text_b = tk.Text(search_books)
        self.search_results_text_b.pack(side='left', fill='both', padx=5, pady=5, expand=True)
        self.search_results_text_b.insert(tk.END, '"Enter search condition and click on Search button"')
        self.search_results_text_b.config(state=tk.DISABLED)
        scrollbar = tk.Scrollbar(search_books, command=self.search_results_text.yview)
        scrollbar.pack(side='right', fill='y')
        self.search_results_text_b.config(yscrollcommand=scrollbar.set)


    def recommendation(self):
        recomm = ttk.Frame(self.nb)
        self.nb.add(recomm, text="Recommendations")

        row_one = tk.Frame(recomm)
        types = tk.Label(row_one, text='Type: ')
        types.pack(side='left', padx=2, pady=2)
        type_var = tk.StringVar()
        self.type_combobox_r = ttk.Combobox(row_one, textvariable=type_var, values=['Movie', 'TV Show', 'Books'])
        self.type_combobox_r.pack(side='left', padx=2, pady=2)
        row_one.pack(anchor='w')

        row_two = tk.Frame(recomm)
        title = tk.Label(row_two, text='Title: ')
        title.pack(side='left', padx=2, pady=2)
        self.title_entry_r = tk.Entry(row_two, width=40)
        self.title_entry_r.pack(side='left', padx=2, pady=2, fill='x')
        row_two.pack(anchor='w')

        row_four = tk.Frame(recomm)
        self.search_show_button_r = tk.Button(row_four, text="Get Recommendation")
        self.search_show_button_r.pack(side='left', padx=2, pady=2, fill='x')
        row_four.pack(anchor='w')

        self.search_results_text_r = tk.Text(recomm)
        self.search_results_text_r.pack(side='left', fill='both', padx=5, pady=5, expand=True)
        self.search_results_text_r.insert(tk.END, '"Enter recommendation condition and click on Get Recommendation button"')
        self.search_results_text_r.config(state=tk.DISABLED)
        scrollbar = tk.Scrollbar(recomm, command=self.search_results_text.yview)
        scrollbar.pack(side='right', fill='y')
        self.search_results_text_r.config(yscrollcommand=scrollbar.set)


    def run(self):
        self.main_window.mainloop()


    def buttons(self):
        self.button = tk.Frame(self.main_window)
        self.shows = tk.Button(self.button, text='Load Shows', command=self.loadshows)
        self.books = tk.Button(self.button, text='Load Books')
        self.recommen = tk.Button(self.button, text='Load Recommendations')
        self.info = tk.Button(self.button, text='Information')
        self.quit = tk.Button(self.button, text='Quit')
        self.button.pack(padx=2, side="bottom", pady=5)
        self.shows.pack(side="left", padx=80)
        self.books.pack(side="left", padx=80)
        self.recommen.pack(side="left", padx=80)
        self.info.pack(side="left", padx=80)
        self.quit.pack(side="left", padx=80)


    def loadshows(self):
        self.first_entry.configure(state=tk.NORMAL)
        self.second_entry.configure(state=tk.NORMAL)
        k = '''
1
                2
                3
                4
                5
                6
                7
                8
                9
                10
                11
                12
                13
                14
                15
                16
                17
                18
                19
                20
                21
                22
                23
                24
                25
                '''
        self.first_entry.delete("1.0", "end")
        self.first_entry.insert("1.0", k)
        self.second_entry.delete("1.0", "end")
        self.first_entry.configure(state=tk.DISABLED)
        self.second_entry.configure(state=tk.DISABLED)


gui = RecommenderGUI()
gui.run()
