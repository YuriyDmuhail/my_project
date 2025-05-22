from hw16_1 import TeamLead

def test_attributes():
    lead = TeamLead("Oksana", 5000, "IT", "Python", 4)

    assert hasattr(lead, "name")
    assert hasattr(lead, "salary")
    assert hasattr(lead, "department")
    assert hasattr(lead, "programming_language")
    assert hasattr(lead, "team_size")