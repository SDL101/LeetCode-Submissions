class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # ransomNote = "aabb"
        # magazine = "ab"
        new_mag_array = []
        for mag_char in magazine:
            new_mag_array.append(mag_char)
            #new_mag_array = [a, b]
        for note_char in ransomNote:
            if note_char in new_mag_array:
                new_mag_array.remove(note_char)
            else:
                return False
        return True
        