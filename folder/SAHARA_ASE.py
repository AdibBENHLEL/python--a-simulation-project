class card :

  def __init__(self,carta):
    self.carta = cardmaker()
    print("hello")
    print(self.carta)  
  
  def cardmaker():
    
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    cardd = {
    "suit",
    "rank",
    "couleur"
    }
    cardd_tab=[]
    carddnumber = 13*4
    for i in card.suits:
      for j in card.ranks:
        
        if i in ["Hearts", "Diamonds"]:
          card = {
                    "suit": i,
                    "rank": j,
                    "couleur": 'red'
                }
                cardd_tab.append(card)
        else:
          card = {
                    "suit": i,
                    "rank": j,
                    "couleur": 'black'
                }
                cardd_tab.append(card)   
        return cardd_tab 

def test_card_class():
    # Create an instance of the card class
    my_card = card()

    # Test if the 'carta' attribute is initialized correctly
    assert hasattr(my_card, 'carta')

    # Test if the 'cardmaker' method generates cards
    cards = my_card.carta.cardmaker()

    # Verify that the number of cards generated is correct (13 ranks * 4 suits)
    assert len(cards) == 13 * 4

    # Verify that each card has the expected attributes
    for c in cards:
        assert 'suit' in c
        assert 'rank' in c
        assert 'couleur' in c

    # Verify that the colors of the cards are assigned correctly
    for c in cards:
        if c['suit'] in ["Hearts", "Diamonds"]:
            assert c['couleur'] == 'red'
        else:
            assert c['couleur'] == 'black'

if __name__ == "__main__":
    test_card_class()
    print("All tests passed.")