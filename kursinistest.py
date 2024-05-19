import unittest
from io import StringIO
from contextlib import redirect_stdout
from kursinis import Movie, Ticket, PremiumTicket, TicketFactory, Theater

class TestMovie(unittest.TestCase):
    def test_movie_str(self):
        movie = Movie("The Matrix", "Action", 150)
        self.assertEqual(str(movie), "The Matrix (Action) - 150 mins")

class TestTicket(unittest.TestCase):
    def test_ticket_str(self):
        movie = Movie("The Matrix", "Action", 150)
        ticket = Ticket(movie, "A1")
        self.assertEqual(str(ticket), "Standard Ticket for The Matrix, Seat A1")

class TestPremiumTicket(unittest.TestCase):
    def test_premium_ticket_str(self):
        movie = Movie("The Matrix", "Action", 150)
        premium_ticket = PremiumTicket(movie, "A1", is_vip=True)
        self.assertEqual(str(premium_ticket), "VIP Ticket for The Matrix, Seat A1")

class TestTicketFactory(unittest.TestCase):
    def test_create_ticket_standard(self):
        movie = Movie("The Matrix", "Action", 150)
        ticket = TicketFactory.create_ticket(movie, "A1")
        self.assertIsInstance(ticket, Ticket)

    def test_create_ticket_premium(self):
        movie = Movie("The Matrix", "Action", 150)
        ticket = TicketFactory.create_ticket(movie, "A1", is_vip=True)
        self.assertIsInstance(ticket, PremiumTicket)

class TestTheater(unittest.TestCase):
    def setUp(self):
        self.theater = Theater()

    def test_add_movie(self):
        movie = Movie("The Matrix", "Action", 150)
        self.theater.add_movie(movie)
        self.assertIn(movie, self.theater.movies)

if __name__ == '__main__':
    unittest.main()
