# Theater Management System

Coursework Report
Introduction
### What is your application?
The application is a theater management system designed to manage movies and ticketing within a theater. It includes features for adding movies, creating tickets (both standard and premium), exporting movie lists to a text file, and importing movie lists from a text file.

### How to run the program?
To run the program:

Ensure you have Python 3.8 or higher installed on your system.
Download the script file theater_management.py.
Open a terminal and navigate to the directory where the script is located.
Run the script using the command: python theater_management.py.
How to use the program?
On running the script, a theater instance is created.
Movies can be added to the theater using the add_movie method.
Tickets can be created using the TicketFactory.
The movie list can be exported to a text file using the export_movies_to_txt method.
The movie list can be imported from a text file using the import_movies_from_txt method.
The current movies can be displayed using the show_movies method.

### Implementation and Functional Requirements
Adding Movies
Movies are added to the theater using the add_movie method of the Theater class. Each movie is represented by an instance of the Movie class.

`theater = Theater()
theater.add_movie(Movie("Inception", "Sci-Fi", 148))
theater.add_movie(Movie("Interstellar", "Sci-Fi", 169))`

# Creating Tickets
Tickets are created using the TicketFactory class. Standard tickets and premium tickets (with VIP options) are supported.

`standard_ticket = TicketFactory.create_ticket(Movie("Inception", "Sci-Fi", 148), "A1")
vip_ticket = TicketFactory.create_ticket(Movie("Inception", "Sci-Fi", 148), "A2", is_vip=True)`

# Exporting and Importing Movies
Movies can be exported to and imported from a text file. This is useful for data persistence and transfer.

`theater.export_movies_to_txt("Movies.txt")
imported_theater = Theater.import_movies_from_txt("Movies.txt")`

# Code Snippets and Explanation
The Theater class follows the Singleton pattern to ensure only one instance of the theater exists. This is managed using the __new__ and __init__ methods.

`class Theater:
    _instance = None `

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Theater, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.movies = []
            self.initialized = True
### Results
- Movie Management: Successfully added and displayed movies in the theater.
- Ticket Creation: Successfully created standard and VIP tickets.
- Data Export/Import: Successfully exported and imported movie data to/from a text file.
- Singleton Implementation: Ensured a single instance of the theater class.

### Conclusions

- Achievements: Implemented a robust theater management system that manages movies and ticketing efficiently.
- Challenges: Ensuring the Singleton pattern was correctly implemented to avoid multiple instances of the theater.
- Future Prospects: Potential to extend the application with features like user management, showtimes, and online ticket booking.
