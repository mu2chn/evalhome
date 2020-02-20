from apps import app
import os
import sys

if __name__ == "__main__":
    args = sys.argv
    if args[1] == "user":
        import apps.test.user
    else:
        port = int(os.environ.get('PORT', 5000))
        app.run(debug=True, host='0.0.0.0', port=port)