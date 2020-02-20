from apps import app
import os, sys

if __name__ == "__main__":
    args = sys.argv
    args.append("run")
    
    if args[1] == "seeduser":
        from apps.test.user import seedUser
        seedUser()
    else:
        port = int(os.environ.get('PORT', 5000))
        app.run(debug=True, host='0.0.0.0', port=port)