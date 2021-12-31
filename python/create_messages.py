def match_messages(name, match):
	text = """\
Hello {0},

This year you will be buying for: {1}
""".format(name, match)
	html = """\
	<html>
	  <body>
	    <p>Hello {0},<br>
	       This year you will be buying for: {1}<br>
	    </p>
	  </body>
	</html>
	""".format(name, match)
	return text, html

def test_messages(name):
	text = """\
Hello {0},

This is a test. Please reply if you have questions or comments.
""".format(name)
	html = """\
	<html>
	  <body>
	    <p>Hello {0},<br>
	       This is a test. Please reply if you have questions or comments.<br>
	    </p>
	  </body>
	</html>
	""".format(name)
	return text, html