# Author: Sunil Gupta, Sainithya Surasani, Nihal Reddy Akula.
# Date: 5/5/2024
# Description: Python Project 2 code.


from Recommender import Recommender
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
        self.loadShows_flag = 0
        self.rating()

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
        self.search_show_button = tk.Button(row_six, text="Search", command=self.searchShows)
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
        self.search_show_button_b = tk.Button(row_four, text="Search", command=self.searchBooks)
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
        self.search_show_button_r = tk.Button(row_four, text="Get Recommendation", command=self.getRecommendations)
        self.search_show_button_r.pack(side='left', padx=2, pady=2, fill='x')
        row_four.pack(anchor='w')

        self.search_results_text_r = tk.Text(recomm)
        self.search_results_text_r.pack(side='left', fill='both', padx=5, pady=5, expand=True)
        self.search_results_text_r.insert(tk.END, '"Enter recommendation condition and click on Get Recommendation button"')
        self.search_results_text_r.config(state=tk.DISABLED)
        scrollbar = tk.Scrollbar(recomm, command=self.search_results_text.yview)
        scrollbar.pack(side='right', fill='y')
        self.search_results_text_r.config(yscrollcommand=scrollbar.set)


    def rating(self):
        ratings = ttk.Frame(self.nb)
        self.nb.add(ratings, text="Ratings")
        pie_chart = tk.Frame(ratings)
        pie_chart.pack()
        self.generate_pie_chart = tk.Button(pie_chart, text="Generate Pie Chart", command=self.getPieChart)
        self.generate_pie_chart.pack(padx=5, pady=5)
        pie_frame = tk.Frame(ratings)
        pie_frame.pack()
        self.pie1 = tk.Canvas(pie_frame, height=250, width=250)
        self.pie1.pack(side='left', padx=5, pady=30)
        self.pie2 = tk.Canvas(pie_frame, height=200, width=200)
        self.pie2.pack(side='right', padx=5, pady=30)


    def getPieChart(self):
        if self.loadShows_flag == 0:
            messagebox.showwarning("Error", f"Please load Show file before generating.")
            return
        movie = self.rec_obj.getMovieStats()
        shows = self.rec_obj.getTVStats()
        movie_label = []
        movie_per = []
        show_label = []
        show_per = []
        for i in range(1, len(movie)):
            if movie[i] == "":
                break
            st = movie[i].split(" ")
            movie_label.append(st[0])
            movie_per.append(float(st[2][0:len(st[2])-1]))
        for i in range(1, len(shows)):
            if shows[i] == "":
                break
            st = shows[i].split(" ")
            show_label.append(st[0])
            show_per.append(float(st[2][0:len(st[2])-1]))

        pairs = list(zip(movie_label, movie_per))
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        movie_label, movie_per = zip(*sorted_pairs)

        pairs = list(zip(show_label, show_per))
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        show_label, show_per = zip(*sorted_pairs)

        movie_label = list(movie_label)
        movie_per = list(movie_per)
        show_label = list(show_label)
        show_per = list(show_per)

        label = []
        perc = []
        while movie_per:
            perc.append(movie_per.pop())
            label.append(movie_label.pop())
            if movie_per:
                perc.append(movie_per.pop(0))
                label.append(movie_label.pop(0))
        movie_per = perc
        movie_label = label

        label = []
        perc = []
        while show_per:
            perc.append(show_per.pop())
            label.append(show_label.pop())
            if show_per:
                perc.append(show_per.pop(0))
                label.append(show_label.pop(0))
        show_per = perc
        show_label = label

        self.pie1.delete("all")
        self.pie2.delete("all")
        pie1, ax1 = plt.subplots(figsize=(7, 7))
        ax1.pie(movie_per, labels=movie_label, autopct='%1.2f%%', startangle=90)
        ax1.set_title("Movies Ratings pie chart:")
        pie_chart1 = FigureCanvasTkAgg(pie1, master=self.pie1)
        pie_chart1.get_tk_widget().pack()
        pie2, ax2 = plt.subplots(figsize=(7, 7))
        ax2.pie(show_per, labels=show_label, autopct='%1.2f%%', startangle=90)
        ax2.set_title("Shows Ratings pie chart:")
        pie_chart2 = FigureCanvasTkAgg(pie2, master=self.pie2)
        pie_chart2.get_tk_widget().pack()


    def buttons(self):
        self.button = tk.Frame(self.main_window)
        self.shows = tk.Button(self.button, text='Load Shows', command=self.loadshows)
        self.books = tk.Button(self.button, text='Load Books', command=self.loadBooks)
        self.recommen = tk.Button(self.button, text='Load Recommendations', command=self.loadAssociations)
        self.info = tk.Button(self.button, text='Information', command=self.creditInfoBox)
        self.quit = tk.Button(self.button, text='Quit', command=self.main_window.quit)
        self.button.pack(padx=2, side="bottom", pady=5)
        self.shows.pack(side="left", padx=80)
        self.books.pack(side="left", padx=80)
        self.recommen.pack(side="left", padx=80)
        self.info.pack(side="left", padx=80)
        self.quit.pack(side="left", padx=80)


    def loadshows(self):
        self.loadShows_flag = 1
        self.first_entry.configure(state=tk.NORMAL)
        self.second_entry.configure(state=tk.NORMAL)
        self.firsts_entry.configure(state=tk.NORMAL)
        self.seconds_entry.configure(state=tk.NORMAL)

        self.rec_obj.loadShows()

        movie_names = self.rec_obj.getMovieList()
        movie_statistics = self.rec_obj.getMovieStats()
        tvshow_name = self.rec_obj.getTVList()
        tvshow_statistics = self.rec_obj.getTVStats()

        self.first_entry.delete("1.0", "end")
        for i in movie_names:
            self.first_entry.insert(tk.END, i + '\n')

        self.second_entry.delete("1.0", "end")
        for i in movie_statistics:
            self.second_entry.insert(tk.END, i + '\n')

        self.firsts_entry.delete("1.0", "end")
        for i in tvshow_name:
            self.firsts_entry.insert(tk.END, i + '\n')

        self.seconds_entry.delete("1.0", "end")
        for i in tvshow_statistics:
            self.seconds_entry.insert(tk.END, i + '\n')

        self.first_entry.configure(state=tk.DISABLED)
        self.second_entry.configure(state=tk.DISABLED)
        self.firsts_entry.configure(state=tk.DISABLED)
        self.seconds_entry.configure(state=tk.DISABLED)


    def loadBooks(self):
        self.loadBooks_flag = 1
        self.firstb_entry.configure(state=tk.NORMAL)
        self.secondb_entry.configure(state=tk.NORMAL)

        self.rec_obj.loadBooks()

        books_names = self.rec_obj.getBookList()
        books_statistics = self.rec_obj.getBookStats()

        self.firstb_entry.delete("1.0", "end")
        for i in books_names:
            self.firstb_entry.insert(tk.END, i + '\n')

        self.secondb_entry.delete("1.0", "end")
        for i in books_statistics:
            self.secondb_entry.insert(tk.END, i + '\n')

        self.firstb_entry.configure(state=tk.DISABLED)
        self.secondb_entry.configure(state=tk.DISABLED)


    def loadAssociations(self):
        self.rec_obj.loadAssociations()

    def creditInfoBox(self):
        messagebox.showinfo("Project details","Group Members:\n1. Sunil Virendra Gupta\n2.Sainithya Surasani\n3.Nihal Reddy Akula\n\nProjected completed on: 5/5/2024")


    def searchShows(self):
        type_show = self.type_combobox.get()
        if type_show == "":
            type_show = None
        title = self.title_entry.get()
        if title == "":
            title = None
        director = self.director_entry.get()
        if director == "":
            director = None
        actor = self.actor_entry.get()
        if actor == "":
            actor = None
        genre = self.genre_entry.get()
        if genre == "":
            genre = None
        stri = self.rec_obj.searchTVMovies(type_show, title, director, actor, genre)
        self.search_results_text.configure(state=tk.NORMAL)
        if len(stri) > 0:
            self.search_results_text.delete("1.0", "end")
            for i in stri:
                self.search_results_text.insert(tk.END, i + '\n')
        self.search_results_text.configure(state=tk.DISABLED)


    def searchBooks(self):
        title = self.title_entry_b.get()
        if title == "":
            title = None
        author = self.author_entry_b.get()
        if author == "":
            author = None
        publisher = self.publisher_entry_b.get()
        if publisher == "":
            publisher = None
        stri = self.rec_obj.searchBooks(title, author, publisher)
        self.search_results_text_b.configure(state=tk.NORMAL)
        if len(stri) > 0:
            self.search_results_text_b.delete("1.0", "end")
            for i in stri:
                self.search_results_text_b.insert(tk.END, i + '\n')
        self.search_results_text_b.configure(state=tk.DISABLED)


    def getRecommendations(self):
        type_show = self.type_combobox_r.get()
        if type_show == "":
            type_show = None
        title = self.title_entry_r.get()
        if title == "":
            title = None
        stri = self.rec_obj.getRecommendations(type_show, title)
        self.search_results_text_r.configure(state=tk.NORMAL)
        self.search_results_text_r.delete("1.0", "end")
        self.search_results_text_r.insert(tk.END, stri)
        self.search_results_text_r.configure(state=tk.DISABLED)


    def run(self):
        self.main_window.mainloop()


def main():
    gui = RecommenderGUI()
    gui.run()


main()
