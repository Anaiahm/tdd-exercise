from main import blackjack_score
import pytest

#@pytest.mark.skip(reason="no way of currently testing this")
def test_score_for_pair_of_number_cards():
  # Arrange
  hand = [3, 4]

  # Act
  score = blackjack_score(hand)

  # Assert <-- Write assert statement here
  assert score == 7

# @pytest.mark.skip(reason="no way of currently testing this")
def test_facecards_have_values_calculated_correctly():
  #Arrange
    hand = ['King',5]
  #Act
    score =  blackjack_score(hand)
  #Assert
    assert score == 15

# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_11_where_it_does_not_go_over_21():
  #Arrange
    hand = [10,'Ace']
  #Act
    score =  blackjack_score(hand)
  #Assert
    assert score == 21


# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_1_where_11_would_bust():
    #Arrange
    hand = [10,2,'Ace',5]
  #Act
    score =  blackjack_score(hand)
  #Assert
    assert score == 18

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_invalid_cards():
      #Arrange
    hand = [10,'Apple']
  #Act
    score =  blackjack_score(hand)
  #Assert
    assert score == "INVALID"



# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_list_length_greater_than_5():
        #Arrange
    hand = [10,2,4,2,5,6]
  #Act
    score =  blackjack_score(hand)
  #Assert
    assert score == "INVALID"


# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_bust_for_scores_over_21():
          #Arrange
    hand = [10,7,7]
  #Act
    score =  blackjack_score(hand)
  #Assert
    assert score == "BUST"

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_12_for_ace_ace_king():
            #Arrange
    hand = ['Ace','Ace','King']
  #Act
    score =  blackjack_score(hand)
  #Assert
    assert score == 12

# @pytest.mark.skip(reason="logic not yet implemented")
def test_returns_14_for_ace_ace_ace_ace():
                #Arrange
    hand = ['Ace','Ace','Ace','Ace']
  #Act
    score =  blackjack_score(hand)
  #Assert
    assert score == 14