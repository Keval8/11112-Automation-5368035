import part2_project
import part2_youtube_count


# First Question Google search Result Count
def test_result_google():
    temp_count = part2_project.result_google()
    assert temp_count >= 10


# 2nd Question YouTube Count

def test_result_youtube():
    temp_count = part2_youtube_count.result_youtube()

    assert temp_count >= 10
