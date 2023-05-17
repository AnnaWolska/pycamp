from totolotek import drew_numbers

def test_drew_numbers():
    #given
    #when
    drawn_numbers = drew_numbers()
    #then
    assert len(drawn_numbers) == 6