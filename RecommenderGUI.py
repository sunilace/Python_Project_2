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
    # Constructer function.
    def __init__(self):
        self.__rec_obj = Recommender()
        self.__main_window = tk.Tk()
        self.__main_window.title("Media Recommender")
        self.__main_window.geometry("1200x800")
        # Creating notebook.
        self.__nb = ttk.Notebook(self.__main_window)
        self.__nb.pack(fill=tk.BOTH, expand=True)
        # To keep track whether the shows are loaded or not for Rating notebook tab.
        self.__loadshows_flag = 0
        self.__loadassociations = 0
        self.movie()
        self.showss()
        self.bookss()
        self.searchshows()
        self.searchbooks()
        self.recommendation()
        self.buttons()
        self.rating()

    # To create GUI for Movie Notebook tab.
    def movie(self):
        # Creating movie notebook tab.
        movie_tab = ttk.Frame(self.__nb)
        self.__nb.add(movie_tab, text='Movies')
        f_frame = tk.Frame(movie_tab)
        f_frame.pack(fill='both', expand=True)
        # Creating text box to display movie title and runtime details.
        self.first_entry = tk.Text(f_frame, wrap='none')
        self.first_entry.pack(fill='both', side='left', expand=True, ipadx=10, ipady=10)
        # Scrollbar for first text box in Movie Notebook.
        scrollbar = tk.Scrollbar(f_frame, command=self.first_entry.yview)
        scrollbar.pack(side="right", fill="y")
        self.first_entry.config(yscrollcommand=scrollbar.set)
        s_frame = tk.Frame(movie_tab)
        s_frame.pack(fill='both', expand=True)
        # Second text box to display ratings.
        self.second_entry = tk.Text(s_frame)
        self.second_entry.pack(fill='both', expand=True, ipadx=10, ipady=10)
        # To enter default data or sentence to show no data has been loaded.
        self.first_entry.insert(1.0, '"No data has been loaded"')
        self.second_entry.insert(1.0, '"No data has been loaded"')
        # Making the text widget non-editable.
        self.first_entry.configure(state=tk.DISABLED)
        self.second_entry.configure(state=tk.DISABLED)

    # Creating GUI for TV Show notebook tab.
    def showss(self):
        tv_shows = ttk.Frame(self.__nb)
        self.__nb.add(tv_shows, text="TV Shows")
        fs_frame = tk.Frame(tv_shows)
        fs_frame.pack(fill='both', expand=True)
        # Creating text widget to display TV show details.
        self.firsts_entry = tk.Text(fs_frame, wrap='none')
        self.firsts_entry.pack(fill='both', side='left', expand=True, ipadx=10, ipady=10)
        # Scrollbar for the text widget.
        scrollbar = tk.Scrollbar(fs_frame, command=self.firsts_entry.yview)
        scrollbar.pack(side="right", fill="y")
        self.firsts_entry.config(yscrollcommand=scrollbar.set)
        ss_frame = tk.Frame(tv_shows)
        ss_frame.pack(fill='both', expand=True)
        # Text widget to display Rating for TV Shows.
        self.seconds_entry = tk.Text(ss_frame)
        self.seconds_entry.pack(fill='both', expand=True, ipadx=10, ipady=10)
        # Default text to display representing no data has been loaded.
        self.firsts_entry.insert(1.0, '"No data has been loaded"')
        self.seconds_entry.insert(1.0, '"No data has been loaded"')
        # Making both the text widget non-editable.
        self.firsts_entry.configure(state=tk.DISABLED)
        self.seconds_entry.configure(state=tk.DISABLED)

    # Creating GUI for Books notebook tab.
    def bookss(self):
        books = ttk.Frame(self.__nb)
        self.__nb.add(books, text="Books")
        fb_frame = tk.Frame(books)
        fb_frame.pack(fill='both', expand=True)
        # Creating text widget to display books details.
        self.firstb_entry = tk.Text(fb_frame, wrap='none')
        self.firstb_entry.pack(fill='both', side='left', expand=True, ipadx=10, ipady=10)
        # Scroll bar for first test widget.
        scrollbar = tk.Scrollbar(fb_frame, command=self.firstb_entry.yview)
        scrollbar.pack(side="right", fill="y")
        self.firstb_entry.config(yscrollcommand=scrollbar.set)
        sb_frame = tk.Frame(books)
        sb_frame.pack(fill='both', expand=True)
        # Second text widget to display average page count, most common author and publisher.
        self.secondb_entry = tk.Text(sb_frame)
        self.secondb_entry.pack(fill='both', expand=True, ipadx=10, ipady=10)
        # Default text to display representing no data has been loaded.
        self.firstb_entry.insert(1.0, '"No data has been loaded"')
        self.secondb_entry.insert(1.0, '"No data has been loaded"')
        # Making both the text widget non-editable.
        self.firstb_entry.configure(state=tk.DISABLED)
        self.secondb_entry.configure(state=tk.DISABLED)

    # Creating GUI to search shows.
    def searchshows(self):
        movie_tv_shows = ttk.Frame(self.__nb)
        self.__nb.add(movie_tv_shows, text='Search Movies/TV')

        # Creating label and combobox widget for Show Type.
        row_one = tk.Frame(movie_tv_shows)
        types = tk.Label(row_one, text='Type: ')
        types.pack(side='left', padx=2, pady=2)
        type_var = tk.StringVar()
        self.type_combobox = ttk.Combobox(row_one, textvariable=type_var, values=['Movie', 'TV Show'])
        self.type_combobox.pack(side='left', padx=2, pady=2)
        row_one.pack(anchor='w')

        # Creating label and entry widget for Title.
        row_two = tk.Frame(movie_tv_shows)
        title = tk.Label(row_two, text='Title: ')
        title.pack(side='left', padx=2, pady=2)
        self.title_entry = tk.Entry(row_two, width=40)
        self.title_entry.pack(side='left', padx=2, pady=2, fill='x')
        row_two.pack(anchor='w')

        # Creating label and entry widget for Director.
        row_three = tk.Frame(movie_tv_shows)
        director = tk.Label(row_three, text='Director: ')
        director.pack(side='left', padx=2, pady=2)
        self.director_entry = tk.Entry(row_three, width=40)
        self.director_entry.pack(side='left', padx=2, pady=2, fill='x')
        row_three.pack(anchor='w')

        # Creating label and entry widget for Actor.
        row_four = tk.Frame(movie_tv_shows)
        actor = tk.Label(row_four, text='Actor: ')
        actor.pack(side='left', padx=2, pady=2)
        self.actor_entry = tk.Entry(row_four, width=40)
        self.actor_entry.pack(side='left', padx=2, pady=2, fill='x')
        row_four.pack(anchor='w')

        # Creating label and entry widget for Genre.
        row_five = tk.Frame(movie_tv_shows)
        genre = tk.Label(row_five, text='Genre: ')
        genre.pack(side='left', padx=2, pady=2)
        self.genre_entry = tk.Entry(row_five, width=40)
        self.genre_entry.pack(side='left', padx=2, pady=2, fill='x')
        row_five.pack(anchor='w')

        # Creating button for Search.
        row_six = tk.Frame(movie_tv_shows)
        self.search_show_button = tk.Button(row_six, text="Search", command=self.searchShows)
        self.search_show_button.pack(side='left', padx=2, pady=2, fill='x')
        row_six.pack(anchor='w')

        # Creating text widget to dispaly result after the search.
        self.search_results_text = tk.Text(movie_tv_shows)
        self.search_results_text.pack(side='left', fill='both', padx=5, pady=5, expand=True)
        # Entering default message.
        self.search_results_text.insert(tk.END, '"Enter search condition and click on Search button"')
        # Disabling the text widget.
        self.search_results_text.config(state=tk.DISABLED)
        # Adding scrollbar to the text widget to scroll through data.
        scrollbar = tk.Scrollbar(movie_tv_shows, command=self.search_results_text.yview)
        scrollbar.pack(side='right', fill='y')
        self.search_results_text.config(yscrollcommand=scrollbar.set)

    # Creating GUI to search Books.
    def searchbooks(self):
        search_books = ttk.Frame(self.__nb)
        self.__nb.add(search_books, text='Search Books')

        # Creating label and entry widget for Title.
        row_one = tk.Frame(search_books)
        title = tk.Label(row_one, text='Title: ')
        title.pack(side='left', padx=2, pady=2)
        self.title_entry_b = tk.Entry(row_one, width=40)
        self.title_entry_b.pack(side='left', padx=2, pady=2, fill='x')
        row_one.pack(anchor='w')

        # Creating label and entry widget for Author.
        row_two = tk.Frame(search_books)
        author = tk.Label(row_two, text='Author: ')
        author.pack(side='left', padx=2, pady=2)
        self.author_entry_b = tk.Entry(row_two, width=40)
        self.author_entry_b.pack(side='left', padx=2, pady=2, fill='x')
        row_two.pack(anchor='w')

        # Creating label and entry widget for Publisher.
        row_three = tk.Frame(search_books)
        publisher = tk.Label(row_three, text='Publisher: ')
        publisher.pack(side='left', padx=2, pady=2)
        self.publisher_entry_b = tk.Entry(row_three, width=40)
        self.publisher_entry_b.pack(side='left', padx=2, pady=2, fill='x')
        row_three.pack(anchor='w')

        # Creating button for search.
        row_four = tk.Frame(search_books)
        self.search_show_button_b = tk.Button(row_four, text="Search", command=self.searchBooks)
        self.search_show_button_b.pack(side='left', padx=2, pady=2, fill='x')
        row_four.pack(anchor='w')

        # Creating text widget to display the search result.
        self.search_results_text_b = tk.Text(search_books)
        self.search_results_text_b.pack(side='left', fill='both', padx=5, pady=5, expand=True)
        # Showing default text.
        self.search_results_text_b.insert(tk.END, '"Enter search condition and click on Search button"')
        self.search_results_text_b.config(state=tk.DISABLED)
        # Scrollbar to scroll through the data in the text widget.
        scrollbar = tk.Scrollbar(search_books, command=self.search_results_text.yview)
        scrollbar.pack(side='right', fill='y')
        self.search_results_text_b.config(yscrollcommand=scrollbar.set)

    # Creating GUI to show recommendation.
    def recommendation(self):
        recomm = ttk.Frame(self.__nb)
        self.__nb.add(recomm, text="Recommendations")

        # Creating label and combobox widget for Media type.
        row_one = tk.Frame(recomm)
        types = tk.Label(row_one, text='Type: ')
        types.pack(side='left', padx=2, pady=2)
        type_var = tk.StringVar()
        self.type_combobox_r = ttk.Combobox(row_one, textvariable=type_var, values=['Movie', 'TV Show', 'Books'])
        self.type_combobox_r.pack(side='left', padx=2, pady=2)
        row_one.pack(anchor='w')

        # Creating label and entry widget for Title.
        row_two = tk.Frame(recomm)
        title = tk.Label(row_two, text='Title: ')
        title.pack(side='left', padx=2, pady=2)
        self.title_entry_r = tk.Entry(row_two, width=40)
        self.title_entry_r.pack(side='left', padx=2, pady=2, fill='x')
        row_two.pack(anchor='w')

        # Creating button for search.
        row_four = tk.Frame(recomm)
        self.search_show_button_r = tk.Button(row_four, text="Get Recommendation", command=self.getRecommendations)
        self.search_show_button_r.pack(side='left', padx=2, pady=2, fill='x')
        row_four.pack(anchor='w')

        # Creating Text area to display search result.
        self.search_results_text_r = tk.Text(recomm)
        self.search_results_text_r.pack(side='left', fill='both', padx=5, pady=5, expand=True)
        # Showing default text.
        self.search_results_text_r.insert(tk.END, '"Enter recommendation condition and click on Get Recommendation button"')
        self.search_results_text_r.config(state=tk.DISABLED)
        # Scrollbar to scroll through the data in the text widget.
        scrollbar = tk.Scrollbar(recomm, command=self.search_results_text.yview)
        scrollbar.pack(side='right', fill='y')
        self.search_results_text_r.config(yscrollcommand=scrollbar.set)

    # Creating GUI to show pie chart in Rating notebook.
    def rating(self):
        ratings = ttk.Frame(self.__nb)
        self.__nb.add(ratings, text="Ratings")
        pie_chart = tk.Frame(ratings)
        pie_chart.pack()
        # Creating button to display pie chart for Movies and TV Shows.
        self.generate_pie_chart = tk.Button(pie_chart, text="Generate Pie Chart", command=self.getPieChart)
        self.generate_pie_chart.pack(padx=5, pady=5)
        pie_frame = tk.Frame(ratings)
        pie_frame.pack()
        # Creating two canvas to display two pie charts.
        self.pie1 = tk.Canvas(pie_frame, height=250, width=250)
        self.pie1.pack(side='left', padx=5, pady=30)
        self.pie2 = tk.Canvas(pie_frame, height=250, width=250)
        self.pie2.pack(side='right', padx=5, pady=30)

    # Function to print pie chart.
    def getPieChart(self):
        # Showing Error message in case generate pie chart button is clicked without loading the shows details.
        if self.__loadshows_flag == 0:
            messagebox.showwarning("Error", f"Please load Show file before generating.")
            return
        # Getting Movie stats details.
        movie = self.__rec_obj.getMovieStats()
        # Getting TV Stats details.
        shows = self.__rec_obj.getTVStats()
        # Two lists to store movies label and percentage.
        movie_label = []
        movie_per = []
        # Two lists to store shows label and percentage.
        show_label = []
        show_per = []
        # Splitting the received string and storing the rating name and percentage in the list for movies.
        for i in range(1, len(movie)):
            if movie[i] == "":
                break
            st = movie[i].split(" ")
            movie_label.append(st[0])
            movie_per.append(float(st[2][0:len(st[2])-1]))
        # Splitting the received string and storing the rating name and percentage in the list for shoes.
        for i in range(1, len(shows)):
            if shows[i] == "":
                break
            st = shows[i].split(" ")
            show_label.append(st[0])
            show_per.append(float(st[2][0:len(st[2])-1]))

        # Sorting the list with movie details.
        pairs = list(zip(movie_label, movie_per))
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        movie_label, movie_per = zip(*sorted_pairs)

        # Sorting the list with shows details.
        pairs = list(zip(show_label, show_per))
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        show_label, show_per = zip(*sorted_pairs)

        # Converting Tuple to list.
        movie_label = list(movie_label)
        movie_per = list(movie_per)
        show_label = list(show_label)
        show_per = list(show_per)

        # Arranging the movie data in list for a pie chart for less text overlap in pie chart.
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

        # Arranging the shows data in list for a pie chart for less text overlap in pie chart.
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

        # Displaying pie chart.
        pie1, ax1 = plt.subplots(figsize=(7, 7))
        ax1.pie(movie_per, labels=movie_label, autopct='%1.2f%%', startangle=90)
        ax1.set_title("Movies Ratings pie chart:")
        pie_chart1 = FigureCanvasTkAgg(pie1, master=self.pie1)
        pie_chart1.get_tk_widget().pack()

        # Displaying pie chart.
        pie2, ax2 = plt.subplots(figsize=(7, 7))
        ax2.pie(show_per, labels=show_label, autopct='%1.2f%%', startangle=90)
        ax2.set_title("Shows Ratings pie chart:")
        pie_chart2 = FigureCanvasTkAgg(pie2, master=self.pie2)
        pie_chart2.get_tk_widget().pack()

    # Function to draw button widgets.
    def buttons(self):
        button = tk.Frame(self.__main_window)

        # Button to load shows.
        shows = tk.Button(button, text='Load Shows', command=self.loadShows)

        # Button to load books.
        books = tk.Button(button, text='Load Books', command=self.loadBooks)

        # Button to load associations.
        recommen = tk.Button(button, text='Load Recommendations', command=self.loadAssociations)

        # Button to show the names and date of completion.
        info = tk.Button(button, text='Information', command=self.creditInfoBox)

        # Button to quit the mainloop.
        quits = tk.Button(button, text='Quit', command=self.__main_window.quit)

        button.pack(padx=2, side="bottom", pady=5)
        shows.pack(side="left", padx=80)
        books.pack(side="left", padx=80)
        recommen.pack(side="left", padx=80)
        info.pack(side="left", padx=80)
        quits.pack(side="left", padx=80)

    # Function to insert data in the entry widgets of the movies and TV shows.
    def loadShows(self):
        # Variable to keep track if shows are loaded or not.
        self.__loadshows_flag = 1

        # Making the entry fields editable to insert data.
        self.first_entry.configure(state=tk.NORMAL)
        self.second_entry.configure(state=tk.NORMAL)
        self.firsts_entry.configure(state=tk.NORMAL)
        self.seconds_entry.configure(state=tk.NORMAL)

        # Calling loadShows function in Recommender.py to load shows data.
        self.__rec_obj.loadShows()

        # To get movie list.
        movie_names = self.__rec_obj.getMovieList()

        # To get movie stats.
        movie_statistics = self.__rec_obj.getMovieStats()

        # To get TV Show list.
        tvshow_name = self.__rec_obj.getTVList()

        #To get TV Show stats.
        tvshow_statistics = self.__rec_obj.getTVStats()

        # Deleting data in the entry widget and displaying data from received list.
        self.first_entry.delete("1.0", "end")
        for i in movie_names:
            self.first_entry.insert(tk.END, i + '\n')

        # Deleting data in the entry widget and displaying data from received list.
        self.second_entry.delete("1.0", "end")
        for i in movie_statistics:
            self.second_entry.insert(tk.END, i + '\n')

        # Deleting data in the entry widget and displaying data from received list.
        self.firsts_entry.delete("1.0", "end")
        for i in tvshow_name:
            self.firsts_entry.insert(tk.END, i + '\n')

        # Deleting data in the entry widget and displaying data from received list.
        self.seconds_entry.delete("1.0", "end")
        for i in tvshow_statistics:
            self.seconds_entry.insert(tk.END, i + '\n')

        # Making the field Non-editable again.
        self.first_entry.configure(state=tk.DISABLED)
        self.second_entry.configure(state=tk.DISABLED)
        self.firsts_entry.configure(state=tk.DISABLED)
        self.seconds_entry.configure(state=tk.DISABLED)

    # Function to Load book details.
    def loadBooks(self):
        # Making fields editable.
        self.firstb_entry.configure(state=tk.NORMAL)
        self.secondb_entry.configure(state=tk.NORMAL)

        # Loading book details.
        self.__rec_obj.loadBooks()

        # Getting book list.
        books_names = self.__rec_obj.getBookList()

        # Getting book stats.
        books_statistics = self.__rec_obj.getBookStats()

        # Deleting data in the entry field and inserting data in received list.
        self.firstb_entry.delete("1.0", "end")
        for i in books_names:
            self.firstb_entry.insert(tk.END, i + '\n')

        # Deleting data in the entry field and inserting data in received list.
        self.secondb_entry.delete("1.0", "end")
        for i in books_statistics:
            self.secondb_entry.insert(tk.END, i + '\n')

        # Making fields editable again.
        self.firstb_entry.configure(state=tk.DISABLED)
        self.secondb_entry.configure(state=tk.DISABLED)

    def loadAssociations(self):
        # To load association data.
        self.__rec_obj.loadAssociations()
        self.__loadassociations = 1

    def creditInfoBox(self):
        # To display credit details.
        messagebox.showinfo("Project details","Group Members:\n1. Sunil Virendra Gupta\n2. Sainithya Surasani\n3. Nihal Reddy Akula\n\nProjected completed on: 5/5/2024")

    # Function to display result after searching with given criteria.
    def searchShows(self):
        # To get data from combobox.
        type_show = self.type_combobox.get()
        # Storing None in case of empty string.
        if type_show == "":
            type_show = None

        # To get data from Title entry.
        title = self.title_entry.get()
        if title == "":
            title = None

        # To get data from Director entry.
        director = self.director_entry.get()
        if director == "":
            director = None

        # To get data from actor entry.
        actor = self.actor_entry.get()
        if actor == "":
            actor = None

        # To get data from genre entry.
        genre = self.genre_entry.get()
        if genre == "":
            genre = None

        # Calling searchTVMovies function to get search details for the given criteria.
        stri = self.__rec_obj.searchTVMovies(type_show, title, director, actor, genre)
        self.search_results_text.configure(state=tk.NORMAL)

        # Deleting old data and inserting new data.
        self.search_results_text.delete("1.0", "end")
        for i in stri:
            self.search_results_text.insert(tk.END, i + '\n')
        self.search_results_text.configure(state=tk.DISABLED)

    # Function to display result after searching with given criteria.
    def searchBooks(self):
        # To get data from title entry widget.
        title = self.title_entry_b.get()
        if title == "":
            title = None

        # To get data from author entry widget.
        author = self.author_entry_b.get()
        if author == "":
            author = None

        # To get data from publisher entry widget.
        publisher = self.publisher_entry_b.get()
        if publisher == "":
            publisher = None

        # Calling searchBooks function to get search details for the given criteria.
        stri = self.__rec_obj.searchBooks(title, author, publisher)
        self.search_results_text_b.configure(state=tk.NORMAL)

        # Deleting old data and inserting new received data.
        self.search_results_text_b.delete("1.0", "end")
        for i in stri:
            self.search_results_text_b.insert(tk.END, i + '\n')
        self.search_results_text_b.configure(state=tk.DISABLED)

    # Function to give recommendation with given search criteria.
    def getRecommendations(self):
        if self.__loadassociations == 0:
            messagebox.showwarning("Error", f"Please load Association file before generating recommendations.")
            return

        # To get data from Type of media combobox.
        type_show = self.type_combobox_r.get()
        if type_show == "":
            type_show = None

        # To get data from title entry box.
        title = self.title_entry_r.get()
        if title == "":
            title = None

        # Calling getRecommendations function to get search details for the given criteria.
        stri = self.__rec_obj.getRecommendations(type_show, title)
        self.search_results_text_r.configure(state=tk.NORMAL)
        self.search_results_text_r.delete("1.0", "end")
        self.search_results_text_r.insert(tk.END, stri)
        self.search_results_text_r.configure(state=tk.DISABLED)


    def run(self):
        self.__main_window.mainloop()


def main():
    gui = RecommenderGUI()
    gui.run()


main()
