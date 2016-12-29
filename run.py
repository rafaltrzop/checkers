from checkers import app
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '--production':
        port = int(os.getenv('PORT'))
        app.run(host='0.0.0.0', port=port, debug=False)
    else:
        app.run(host='0.0.0.0', debug=True)
