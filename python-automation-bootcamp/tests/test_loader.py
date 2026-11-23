import json

import pytest
from oop_basics import TestDataLoader


@pytest.mark.parametrize("json_content, expected_exception, expected_count",
    [
        ('{"scenario":[{"id":"Test-001"}]}',TypeError,0),
        ('{"scenarios":[]}',ValueError,0),
        ('{"scenarios"-[{"id":"Test"}]}',json.JSONDecodeError,0),
        ('{"scenarios":[{"id":"Test-001"}]}',None,1)

    ]
)                      
def test_loader(tmp_path, json_content, expected_exception, expected_count):
    file_path=tmp_path/"test_scenario.json"
    
    file_path.write_text(
        json_content,
        encoding="utf-8"
    )

    if expected_exception:
        with pytest.raises(expected_exception):
            TestDataLoader.load_scenarios(file_path)
    else:
        data=TestDataLoader.load_scenarios(file_path)
        assert len(data)==expected_count



