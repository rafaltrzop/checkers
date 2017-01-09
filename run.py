from checkers import app
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == '--heroku':
            port = int(os.getenv('PORT'))
            app.run(host='0.0.0.0', port=port, debug=False)

        if sys.argv[1] == '--wierzba':
            app.run(host='0.0.0.0', port=5028, debug=True)
    else:
        app.run(host='0.0.0.0', debug=True)
