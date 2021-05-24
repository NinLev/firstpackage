from mlproject.distance import haversine

def test_haversine():
    
    distance = haversine(48.865070, 2.380009, 52.53426920651234, 13.378269069628614)

    assert isinstance(distance, float) is True
    assert distance == 1287.7924964466247