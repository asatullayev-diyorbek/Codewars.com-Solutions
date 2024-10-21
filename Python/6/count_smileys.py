"""https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python"""


valid_face = {
    ':-)', ':-D', ':~)',
    ':~D', ':)', ':D', 
    ';-)', ';-D', ';~)', 
    ';~D', ';)', ';D'
}

def count_smileys(arr):
    return sum(
        face in valid_face 
        for face in arr
    )


if __name__ == '__main__':
    test_faces = [
        ':)', ':D', ';-D', 
        ':~)', ':(', ';>', 
        ':D', ':~D', ':-C'
    ]
    print(count_smileys(test_faces))  # result: 6
