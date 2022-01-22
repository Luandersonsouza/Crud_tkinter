from tkinter import *
from tkinter import ttk
import sqlite3

window = Tk()
class functions():
	def clear_frame_1(self):
		self.code_entry.delete(0, END)
		self.name_entry.delete(0, END)
		self.phone_entry.delete(0, END)
		self.city_entry.delete(0,END)


	def db_connection(self):
		self.conn = sqlite3.connect("customers.db")
		self.cursor = self.conn.cursor();print("connecting to database")


	def db_disconnection(self):
		self.conn.close();print("disconnecting from database")


	def create_tables_db(self):
		self.db_connection() 
		self.cursor.execute("""
			CREATE TABLE IF NOT EXISTS customers( 
				code INTEGER PRIMARY KEY,
				name_customers CHAR(40) NOT NULL,
				phone INTEGER(20),
				city CHAR(40)
			);
		""")
		self.conn.commit(); print("Created database")
		self.db_disconnection()


	def add_customer(self):
		self.code = self.code_entry.get()
		self.name = self.name_entry.get()
		self.phone = self.phone_entry.get()
		self.city = self.city_entry.get()

		self.db_connection()

		self.cursor.execute(""" INSERT INTO customers (name_customers, phone, city)
				VALUES (?,?,?)""", (self.name, self.phone, self.city))
		self.conn.commit()
		self.db_disconnection()
		self.select_list()
		self.clear_frame_1()


	def select_list(self):
		self.listaCli.delete(*self.listaCli.get_children())
		self.db_connection()
		lista = self.cursor.execute("""	SELECT code, name_customers, phone, city FROM customers
					ORDER BY name_customers ASC; """)
		for i in lista:
			self.listaCli.insert("", END, values=i)
			self.db_disconnection()


class aplication(functions):
	def __init__(self):
		self.window = window
		self.screen()
		self.frames_in_screen()
		self.widgets_Frame_1()
		self.widgets_Frame_2()
		self.create_tables_db()
		self.select_list()
		window.mainloop()


	def screen(self):
		self.window.title("customer registration")
		self.window.configure(background= '#6495ED')
		self.window.geometry("700x500")
		self.window.resizable(True, True)
		self.window.maxsize(width = 900, height= 700)
		self.window.minsize(width = 500, height= 400)


	def frames_in_screen(self):
		self.frame_1= Frame(self.window, bd=4, bg='#B0C4DE', highlightbackground='#D3D3D3', highlightthickness=3)
		self.frame_1.place(relx = 0.02, rely=0.02, relwidth = 0.96, relheight = 0.46)
		

		self.frame_2= Frame(self.window, bd=4, bg='#B0C4DE', highlightbackground='#D3D3D3', highlightthickness=3)
		self.frame_2.place(relx = 0.02, rely=0.5, relwidth = 0.96, relheight = 0.46)


	def widgets_Frame_1(self):
		#creating the clear button
		self.button_clear = Button(self.frame_1, text="Clear", bd = 2, bg = '#107db2',
									 fg = 'white', font = ('verdana', 8, 'bold'), command = self.clear_frame_1)
		self.button_clear.place(relx= 0.2, rely= 0.15,relwidth=0.1, relheight=0.15)

		#creanting the search button
		self.button_search = Button(self.frame_1, text="Search",bd = 2, bg = '#107db2',
									 fg = 'white', font = ('verdana', 8, 'bold'))
		self.button_search.place(relx= 0.3, rely= 0.15,relwidth=0.1, relheight=0.15)


		#creating the new button
		self.button_new = Button(self.frame_1, text="New",bd = 2, bg = '#107db2',
									 fg = 'white', font = ('verdana', 8, 'bold'), command= self.add_customer)
		self.button_new.place(relx= 0.6, rely= 0.15,relwidth=0.1, relheight=0.15)


		#creating the change button
		self.button_change = Button(self.frame_1, text="Change", bd = 2, bg = '#107db2',
									 fg = 'white', font = ('verdana', 8, 'bold'))
		self.button_change.place(relx= 0.7, rely= 0.15,relwidth=0.1, relheight=0.15)


		#creating the delete button
		self.button_delete = Button(self.frame_1, text="Delete", bd = 2, bg = '#107db2',
									 fg = 'white', font = ('verdana', 8, 'bold'))
		self.button_delete.place(relx= 0.8, rely= 0.15,relwidth=0.1, relheight=0.15)


		#label code
		self.label_code= Label(self.frame_1, text="Code", bg = '#B0C4DE')
		self.label_code.place(relx=0.05, rely=0.05)
		self.code_entry= Entry(self.frame_1)
		self.code_entry.place(relx=0.05, rely= 0.16, relwidth=0.08)


		#label name 
		self.label_name= Label(self.frame_1, text="Name", bg = '#B0C4DE')
		self.label_name.place(relx=0.05, rely=0.35)
		self.name_entry= Entry(self.frame_1)
		self.name_entry.place(relx=0.05, rely= 0.45, relwidth=0.85)


		#label telephone
		self.label_phone= Label(self.frame_1, text="Phone", bg = '#B0C4DE')
		self.label_phone.place(relx=0.05, rely=0.6)
		self.phone_entry= Entry(self.frame_1)
		self.phone_entry.place(relx=0.05, rely= 0.7, relwidth=0.4)

		#label description
		self.label_city= Label(self.frame_1, text="City", bg = '#B0C4DE')
		self.label_city.place(relx=0.5, rely=0.6)
		self.city_entry= Entry(self.frame_1)
		self.city_entry.place(relx=0.5, rely= 0.7, relwidth=0.4)


	def widgets_Frame_2(self):
		self.listaCli = ttk.Treeview(self.frame_2, height = 3, colum =("col1","col2", "col3", "col4"))
		self.listaCli.heading("#0", text = "")
		self.listaCli.heading("#1", text = "Code")
		self.listaCli.heading("#2", text = "Name")
		self.listaCli.heading("#3", text = "Phone")
		self.listaCli.heading("#4", text = "City")


		self.listaCli.column('#0', width=1)
		self.listaCli.column('#1', width=50)
		self.listaCli.column('#2', width=200)
		self.listaCli.column('#3', width=125)
		self.listaCli.column('#4', width=125)

		self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

		self.scrool_lista = Scrollbar(self.frame_2, orient='vertical')
		self.listaCli.configure(yscroll=self.scrool_lista.set)
		self.scrool_lista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight= 0.85)



aplication()