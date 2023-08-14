import bcrypt

password = b"s.F@3565%"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

#username = request.form.get("username")
#password = request.form.get("password").encode("utf-8")

if bcrypt.checkpw(password, hashed):
    print("Matched")
    
else:
    print("Did not")
    
    import time
    
    start = time.time()
    hashed= bcrypt.hashpw(password, bcrypt.gensalt(rounds=12))
    end = time.time()
    f= end - start
    print(f)