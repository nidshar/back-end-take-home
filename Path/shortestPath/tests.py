import pytest

        
@pytest.mark.parametrize(
    "source,destination,expected_result",
    [
        ("YYZ","JFK","YYZ -> JFK"),
        ("YYZ","YVR","YYZ -> JFK -> LAX -> YVR"),
        ("YYZ","ORD","No Route"),
        ("XXX","YYZ","Invalid Origin"),
        ("ORD","XXX","Invalid Destination")
    ]
)
def test_path(db,client,source,destination,expected_result):
    response = client.get(f"/path/?source={source}&destination={destination}")
    assert response.status_code == 200
    assert response.content.decode("utf-8") == expected_result
    
    