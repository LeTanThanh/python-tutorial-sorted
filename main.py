if __name__ == "__main__":
  # Introduction to the Python sorted() function

  """
  sorted(list)
  sorted(list, reverse = True)
  """

  # Using Python sorted() function to sort a list of strings

  guests = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer"]
  sorted_guests = sorted(guests)
  print(guests)
  print(sorted_guests)

  guests = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer"]
  sorted_guests = sorted(guests, reverse = True)
  print(guests)
  print(sorted_guests)

  # Using Python sorted() function to sort a list of numbers

  scores = [5, 7, 4, 6, 9, 8]
  sorted_scores = sorted(scores)
  print(scores)
  print(sorted_scores)

  scores = [5, 7, 4, 6, 9, 8]
  sorted_scores = sorted(scores, reverse = True)
  print(scores)
  print(sorted_scores)
