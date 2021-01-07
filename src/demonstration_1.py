"""
I was bored one day and decided to look at last names in the phonebook for my
area.

I flipped open the phonebook to a random page near the middle and started
perusing. I wrote each last name that I was unfamiliar with down on paper in
increasing order. When I got to the end of the phonebook, I was having so much
fun I decided to start from the beginning and keep going until I reached the
page where I had started.

When I was finished, I had a list of interesting last names that were mostly
alphabetical. The problem was that my list starts somehere near the middle of
the alphabet, reaches the end, and then starts from the beginning of the
alphabet. In other words, my list of names is sorted, but it is "rotated."

Example:


Write a function that finds the index of the "rotation point". The "rotation
point" is where I started working from the beginning of the phone book. The
list I came up was absolutely huge, so make sure your solution is efficient.

*Note: you should be able to come up with a solution that has O(log n) time
complexity.*
"""
def find_rotation_point(surnames):
    # get the first name and use it to compare against all guesses
    first_surname = surnames[0]
    # create our search space
    start_index = 0
    end_index = len(surnames) - 1
      
    while start_index < end_index:
        # make guesses, (specifically in the middle of our space)
        guess_index = start_index + ((end_index - start_index) // 2)
        # check if the guess is lower or greater than the first_surname
        # if the guess is greater than the first_surname
        if surnames[guess_index] >= first_surname:
            start_index = guess_index
            # move the start to the next guess location
        # otherwise if the guess is lower, move the end up
        else:
            end_index = guess_index
        # if only two items left, return the lower item
        if start_index + 1 == end_index:
            # the lower item should be the end
            return end_index
        
surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]

print(find_rotation_point(surnames))
            
        
    

