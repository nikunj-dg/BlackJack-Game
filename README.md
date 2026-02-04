# Blackjack CLI Game (Python)

A command-line implementation of the classic Blackjack (21) card game built using Python and object-oriented programming principles.

This game allows a player to play against a dealer, place bets, track balance, and follow standard Blackjack rules.

## Game Rules

- Try to get as close to 21 as possible without going over.
- Dealer hits until their hand value reaches 17.
- Face cards (Jack, Queen, King) are worth 10.
- Aces count as 1 or 11 (automatically adjusted).
- Player starts with a balance of $1000.
- Player can Hit or Stand.
- Bets are deducted or added based on the outcome.

## Features

- Full 52-card deck
- Deck shuffling
- Hit or Stand logic
- Betting system with balance tracking
- Automatic Ace value adjustment
- Dealer AI (hits until 17)
- Replay option
- Object-Oriented Design

## Project Structure

This project is implemented using OOP with the following classes:

### Card

Represents a single playing card.

### Deck

Creates a standard 52-card deck

Shuffles cards

Deals one card at a time

### Hand

Tracks player's cards

Calculates hand value

Adjusts for Aces

Manages player balance

## Snippet 

<img width="659" height="412" alt="image" src="https://github.com/user-attachments/assets/1cfd3dbe-3efb-49e1-bac1-c3a52a984aba" />

<img width="653" height="373" alt="image" src="https://github.com/user-attachments/assets/92f5f02a-4c40-4885-8b28-0c0a67f7d16a" />

## Usage

python main.py

## Future Improvements

- Input validation for bet amount
- Prevent betting more than balance
- Blackjack detection (natural 21)
- Split and Double Down options
- Persistent balance storage
- Convert to GUI (Tkinter / Pygame)
- Add unit tests
