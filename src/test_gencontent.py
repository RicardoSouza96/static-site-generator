import unittest

from gencontent import extract_title

class TestGenContent(unittest.TestCase):
    
    def test_simple_h1_header(self):
        """Test extracting a simple H1 header"""
        markdown = "# Hello World"
        result = extract_title(markdown)
        self.assertEqual(result, "Hello World")
    
    def test_h1_with_extra_spaces(self):
        """Test H1 header with leading/trailing spaces"""
        markdown = "#   Hello World   "
        result = extract_title(markdown)
        self.assertEqual(result, "Hello World")
    
    def test_h1_with_newline(self):
        """Test H1 header with newline after"""
        markdown = "# Hello World\n"
        result = extract_title(markdown)
        self.assertEqual(result, "Hello World")
    
    def test_h1_with_trailing_newlines(self):
        """Test H1 header with multiple newlines after"""
        markdown = "# Hello World\n\n\n"
        result = extract_title(markdown)
        self.assertEqual(result, "Hello World")
    
    def test_h1_with_special_characters(self):
        """Test H1 header with special characters"""
        markdown = "# Hello @#$%^ World!"
        result = extract_title(markdown)
        self.assertEqual(result, "Hello @#$%^ World!")
    
    def test_h1_with_numbers(self):
        """Test H1 header with numbers"""
        markdown = "# Title 123"
        result = extract_title(markdown)
        self.assertEqual(result, "Title 123")
    
    def test_h1_with_unicode(self):
        """Test H1 header with unicode characters"""
        markdown = "# 你好世界"
        result = extract_title(markdown)
        self.assertEqual(result, "你好世界")
    
    def test_h1_with_emoji(self):
        """Test H1 header with emoji"""
        markdown = "# 🚀 Hello World"
        result = extract_title(markdown)
        self.assertEqual(result, "🚀 Hello World")
    
    def test_no_h1_raises_exception(self):
        """Test that exception is raised when no H1 header exists"""
        markdown = "Hello World"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "There's no h1 header")
    
    def test_no_h1_empty_string(self):
        """Test that exception is raised for empty string"""
        markdown = ""
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "There's no h1 header")
    
    def test_h2_not_detected(self):
        """Test that H2 header is not detected as H1"""
        markdown = "## Hello World"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "There's no h1 header")
    
    def test_h1_with_markdown_after(self):
        """Test H1 header with markdown formatting after"""
        markdown = "# Hello *World*"
        result = extract_title(markdown)
        self.assertEqual(result, "Hello *World*")

if __name__ == '__main__':
    unittest.main()