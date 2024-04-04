import streamlit as st
import random


def hangman():
    words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage",
                      "plants"]
    word = random.choice(words_to_guess)
    display = '_' * len(word)
    already_guessed = []
    limit = 5
    count = 0

    st.write(f"Welcome to Hangman, {name}!")
    st.write("The game is about to start!\nLet's play Hangman!")
    st.write(f"This is the Hangman Word: {display}")
    i =0;
    while count < limit and '_' in display:
        i +=3;
        guess = st.text_input(f"Enter your guess (single letter):", key=f"guess_{i}").lower()

        if len(guess) == 1 and guess.isalpha() and guess not in already_guessed:
            already_guessed.append(guess)
            if guess in word:
                display = ''.join([char if char in already_guessed else '_ ' for char in word])
                st.write(f"This is the Hangman Word: {display}")
            else:
                count += 1
                st.write(f"Wrong guess. {limit - count} guesses remaining")
        else:
            st.write("Invalid input. Please enter a single letter that you haven't guessed before.")

    if '_' not in display:
        st.write("Congrats! You have guessed the word correctly!")
    else:
        st.write("Wrong guess. You are hanged!!!")
        st.write("The word was:", word)

    play_again = st.radio("Do you want to play again?", ('Yes', 'No'), key="play_again")
    if play_again == 'Yes':
        hangman()
    else:
        st.write("Thanks For Playing! We expect you back again!")


name = st.text_input("Enter your name:", key="name")
hangman()
