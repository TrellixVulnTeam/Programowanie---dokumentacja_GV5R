class TooManyPagesReadError(ValueError):
  pass

class Book:
  def __init__(self, name: str, page_count: int) -> None:
    self.name = name
    self.page_count = page_count
    self.pages_read = 0

  def __repr__(self) -> str:
    return (
      f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
    )

  def read(self, pages: int) -> None:
    if self.pages_read + pages > self.page_count:
      raise TooManyPagesReadError(
        f"You tried to read {self.pages_read + pages} pages, but book has only {self.page_count} pages."
      )
    self.pages_read += pages
    print(f"you have now read {self.pages_read} pages out of {self.page_count}.")

python101 = Book("Python 101", 50)

try:
  python101.read(35)
  python101.read(50)
except TooManyPagesReadError as message:
  print(message)