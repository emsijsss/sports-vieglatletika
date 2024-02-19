import getpass
from rich.console import Console
from rich.table import Table

def atslegties():
  while True:
    x = str(input("Vai jūs vēlaties atslēgties? (jā/nē)" ))
    if x == "jā":
     print("Atslēgšanās veiksmīga!")
     break
    else:
      print("Ja vēlieties atslēgties, ievadiet 'jā'")
  
def main():
  a = input("Ievadi lietotājvārdu: ")
  b = getpass.getpass("Ievadi paroli: ")
  login(a,b)

def login(a,b):
    if a == "user" and b == "password":
      print("Logins veiksmīgs!")
  
      table = Table(title="Statistika")
      rows = [
        ["200m", "13.02", "23,28"],
        ["400m", "10.02", "49,78"],
        ["Augstlekšana", "08.02", "1,97"],]
    
      columns = ["Disciplīna", "Datums", "Rezultāts"]

      for column in columns:
        table.add_column(column)
    
      for row in rows:
        table.add_row(*row, style='bright_green')
    
      console = Console()
      console.print(table)
    
      table = Table(title="Treniņplāni")
      rows = [
          ["Tāllekšana", "12.02", "6,24"],
          ["Kārtslekšana", "15.02", "4.80"],
          ["Šķēpmešana", "16.02", "78.24"],
      ]
      columns = ["Disciplīna", "Datums", "Rezultāts"]
      
      for column in columns:
          table.add_column(column)
      
      for row in rows:
          table.add_row(*row, style='bright_green')
      
          console = Console()
      console.print(table) 
      atslegties()
    else:
      print("Piekļuve liegta!")
main()
